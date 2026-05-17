#!/usr/bin/env python3
"""IPATECHS Bi-Fold Company Profile PDF Generator — ReportLab"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import math, os

# ─── OUTPUT PATH ───────────────────────────────────────────────────────────────
OUTPUT = os.path.join(os.path.dirname(__file__), 'docs', 'ipatechs_bifold.pdf')
FONT_DIR = '/usr/share/fonts/truetype'

# ─── REGISTER FONTS ────────────────────────────────────────────────────────────
def reg(alias, path):
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(alias, path))
        return True
    return False

reg('DJSans',       f'{FONT_DIR}/dejavu/DejaVuSans.ttf')
reg('DJSans-Bold',  f'{FONT_DIR}/dejavu/DejaVuSans-Bold.ttf')
reg('DJSans-Light', f'{FONT_DIR}/dejavu/DejaVuSans.ttf')
reg('DJCond',       f'{FONT_DIR}/liberation/LiberationSans-Regular.ttf')
reg('DJCond-Bold',  f'{FONT_DIR}/liberation/LiberationSans-Bold.ttf')
reg('LibSans',      f'{FONT_DIR}/liberation/LiberationSans-Regular.ttf')
reg('LibSans-Bold', f'{FONT_DIR}/liberation/LiberationSans-Bold.ttf')

# ─── BRAND COLOURS ─────────────────────────────────────────────────────────────
ORANGE      = HexColor('#FF6600')
ORANGE_DIM  = HexColor('#CC5200')
DARK        = HexColor('#080808')
DARK2       = HexColor('#101010')
DARK3       = HexColor('#181818')
DARK4       = HexColor('#222222')
MUTED       = HexColor('#888888')
LIGHT       = HexColor('#F0F0F0')
ORANGE_PALE = HexColor('#FF6600', hasAlpha=True)   # tinted fills use alpha manually

W, H = A4   # 595.28 x 841.89 pt  (≈ 210 × 297 mm)

# ─── HELPERS ───────────────────────────────────────────────────────────────────
def rgba(hex_color, a):
    c = HexColor(hex_color)
    return Color(c.red, c.green, c.blue, a)

def chamfer_rect(c, x, y, w, h, cut=6):
    """Draw a chamfered (angular-cut) rectangle — top-right & bottom-left corners."""
    path = c.beginPath()
    path.moveTo(x + cut, y + h)
    path.lineTo(x + w,   y + h)
    path.lineTo(x + w,   y + cut)
    path.lineTo(x + w - cut, y)
    path.lineTo(x,       y)
    path.lineTo(x,       y + h - cut)
    path.close()
    return path

def chamfer_rect_all(c, x, y, w, h, cut=5):
    """Chamfer all 4 corners."""
    path = c.beginPath()
    path.moveTo(x + cut,     y + h)
    path.lineTo(x + w - cut, y + h)
    path.lineTo(x + w,       y + h - cut)
    path.lineTo(x + w,       y + cut)
    path.lineTo(x + w - cut, y)
    path.lineTo(x + cut,     y)
    path.lineTo(x,           y + cut)
    path.lineTo(x,           y + h - cut)
    path.close()
    return path

def text_box(c, txt, font, size, color, x, y, w, align='left', leading=None):
    """Draw wrapped paragraph text."""
    if leading is None:
        leading = size * 1.35
    style = ParagraphStyle('s', fontName=font, fontSize=size,
                           textColor=color, leading=leading,
                           alignment={'left': TA_LEFT, 'center': TA_CENTER, 'right': TA_RIGHT}[align])
    p = Paragraph(txt, style)
    pw, ph = p.wrap(w, 9999)
    p.drawOn(c, x, y - ph)
    return ph

def label_row(c, txt, x, y, line_w=18):
    """Orange label with leading rule — e.g. '— SECTION LABEL'."""
    c.setFillColor(ORANGE)
    c.rect(x, y + 3.5, line_w, 1.5, fill=1, stroke=0)
    c.setFont('DJCond-Bold', 7)
    c.setFillColor(ORANGE)
    c._charSpace = 3.5
    c.drawString(x + line_w + 6, y, txt.upper())
    c._charSpace = 0

def section_title(c, line1, line2_accent, x, y, size=30):
    c.setFont('DJCond-Bold', size)
    c.setFillColor(white)
    c.drawString(x, y, line1)
    c.setFillColor(ORANGE)
    c.drawString(x, y - size * 1.1, line2_accent)

def orange_stripe(c, x, y, w, h):
    c.setFillColor(ORANGE)
    c.rect(x, y, w, h, fill=1, stroke=0)

def dark_rect(c, x, y, w, h, color=None):
    c.setFillColor(color or DARK3)
    c.rect(x, y, w, h, fill=1, stroke=0)

def noise_rect(c, x, y, w, h, alpha=0.04):
    """Simulate subtle texture with very faint random-looking dots."""
    c.saveState()
    c.setFillColor(rgba('#FFFFFF', alpha))
    step = 6
    import random; random.seed(42)
    for ix in range(x, x + w, step):
        for iy in range(y, y + h, step):
            if random.random() < 0.4:
                c.rect(ix + random.uniform(0, step), iy + random.uniform(0, step),
                       0.6, 0.6, fill=1, stroke=0)
    c.restoreState()

def grid_lines(c, x, y, w, h, spacing=40, alpha=0.03):
    c.saveState()
    c.setStrokeColor(rgba('#FFFFFF', alpha))
    c.setLineWidth(0.3)
    for ix in range(0, int(w) + spacing, spacing):
        c.line(x + ix, y, x + ix, y + h)
    for iy in range(0, int(h) + spacing, spacing):
        c.line(x, y + iy, x + w, y + iy)
    c.restoreState()

def gradient_rect(c, x, y, w, h, col1, col2, steps=60, vertical=True):
    """Simple gradient using thin slices."""
    for i in range(steps):
        t = i / steps
        r = col1.red   + t * (col2.red   - col1.red)
        g = col1.green + t * (col2.green - col1.green)
        b = col1.blue  + t * (col2.blue  - col1.blue)
        a = col1.alpha + t * (col2.alpha - col1.alpha) if hasattr(col1, 'alpha') else 1
        c.setFillColor(Color(r, g, b, a))
        if vertical:
            sy = y + h - (i + 1) * h / steps
            c.rect(x, sy, w, h / steps + 0.5, fill=1, stroke=0)
        else:
            sx = x + i * w / steps
            c.rect(sx, y, w / steps + 0.5, h, fill=1, stroke=0)

def check_item(c, txt, x, y, font='DJSans', size=8.5):
    """Orange check mark + text."""
    c.setFillColor(ORANGE)
    c.setFont('DJCond-Bold', 9)
    c.drawString(x, y, '►')
    c.setFont(font, size)
    c.setFillColor(LIGHT)
    c.drawString(x + 11, y, txt)
    return size * 1.6

def icon_box(c, x, y, size=20):
    """Draw a chamfered orange-tinted icon box, return centre."""
    c.saveState()
    c.setFillColor(rgba('#FF6600', 0.12))
    path = chamfer_rect_all(c, x, y, size, size, cut=4)
    c.drawPath(path, fill=1, stroke=0)
    c.setStrokeColor(rgba('#FF6600', 0.35))
    c.setLineWidth(0.6)
    c.drawPath(path, fill=0, stroke=1)
    c.restoreState()
    return x + size / 2, y + size / 2

def divider(c, x, y, w, alpha=0.1):
    c.setStrokeColor(rgba('#FFFFFF', alpha))
    c.setLineWidth(0.5)
    c.line(x, y, x + w, y)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — FRONT COVER
# ═══════════════════════════════════════════════════════════════════════════════
def draw_cover(c):
    # Full dark background
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Grid lines overlay
    grid_lines(c, 0, 0, W, H, spacing=45, alpha=0.035)

    # Diagonal orange slab — bottom portion
    slab_h = H * 0.44
    path = c.beginPath()
    path.moveTo(0,  slab_h * 0.30)
    path.lineTo(W,  0)
    path.lineTo(W,  slab_h)
    path.lineTo(0,  slab_h)
    path.close()
    c.setFillColor(ORANGE)
    c.drawPath(path, fill=1, stroke=0)

    # Dark gradient overlay over slab (to darken it)
    gradient_rect(c, 0, 0, W, slab_h * 0.8,
                  Color(0.03, 0.03, 0.03, 0.5),
                  Color(0.03, 0.03, 0.03, 0.0))

    # Radial atmospheric orange glow (top-right quadrant) — painted as faint rect
    c.saveState()
    c.setFillColor(rgba('#FF6600', 0.06))
    c.ellipse(W * 0.55, H * 0.4, W * 1.4, H * 1.05, fill=1, stroke=0)
    c.restoreState()

    # ── LOGO (top-left) ────────────────────────────────────────────────────────
    lx, ly = 18*mm, H - 18*mm
    # Hex icon box
    box_s = 28
    c.setFillColor(ORANGE)
    path = chamfer_rect_all(c, lx, ly - box_s, box_s, box_s, cut=5)
    c.drawPath(path, fill=1, stroke=0)
    # Gear icon in box (simplified cross)
    c.setFillColor(black)
    c.setFont('DJCond-Bold', 14)
    c.drawCentredString(lx + box_s / 2, ly - box_s + 7, '⚙')

    c.setFont('DJCond-Bold', 22)
    c.setFillColor(white)
    c.drawString(lx + box_s + 7, ly - 20, 'IPATECHS')
    c.setFillColor(ORANGE)
    c.drawString(lx + box_s + 7, ly - 36, 'CO LTD')

    # Badge top-right
    bx, by = W - 18*mm - 60, ly - 22
    c.setStrokeColor(rgba('#FFFFFF', 0.18))
    c.setLineWidth(0.6)
    c.rect(bx, by, 60, 18, stroke=1, fill=0)
    c.setFont('DJCond-Bold', 6.5)
    c.setFillColor(rgba('#FFFFFF', 0.55))
    c._charSpace = 2.5
    c.drawCentredString(bx + 30, by + 6, 'COMPANY PROFILE 2025')
    c._charSpace = 0

    # ── HERO HEADLINE ──────────────────────────────────────────────────────────
    hx = 18*mm
    hy_base = H * 0.55

    # Eyebrow
    label_row(c, 'Est. 2019  ·  Dar es Salaam, Tanzania', hx, hy_base + 10*mm)

    # Title  — 3 lines
    c.saveState()
    c.setFont('DJCond-Bold', 66)
    c.setFillColor(white)
    c.drawString(hx, hy_base - 2,  'YOUR GLOBAL')

    # Outline style text (simulated with stroke)
    c.setFont('DJCond-Bold', 66)
    c.setFillColor(DARK)
    c.setStrokeColor(white)
    c.setLineWidth(0.8)
    c.drawString(hx, hy_base - 68, 'PARTNER IN')
    c.setFillColor(white)
    c.setStrokeColor(white)
    c.setLineWidth(0.3)
    c.drawString(hx, hy_base - 68, 'PARTNER IN')

    c.setFillColor(DARK)
    c.setStrokeColor(DARK)
    c.setLineWidth(0)
    c.setFont('DJCond-Bold', 66)
    c.setFillColor(DARK)
    c.drawString(hx, hy_base - 134, 'ENGINEERING')
    c.restoreState()

    # Sub-text
    sub = ("East Africa's trusted supplier of industrial spare parts, precision "
           "engineering solutions, and construction equipment. Connecting global "
           "brands to local industries since 2019.")
    c.saveState()
    c.setFont('DJSans-Light', 9.5)
    c.setFillColor(rgba('#F0F0F0', 0.65))
    tw = 155*mm
    # word-wrap manually
    words = sub.split()
    lines_sub = []
    line = ''
    for w_ in words:
        test = (line + ' ' + w_).strip()
        if c.stringWidth(test, 'DJSans-Light', 9.5) < tw:
            line = test
        else:
            lines_sub.append(line)
            line = w_
    lines_sub.append(line)
    sy = hy_base - 175
    for ln in lines_sub:
        c.drawString(hx, sy, ln)
        sy -= 15
    c.restoreState()

    # ── STATS STRIP ────────────────────────────────────────────────────────────
    stats_y = 55*mm
    divider(c, hx, stats_y + 12*mm, 170*mm, alpha=0.15)
    stats = [('6+', 'YEARS\nEXPERIENCE'), ('150+', 'CLIENTS\nSERVED'), ('29+', 'GLOBAL\nBRANDS'), ('12', 'INDUSTRIES\nCOVERED')]
    sx = hx
    for num, lbl in stats:
        c.setFont('DJCond-Bold', 32)
        c.setFillColor(white)
        c.drawString(sx, stats_y + 6*mm, num)
        c.setFont('DJCond', 7)
        c.setFillColor(rgba('#888888', 1))
        c._charSpace = 1.5
        for i, ln in enumerate(lbl.split('\n')):
            c.drawString(sx, stats_y + 3*mm - i * 9, ln)
        c._charSpace = 0
        sx += 42*mm

    # ── BOTTOM TICKER BAND ─────────────────────────────────────────────────────
    band_h = 11*mm
    orange_stripe(c, 0, 0, W, band_h)
    ticker_items = ['Industrial Parts', '◆', 'Mechanical Eng.', '◆', 'Electrical Eng.',
                    '◆', 'Mining Solutions', '◆', 'Power & Energy', '◆', 'Petroleum & Gas',
                    '◆', 'Automation', '◆', 'Construction']
    tx = 10*mm
    c.setFont('DJCond-Bold', 7.5)
    c.setFillColor(black)
    c._charSpace = 2
    ty = band_h / 2 - 3
    for item in ticker_items:
        c.drawString(tx, ty, item)
        tx += c.stringWidth(item, 'DJCond-Bold', 7.5) / 1 + 8
        if tx > W - 10*mm:
            break
    c._charSpace = 0

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — INSIDE LEFT  (About, Vision/Mission, Values, Stats)
# ═══════════════════════════════════════════════════════════════════════════════
def draw_inside_left(c):
    # Background
    c.setFillColor(DARK2)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── TOP IMAGE STRIP ──────────────────────────────────────────────────────
    strip_h = 70*mm
    # Simulate image with dark-tinted gradient
    gradient_rect(c, 0, H - strip_h, W, strip_h,
                  Color(0.06, 0.07, 0.07, 1),
                  Color(0.18, 0.18, 0.18, 1), vertical=False)
    # Industrial pattern (grid lines on strip)
    grid_lines(c, 0, H - strip_h, W, strip_h, spacing=30, alpha=0.06)
    # Orange accent gradient overlay
    gradient_rect(c, 0, H - strip_h, W * 0.4, strip_h,
                  Color(ORANGE.red, ORANGE.green, ORANGE.blue, 0.12),
                  Color(ORANGE.red, ORANGE.green, ORANGE.blue, 0.0), vertical=False)
    # Bottom fade to DARK2
    gradient_rect(c, 0, H - strip_h, W, strip_h * 0.45,
                  Color(0.063, 0.063, 0.063, 1),
                  Color(0.063, 0.063, 0.063, 0.0))

    # Industrial cross-hatch detail
    c.saveState()
    c.setStrokeColor(rgba('#FF6600', 0.08))
    c.setLineWidth(0.4)
    for i in range(0, int(W), 20):
        c.line(i, H - strip_h, i + strip_h, H)
    c.restoreState()

    # Year badge on strip
    badge_x = W - 38*mm
    badge_y = H - strip_h + 18*mm
    badge_w, badge_h = 28*mm, 22*mm
    c.setFillColor(ORANGE)
    path = chamfer_rect_all(c, badge_x, badge_y, badge_w, badge_h, cut=5)
    c.drawPath(path, fill=1, stroke=0)
    c.setFont('DJCond-Bold', 22)
    c.setFillColor(black)
    c.drawCentredString(badge_x + badge_w / 2, badge_y + badge_h - 17, '2019')
    c.setFont('DJCond-Bold', 7)
    c._charSpace = 1.5
    c.drawCentredString(badge_x + badge_w / 2, badge_y + 5, 'FOUNDED')
    c._charSpace = 0

    # Label + title on strip
    lx = 15*mm
    label_row(c, 'Who We Are', lx, H - strip_h + 25*mm)
    c.setFont('DJCond-Bold', 32)
    c.setFillColor(white)
    c.drawString(lx, H - strip_h + 8*mm, 'ABOUT ')
    c.setFillColor(ORANGE)
    aw = c.stringWidth('ABOUT ', 'DJCond-Bold', 32)
    c.drawString(lx + aw, H - strip_h + 8*mm, 'IPATECHS')

    # ── BODY ────────────────────────────────────────────────────────────────
    bx = 15*mm
    by = H - strip_h - 8*mm

    # INTRO paragraphs
    intro_lines = [
        "IPATECHS COMPANY LIMITED is a globally recognised leader in the supply and distribution "
        "of industrial spare parts, engineering solutions, and construction machinery.",
        "We serve Tanzania and the wider East African region with a commitment to quality, innovation, "
        "and reliable service — bridging world-class global manufacturers with local industrial needs.",
    ]
    c.setFont('DJSans-Light', 9)
    c.setFillColor(rgba('#F0F0F0', 0.70))
    iy = by
    for para in intro_lines:
        words = para.split()
        line = ''
        for w_ in words:
            test = (line + ' ' + w_).strip()
            if c.stringWidth(test, 'DJSans-Light', 9) < W - 30*mm:
                line = test
            else:
                c.drawString(bx, iy, line)
                iy -= 13
                line = w_
        c.drawString(bx, iy, line)
        iy -= 18

    # ── VISION & MISSION CARDS ───────────────────────────────────────────────
    iy -= 4
    card_h = 32*mm
    card_w = (W - 35*mm) / 2
    for i, (title_str, body) in enumerate([
        ('OUR VISION',
         'To be a global leader in advanced engineering solutions, industrial spare parts, '
         'and construction equipment — empowering businesses with innovative, sustainable solutions.'),
        ('OUR MISSION',
         'To supply world-class products tailored to client needs, ensure timely delivery reducing '
         'operational downtime, and foster long-term partnerships with clients and global brands.'),
    ]):
        cx = bx + i * (card_w + 5*mm)
        # Card background
        c.setFillColor(DARK3)
        path = chamfer_rect_all(c, cx, iy - card_h, card_w, card_h, cut=5)
        c.drawPath(path, fill=1, stroke=0)
        # Top orange border
        c.setFillColor(ORANGE)
        c.rect(cx, iy - 1.5, card_w, 2, fill=1, stroke=0)
        # Title
        c.setFont('DJCond-Bold', 13)
        c.setFillColor(white)
        c.drawString(cx + 4*mm, iy - 8*mm, title_str)
        # Body
        c.setFont('DJSans', 7.5)
        c.setFillColor(rgba('#F0F0F0', 0.60))
        words = body.split()
        line = ''
        ty = iy - 14*mm
        for w_ in words:
            test = (line + ' ' + w_).strip()
            if c.stringWidth(test, 'DJSans', 7.5) < card_w - 8*mm:
                line = test
            else:
                c.drawString(cx + 4*mm, ty, line)
                ty -= 11
                line = w_
        c.drawString(cx + 4*mm, ty, line)

    iy -= card_h + 8*mm

    # ── CORE VALUES ──────────────────────────────────────────────────────────
    divider(c, bx, iy, W - 30*mm)
    iy -= 6
    c.setFont('DJCond-Bold', 11)
    c.setFillColor(white)
    c._charSpace = 2
    c.drawString(bx, iy - 5, 'CORE VALUES')
    c._charSpace = 0
    iy -= 16

    vals = [
        ('Quality First',     'Only certified genuine products from vetted global manufacturers'),
        ('Timely Delivery',   'Efficient logistics networks minimising operational downtime'),
        ('Client Focus',      'Long-term relationships built on trust and technical expertise'),
        ('Sustainability',    'Promoting energy-efficient and eco-friendly technologies'),
    ]
    col_w = (W - 30*mm) / 2
    for idx, (vtitle, vdesc) in enumerate(vals):
        col = idx % 2
        row = idx // 2
        vx = bx + col * (col_w + 5*mm)
        vy = iy - row * 22*mm

        # Icon box
        icon_box(c, vx, vy - 16, size=16)
        # Title + desc
        c.setFont('DJCond-Bold', 9.5)
        c.setFillColor(white)
        c.drawString(vx + 20, vy - 8, vtitle.upper())
        c.setFont('DJSans', 7.5)
        c.setFillColor(MUTED)
        c.drawString(vx + 20, vy - 18, vdesc)

    iy -= 50

    # ── STATS STRIP ──────────────────────────────────────────────────────────
    strip_sy = 14*mm
    c.setFillColor(DARK3)
    c.rect(0, strip_sy, W, 20*mm, fill=1, stroke=0)
    divider(c, 0, strip_sy + 20*mm, W)
    divider(c, 0, strip_sy, W)

    stats = [('2019', 'YEAR FOUNDED'), ('6+', 'YEARS ACTIVE'), ('150+', 'CLIENTS SERVED'), ('29+', 'BRAND PARTNERS'), ('12', 'INDUSTRIES')]
    sw = W / len(stats)
    for i, (num, lbl) in enumerate(stats):
        sx = i * sw
        if i > 0:
            c.setStrokeColor(rgba('#FFFFFF', 0.07))
            c.setLineWidth(0.5)
            c.line(sx, strip_sy, sx, strip_sy + 20*mm)
        c.setFont('DJCond-Bold', 20)
        c.setFillColor(white)
        nw = c.stringWidth(num, 'DJCond-Bold', 20)
        c.drawString(sx + sw / 2 - nw / 2, strip_sy + 11*mm, num)
        c.setFont('DJCond-Bold', 6)
        c.setFillColor(MUTED)
        c._charSpace = 1.5
        lw = c.stringWidth(lbl, 'DJCond-Bold', 6)
        c.drawString(sx + sw / 2 - lw / 2, strip_sy + 5*mm, lbl)
        c._charSpace = 0

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — INSIDE RIGHT  (Services 3×3 + Partners + Industries)
# ═══════════════════════════════════════════════════════════════════════════════
def draw_inside_right(c):
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    grid_lines(c, 0, 0, W, H, spacing=50, alpha=0.025)

    bx = 15*mm

    # HEADER
    label_row(c, 'Key Services & Specializations', bx, H - 16*mm)
    c.setFont('DJCond-Bold', 30)
    c.setFillColor(white)
    c.drawString(bx, H - 28*mm, 'WHAT WE ')
    ow = c.stringWidth('WHAT WE ', 'DJCond-Bold', 30)
    c.setFillColor(ORANGE)
    c.drawString(bx + ow, H - 28*mm, 'DELIVER')

    # ── SERVICE CARDS 3×3 ────────────────────────────────────────────────────
    services = [
        ('01', 'Industrial Spare Parts',   'Bearings, belts, hydraulics, seals, pumps & filtration.'),
        ('02', 'Mechanical Engineering',   'Motors, gearboxes, valves & precision tooling.'),
        ('03', 'Electrical Engineering',   'Switchgears, VFDs, cables & power distribution.'),
        ('04', 'Material Engineering',     'Alloys, heat-resistant steels & composites.'),
        ('05', 'Petroleum & Gas',          'Pipelines, valves, flow control & safety systems.'),
        ('06', 'Power & Energy',           'Generators, turbines, solar & wind solutions.'),
        ('07', 'Mining Solutions',         'Crushers, conveyors & heavy excavation machinery.'),
        ('08', 'Automation Engineering',   'PLCs, SCADA, robotics & IoT control systems.'),
        ('09', 'Construction Sector',      'CAT & Komatsu machinery, cranes & spares.'),
    ]

    cols = 3
    top_y = H - 38*mm
    card_w = (W - 30*mm - (cols - 1) * 3) / cols
    card_h = 28*mm
    row_gap = 3

    for idx, (num, title, desc) in enumerate(services):
        col = idx % cols
        row = idx // cols
        cx = bx + col * (card_w + 3)
        cy = top_y - row * (card_h + row_gap) - card_h

        # Card background
        c.setFillColor(DARK2)
        c.rect(cx, cy, card_w, card_h, fill=1, stroke=0)

        # Orange bottom border on accent cards
        if idx in (0, 5, 8):
            c.setFillColor(ORANGE)
            c.rect(cx, cy, card_w, 1.5, fill=1, stroke=0)

        # Ghost number
        c.saveState()
        c.setFont('DJCond-Bold', 28)
        c.setFillColor(rgba('#FFFFFF', 0.04))
        c.drawString(cx + card_w - 22, cy + card_h - 20, num)
        c.restoreState()

        # Icon
        icon_box(c, cx + 3, cy + card_h - 15, size=12)

        # Title
        c.setFont('DJCond-Bold', 9)
        c.setFillColor(white)
        c.drawString(cx + 4, cy + card_h - 20, title.upper())

        # Desc
        c.setFont('DJSans', 7)
        c.setFillColor(MUTED)
        words = desc.split()
        line = ''
        ty = cy + card_h - 30
        for w_ in words:
            test = (line + ' ' + w_).strip()
            if c.stringWidth(test, 'DJSans', 7) < card_w - 7:
                line = test
            else:
                c.drawString(cx + 4, ty, line)
                ty -= 9
                line = w_
        c.drawString(cx + 4, ty, line)

    # ── BRAND PARTNERS ───────────────────────────────────────────────────────
    brand_y = top_y - 3 * (card_h + row_gap) - 10*mm
    divider(c, bx, brand_y, W - 30*mm)
    brand_y -= 6

    c.setFont('DJCond-Bold', 10)
    c.setFillColor(white)
    c._charSpace = 2
    c.drawString(bx, brand_y - 5, 'OUR GLOBAL BRAND PARTNERS')
    c._charSpace = 0
    brand_y -= 15

    brands = ['ABB', 'Siemens', 'SKF', 'Cummins', 'Grundfos',
              'Honeywell', 'Schneider', 'Timken', 'Caterpillar', 'Endress+H.']
    pill_w = (W - 30*mm - 9 * 4) / 10
    pill_h = 14*mm
    for i, brand in enumerate(brands):
        px = bx + i * (pill_w + 4)
        py = brand_y - pill_h
        # White pill
        c.setFillColor(white)
        path = chamfer_rect_all(c, px, py, pill_w, pill_h, cut=3)
        c.drawPath(path, fill=1, stroke=0)
        c.setFont('DJCond-Bold', 6.5)
        c.setFillColor(HexColor('#333333'))
        bw = c.stringWidth(brand, 'DJCond-Bold', 6.5)
        c.drawString(px + pill_w / 2 - bw / 2, py + pill_h / 2 - 3, brand)

    # ── INDUSTRIES SERVED TAGS ───────────────────────────────────────────────
    ind_y = brand_y - pill_h - 10*mm
    divider(c, bx, ind_y, W - 30*mm)
    ind_y -= 6

    c.setFont('DJCond-Bold', 10)
    c.setFillColor(white)
    c._charSpace = 2
    c.drawString(bx, ind_y - 5, 'INDUSTRIES WE SERVE')
    c._charSpace = 0
    ind_y -= 14

    industries = ['Port Handling', 'Oil & Gas', 'Automation & Control', 'Mining',
                  'Cement', 'Water & Wastewater', 'Power Generation', 'Refrigeration',
                  'Filtration', 'Electrical', 'Mechanical', 'General Engineering']
    tag_x = bx
    tag_y = ind_y
    for tag in industries:
        tag_w = c.stringWidth(tag, 'DJCond-Bold', 7.5) + 12
        tag_h = 10
        if tag_x + tag_w > W - 15*mm:
            tag_x = bx
            tag_y -= 14
        # Background
        c.setFillColor(rgba('#FF6600', 0.10))
        c.rect(tag_x, tag_y, tag_w, tag_h, fill=1, stroke=0)
        c.setStrokeColor(rgba('#FF6600', 0.30))
        c.setLineWidth(0.5)
        c.rect(tag_x, tag_y, tag_w, tag_h, fill=0, stroke=1)
        c.setFont('DJCond-Bold', 7.5)
        c.setFillColor(ORANGE)
        c.drawString(tag_x + 6, tag_y + 2, tag)
        tag_x += tag_w + 4

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — BACK COVER  (Why IPATECHS + Contact)
# ═══════════════════════════════════════════════════════════════════════════════
def draw_back_cover(c):
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    grid_lines(c, 0, 0, W, H, spacing=40, alpha=0.03)

    # Left orange stripe
    c.setFillColor(ORANGE)
    c.rect(0, 0, 5*mm, H, fill=1, stroke=0)

    # ── TOP IMAGE STRIP ──────────────────────────────────────────────────────
    strip_h = 58*mm
    gradient_rect(c, 0, H - strip_h, W, strip_h,
                  Color(0.12, 0.13, 0.13, 1),
                  Color(0.06, 0.06, 0.06, 1), vertical=False)
    grid_lines(c, 0, H - strip_h, W, strip_h, spacing=25, alpha=0.08)

    # Industrial silhouette bars (machinery simulation)
    c.saveState()
    c.setFillColor(rgba('#FF6600', 0.07))
    for i, (sx, sy, sw, sh) in enumerate([
        (30, H - strip_h, 8, strip_h * 0.7),
        (55, H - strip_h, 12, strip_h * 0.9),
        (82, H - strip_h, 6, strip_h * 0.5),
        (100, H - strip_h, 18, strip_h * 0.8),
        (130, H - strip_h, 10, strip_h * 0.6),
        (160, H - strip_h, 14, strip_h),
        (190, H - strip_h, 8, strip_h * 0.75),
    ]):
        c.rect(sx*mm, sy, sw*mm, sh, fill=1, stroke=0)
    c.restoreState()

    # Fade strip bottom to dark
    gradient_rect(c, 0, H - strip_h, W, strip_h * 0.5,
                  Color(0.03, 0.03, 0.03, 1),
                  Color(0.03, 0.03, 0.03, 0.0))

    # ── HEADER ───────────────────────────────────────────────────────────────
    lx = 20*mm
    label_row(c, 'Why IPATECHS', lx, H - strip_h - 10*mm)
    c.setFont('DJCond-Bold', 30)
    c.setFillColor(white)
    c.drawString(lx, H - strip_h - 22*mm, 'THE ')
    tw = c.stringWidth('THE ', 'DJCond-Bold', 30)
    c.setFillColor(ORANGE)
    c.drawString(lx + tw, H - strip_h - 22*mm, 'IPATECHS')
    tw2 = c.stringWidth('IPATECHS', 'DJCond-Bold', 30)
    c.setFillColor(white)
    c.drawString(lx + tw + tw2, H - strip_h - 22*mm, ' ADVANTAGE')

    # ── WHY US GRID (2×3) ────────────────────────────────────────────────────
    why_items = [
        ('01', 'Comprehensive Offerings',
         'Complete end-to-end solutions from spare parts to heavy construction machinery.'),
        ('02', 'Global Brand Expertise',
         'Partnerships with ABB, Siemens, SKF, Cummins & 25+ world-leading brands.'),
        ('03', 'Timely Delivery',
         'Strategic sourcing and logistics networks keep your operations running.'),
        ('04', 'Customised Solutions',
         'Tailored products and services solving your specific engineering challenges.'),
        ('05', 'Local East Africa Presence',
         'Deep knowledge of Tanzanian & East African industrial and regulatory needs.'),
        ('06', 'Sustainability Commitment',
         'Energy-efficient technologies: solar, smart energy management & green solutions.'),
    ]

    top_w = H - strip_h - 35*mm
    w_card_w = (W - 35*mm) / 2
    w_card_h = 24*mm

    for idx, (num, title, desc) in enumerate(why_items):
        col = idx % 2
        row = idx // 2
        wx = lx + col * (w_card_w + 5*mm)
        wy = top_w - row * (w_card_h + 3) - w_card_h

        # Card
        c.setFillColor(DARK2)
        c.rect(wx, wy, w_card_w, w_card_h, fill=1, stroke=0)

        # Ghost number
        c.saveState()
        c.setFont('DJCond-Bold', 30)
        c.setFillColor(rgba('#FF6600', 0.12))
        c.drawString(wx + w_card_w - 24, wy + w_card_h - 22, num)
        c.restoreState()

        # Title
        c.setFont('DJCond-Bold', 9.5)
        c.setFillColor(white)
        c.drawString(wx + 5, wy + w_card_h - 9, title.upper())

        # Desc
        c.setFont('DJSans', 7.5)
        c.setFillColor(MUTED)
        words = desc.split()
        line = ''
        ty = wy + w_card_h - 18
        for w_ in words:
            test = (line + ' ' + w_).strip()
            if c.stringWidth(test, 'DJSans', 7.5) < w_card_w - 10:
                line = test
            else:
                c.drawString(wx + 5, ty, line)
                ty -= 9.5
                line = w_
        c.drawString(wx + 5, ty, line)

    # ── CONTACT BLOCK ────────────────────────────────────────────────────────
    contact_y_top = top_w - 3 * (w_card_h + 3) - 10*mm
    block_h = 42*mm
    contact_y = contact_y_top - block_h

    # Orange chamfered block
    c.setFillColor(ORANGE)
    path = chamfer_rect_all(c, lx, contact_y, W - 35*mm, block_h, cut=7)
    c.drawPath(path, fill=1, stroke=0)

    # Title
    c.setFont('DJCond-Bold', 22)
    c.setFillColor(black)
    c.drawString(lx + 6*mm, contact_y + block_h - 12*mm, 'GET IN TOUCH WITH US')

    # Contact items (2×2 grid)
    contacts = [
        ('ADDRESS', 'Makongo Road, Postal Code 14129\nDar es Salaam, Tanzania'),
        ('PHONE',   '+255 750 304 097'),
        ('EMAIL',   'info@ipatechs.com'),
        ('WEBSITE', 'www.ipatechs.com'),
    ]
    ci_w = (W - 35*mm - 12*mm) / 2
    for i, (lbl, val) in enumerate(contacts):
        col = i % 2
        row = i // 2
        cx_ = lx + 6*mm + col * (ci_w + 4*mm)
        cy_ = contact_y + block_h - 20*mm - row * 16*mm

        c.setFont('DJCond-Bold', 6.5)
        c.setFillColor(rgba('#000000', 0.55))
        c._charSpace = 2
        c.drawString(cx_, cy_, lbl)
        c._charSpace = 0
        c.setFont('DJSans-Bold', 8.5)
        c.setFillColor(black)
        for j, line in enumerate(val.split('\n')):
            c.drawString(cx_, cy_ - 10 - j * 10, line)

    # ── BOTTOM FOOTER ────────────────────────────────────────────────────────
    divider(c, lx, 10*mm, W - 35*mm)
    c.setFont('DJCond-Bold', 18)
    c.setFillColor(white)
    c.drawString(lx, 5.5*mm, 'IPA')
    bw = c.stringWidth('IPA', 'DJCond-Bold', 18)
    c.setFillColor(ORANGE)
    c.drawString(lx + bw, 5.5*mm, 'TECHS CO LTD')
    c.setFont('DJCond', 7)
    c.setFillColor(MUTED)
    c._charSpace = 1.5
    c.drawRightString(W - 15*mm, 5.5*mm, '© 2025  ·  INDUSTRIAL PARTS · ENGINEERING EXCELLENCE')
    c._charSpace = 0

# ═══════════════════════════════════════════════════════════════════════════════
# BUILD PDF
# ═══════════════════════════════════════════════════════════════════════════════
def build():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle('IPATECHS Company Limited — Corporate Profile 2025')
    c.setAuthor('IPATECHS Company Limited')
    c.setSubject('Industrial Spare Parts, Engineering Solutions & Construction Equipment')

    # Page 1 — Front Cover
    draw_cover(c)
    c.showPage()

    # Page 2 — Inside Left
    draw_inside_left(c)
    c.showPage()

    # Page 3 — Inside Right
    draw_inside_right(c)
    c.showPage()

    # Page 4 — Back Cover
    draw_back_cover(c)
    c.showPage()

    c.save()
    print(f'✓ PDF saved: {OUTPUT}')
    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f'  File size: {size_kb:.1f} KB')

if __name__ == '__main__':
    build()
