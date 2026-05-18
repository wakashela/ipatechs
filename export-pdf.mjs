import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, 'ipatechs_bifold_v0.0.1.html');
const pdfPath = path.join(__dirname, 'docs', 'ipatechs_bifold_v0.0.1.pdf');

async function exportPdf() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 2480, height: 3508 },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();

  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle', timeout: 30000 });

  await page.addStyleTag({
    content: `@page { size: 210mm 297mm; margin: 0; }`,
  });

  await page.waitForTimeout(3000);
  await page.evaluate(() => document.fonts.ready);

  await page.pdf({
    path: pdfPath,
    width: '210mm',
    height: '297mm',
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
    scale: 1,
    displayHeaderFooter: false,
    pageRanges: '',
  });

  console.log(`PDF exported to: ${pdfPath}`);
  await browser.close();
}

exportPdf().catch((err) => {
  console.error('PDF export failed:', err);
  process.exit(1);
});
