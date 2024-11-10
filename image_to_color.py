import base64
from openai import OpenAI
import os
import json

image_path = "./screenshot.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(image_path)

# Set API key (make sure to keep this secure in a real implementation)
#
# Initialize OpenAI client
client = OpenAI()

# Create the request with the base64-encoded image
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Give me the main theme color in color code and the color of majority text dont consider footer text.Return in json format dont include ```json```.Name of fields mainThemeColor and majorityTextColor"},
            {

              "type": "image_url",
              "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ],
        }
    ],
    max_tokens=300,
)

parsed_content = json.loads(response.choices[0].message.content)  # Parse if response is a valid JSON string
# Print the response
with open("color.json", "w", encoding="utf-8") as json_file:
    json.dump(parsed_content, json_file, ensure_ascii=False, indent=4)

# Print confirmation
print("Response and color theme saved to color.json!")
