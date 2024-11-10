const puppeteer = require('puppeteer');

// Get the URL from the first command-line argument
const url = process.argv[2];

if (!url) {
  console.error("Please provide a URL as the first argument.");
  process.exit(1);
}

(async () => {
  // Launching a headless browser
  const browser = await puppeteer.launch({
    headless: true, // Runs Chromium in headless mode
  });
  const page = await browser.newPage();

 // Set a desktop viewport (you can adjust the dimensions as needed)
  await page.setViewport({
    width: 1280, // Desktop width
    height: 800, // Desktop height
  });

  // Go to the URL provided in the command-line argument
  await page.goto(url, {
    waitUntil: 'networkidle2' // Wait until the network is idle
  });

  // Take a screenshot and save it as a JPEG
  await page.screenshot({
    path: 'screenshot.jpg',
    type: 'jpeg',
    quality: 80, // Quality of JPEG from 0 to 100
    fullPage: true, // Capture the entire page
  });

  // Close the browser
  await browser.close();
  console.log('Screenshot saved as screenshot.jpg');
})();
