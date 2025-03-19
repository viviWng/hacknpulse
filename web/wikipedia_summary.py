# filename: wikipedia_summary.py
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

# Fetch the content of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract the main text from the article
paragraphs = soup.find_all("p")
text = " ".join([paragraph.text for paragraph in paragraphs])

# Generate a summary of the article
summary = summarize(text, ratio=0.2)

print(summary)