from textblob import TextBlob
from newspaper import Article
import nltk

url = 'https://www.wionews.com/world/finland-likely-to-join-nato-this-summer-minister-lintila-to-wion-471933'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
