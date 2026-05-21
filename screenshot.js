const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage();

  // Desktop initial
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('http://localhost:8080/index.html');
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: '/tmp/apple-desktop.png', fullPage: true });

  // With form open (ITC selected)
  await page.click('#card-itc');
  await page.waitForTimeout(500);
  await page.screenshot({ path: '/tmp/apple-form.png', fullPage: true });

  // Mobile
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('http://localhost:8080/index.html');
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: '/tmp/apple-mobile.png', fullPage: true });

  await browser.close();
  console.log('done');
})();
