# filename: wikipedia_summary_newspaper3k.py
from newspaper import Article

# Fetch the content of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
article = Article(url)
article.download()
article.parse()

# Generate a summary of the article
article.nlp()
summary = article.summary

print(summary)