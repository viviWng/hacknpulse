# filename: extract_wikipedia_text.py
import requests
from bs4 import BeautifulSoup

# Fetch the content of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract the main text from the article
paragraphs = soup.find_all("p")
text = " ".join([paragraph.text for paragraph in paragraphs])

# Save the extracted text to a file
with open("wikipedia_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Text extracted and saved to 'wikipedia_text.txt'")