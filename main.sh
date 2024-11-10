#!/bin/bash

# Check if URL is passed as an argument
if [ -z "$1" ]; then
  echo "Usage: ./generate_pdf.sh <URL>"
  exit 1
fi

URL="$1"
OUTPUT_FILE="website_screenshot.pdf"

# Run Chrome in headless mode to generate PDF
chromium --headless --disable-gpu --print-to-pdf="$OUTPUT_FILE" "$URL"

echo "PDF saved as $OUTPUT_FILE"
