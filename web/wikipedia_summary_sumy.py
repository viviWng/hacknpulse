# filename: wikipedia_summary_sumy.py
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Fetch the content of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
parser = HtmlParser.from_url(url, Tokenizer("english"))

# Generate a summary of the article using LSA Summarizer
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 5)  # Specify the number of sentences in the summary

for sentence in summary:
    print(sentence)
