# Rule-based chatbot using only built-in Python features.
# It can give trip packing tips and book suggestions.

print("Hi! My name is Dumbai.")
print("I can help you with packing tips for trips or book suggestions.")
print("Type 'trip', 'book', or 'exit' to stop.")

while True:
    user_input = input("What would you like help with? ").strip().lower()

    if user_input in ["exit", "bye", "quit"]:
        print("Bye! Have a safe trip and happy reading.")
        break

    if "trip" in user_input or "pack" in user_input or "travel" in user_input:
        print("Here are some trip packing tips:")
        print("1. Make a checklist before you pack.")
        print("2. Pack only the things you really need.")
        print("3. Put important items in your handbag.")
        print("4. Carry a small first-aid kit.")
        print("5. Check the weather before traveling.")

    elif "book" in user_input or "read" in user_input:
        print("Here are some book suggestions:")
        print("1. The Alchemist by Paulo Coelho")
        print("2. Think and Grow Rich by Napoleon Hill")
        print("3. Harry Potter by J.K. Rowling")
        print("4. Atomic Habits by James Clear")

    else:
        print("I can help with trip packing or book recommendations.")
        print("Try asking about 'trip' or 'book'.")