const puppeteer = require('puppeteer');

(async () => {
  // Get URL from command-line arguments
  const url = process.argv[2];
  if (!url) {
    console.error('Usage: node screenshot.js <URL>');
    process.exit(1);
  }

  // Launch the browser
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox'], // Necessary for running in some environments
  });
  const page = await browser.newPage();

  // Set the viewport if you want a specific resolution
  await page.setViewport({ width: 1280, height: 800 });

  // Go to the provided URL
  await page.goto(url, { waitUntil: 'networkidle2' });

  // Create a PDF of the page
  await page.pdf({ path: 'website_screenshot.pdf', format: 'A4' });

  console.log('Screenshot saved as website_screenshot.pdf');

  // Close the browser
  await browser.close();
})();
