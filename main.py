import logging
import sys
import os
import argparse
import json
import nltk
nltk.download('punkt')

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Define command-line argument parsing
parser = argparse.ArgumentParser(description="Web scraper using LlamaIndex")
parser.add_argument("url", type=str, help="The URL of the webpage to scrape")

# Parse the arguments
args = parser.parse_args()
url = args.url

# Load data from the provided URL
documents = SimpleWebPageReader(html_to_text=True).load_data([url])

# Print the loaded document (for debugging or verification)
print(documents[0])

# Create the index
index = SummaryIndex.from_documents(documents)

# Set logging to DEBUG for more detailed outputs (if needed)
query_engine = index.as_query_engine()

# Query the index for information in JSON format
response = query_engine.query("Give me name, phone number, locations and logo path if no logo then empty,Also return the color codes of theme.Give output in json. Don't include ```json```")

# Check if the response has a method to get the result as JSON or dictionary
# Adjust based on the library documentation
response_data = json.loads(f"{response}")
print(response_data)

# Save the response to a JSON file
file_path = "index.json"
with open(file_path, "w") as file:
    json.dump(response_data, file)

print(f"Response saved in file: {file_path}")
