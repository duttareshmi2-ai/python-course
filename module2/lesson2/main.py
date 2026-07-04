from textblob import TextBlob
from rich.console import Console

c = Console()
c.print("🐍 Welcome to the Sentiment spy 🐍", style="cyan")

history = []

while True:
    user_sentiment = input(
        "Enter a sentence to help the Sentiment spy to check your sentiment or write reset, history or exit: "
    )

    if user_sentiment.lower() == "exit":
        c.print("Exiting the Sentiment spy. Goodbye!", style="cyan")
        break

    if user_sentiment.lower() == "reset":
        history.clear()
        c.print("History cleared.", style="yellow")
        continue

    if user_sentiment.lower() == "history":
        if history:
            c.print("Sentiment history:", style="magenta")
            for item in history:
                c.print(f"- {item}", style="white")
        else:
            c.print("No history yet.", style="yellow")
        continue

    analysis = TextBlob(user_sentiment)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
        style = "green"
    elif polarity < 0:
        sentiment = "negative"
        style = "red"
    else:
        sentiment = "neutral"
        style = "blue"

    history.append(f"{user_sentiment} -> {sentiment}")
    c.print(f"Sentiment: {sentiment} (polarity: {polarity:.2f})", style=style)
