# filename: wikipedia_summary_no_library.py
import requests
from bs4 import BeautifulSoup

# Fetch the content of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract the main text from the article
paragraphs = soup.find_all("p")
text = " ".join([paragraph.text for paragraph in paragraphs])

# Print the extracted text
print(text)