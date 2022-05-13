from textblob import TextBlob


def outcome(polarity):
    """Returns the sentiment [positive/negative or neutral] based on polarity"""
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"


with open("sample_data.txt", encoding="utf-8") as sample_file:
    data = sample_file.readlines()
    for line in data:
        print(line, end=" ")
        text = TextBlob(line)
        # A general text block, meant for larger bodies of text (esp. those containing sentences). Inherits from
        # BaseBlob  .
        sentiment = text.sentiment.polarity
        # Return a tuple of form (polarity, subjectivity ) where polarity is a float within the range [-1.0,
        # 1.0] and subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very
        # subjective.
        print(f'{outcome(sentiment)} \n')
