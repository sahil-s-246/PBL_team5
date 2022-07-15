from textblob import TextBlob


def outcome(polarity):
    """Returns the sentiment [positive/negative or neutral] based on polarity"""
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"


while True:
    line = input("Enter a sentence: ")
    print(line, end=" ")
    text = TextBlob(line)
    # A general text block, meant for larger bodies of text (esp. those containing sentences). Inherits from
    # BaseBlob  .
    sentiment = text.sentiment.polarity

    print(f'result: {outcome(sentiment)} \n')
