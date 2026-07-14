from textblob import TextBlob

def get_movie_recommendation(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        return "Try: Chhota Bheem and the Throne of Bali - a simple and fun Indian kids movie."
    elif polarity < -0.2:
        return "Try: Motu Patlu: King of Kings - a light and cheerful Indian cartoon movie."
    else:
        return "Try: Bhoothnath Returns - a gentle and family-friendly Indian movie."

user_input = input("Describe your mood or feeling: ")
polarity = TextBlob(user_input).sentiment.polarity

print("Sentiment polarity:", round(polarity, 3))
print(get_movie_recommendation(user_input)) 