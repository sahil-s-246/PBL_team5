from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from training_data import training_data


def give_output(sentiment):
    if sentiment == "pos":
        return "positive"
    elif sentiment == "neg":
        return "negative"
    else:
        return "neutral"


TEST_STRING1 = "This is one of the better products that have been released this year." \
               "I would recommend it to everyone"
TEST_STRING2 = "I dont like this product It has several flaws in it that need to be addressed immediately"
test = [TEST_STRING1, TEST_STRING2]
classifier = NaiveBayesClassifier(training_data)
# A classifier based on the Naive Bayes algorithm, as implemented in NLTK.
for line in test:
    text = TextBlob(line, classifier=classifier)

    result = text.classify()
    print(f"{line} : {give_output(result)}")
