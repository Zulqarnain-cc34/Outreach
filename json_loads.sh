
if [ -z "$1" ]; then
  echo "Usage: ./generate_pdf.sh <URL>"
  exit 1
fi

URL="$1"

python main.py "$URL"

cd ./screenshot

node index.js "$URL"

mv screenshot.jpg ../

cd ../

python image_to_color.py
