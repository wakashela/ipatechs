// NAV SCROLL
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
    document.getElementById('back-top').classList.toggle('visible', window.scrollY > 400);
});

// HAMBURGER
const ham = document.getElementById('hamburger'), mob = document.getElementById('mobileMenu');
ham.addEventListener('click', () => { ham.classList.toggle('open'); mob.classList.toggle('open'); });
mob.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { ham.classList.remove('open'); mob.classList.remove('open'); }));

// COUNTER
function animateCount(el, target, duration = 1800) {
    let start = 0, startTime = null;
    const step = ts => { if (!startTime) startTime = ts; const p = Math.min((ts - startTime) / duration, 1); const e = 1 - Math.pow(1 - p, 3); el.textContent = Math.floor(e * target); if (p < 1) requestAnimationFrame(step); else el.textContent = target; };
    requestAnimationFrame(step);
}
const statsObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { animateCount(document.getElementById('stat-years'), 6); animateCount(document.getElementById('stat-clients'), 150); animateCount(document.getElementById('stat-products'), 50); animateCount(document.getElementById('stat-industries'), 10); statsObs.disconnect(); } });
}, { threshold: 0.3 });
const heroStats = document.querySelector('.hero-stats');
if (heroStats) statsObs.observe(heroStats);

// REVEAL
const revObs = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }); }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
document.querySelectorAll('.reveal,.reveal-left,.reveal-right').forEach(el => revObs.observe(el));

// TABS
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
    });
});

// MODAL
function openModal(productName) { document.getElementById('modalProductName').textContent = productName; document.getElementById('modalOverlay').classList.add('open'); }
function closeModal() { document.getElementById('modalOverlay').classList.remove('open'); }
function closeModalOutside(e) { if (e.target === document.getElementById('modalOverlay')) closeModal(); }
function submitEnquiry() {
    const name = document.getElementById('enquiryName').value.trim();
    const email = document.getElementById('enquiryEmail').value.trim();
    const msg = document.getElementById('enquiryMessage').value.trim();
    if (!name || !email || !msg) { alert('Please fill in all required fields.'); return; }
    alert('Thank you for your enquiry! Our team will contact you shortly.\n\nYou can also reach us at:\nPhone: +255 750 304 097\nEmail: info@ipatechs.com');
    closeModal();
    ['enquiryName', 'enquiryEmail', 'enquiryPhone', 'enquiryCompany', 'enquiryMessage'].forEach(id => document.getElementById(id).value = '');
}

// ACTIVE NAV
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');
const activeObs = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) { navLinks.forEach(a => a.style.color = ''); const active = document.querySelector('.nav-links a[href="#' + e.target.id + '"]'); if (active) active.style.color = 'var(--white)'; } }); }, { threshold: 0.4 });
sections.forEach(s => activeObs.observe(s));
