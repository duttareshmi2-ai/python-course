# Step 1: Pair book names with copy counts using zip()
books = ["Harry Potter", "Percy Jackson", "Narnia", "Sherlock Holmes"]
copies = [3, 0, 5, 2]

library = dict(zip(books, copies))
print("Library stock:", library)

# Step 2: Filter available books (copies > 0)
available_books = {book: count for book, count in library.items() if count > 0}
print("Available books:", available_books)

# Step 3: Update late fees using map() with a normal function
def add_fee(fee):
    return fee + 5   # increase each fee by ₹5

late_fees = [10, 20, 15, 25]  # fees for each book
updated_fees = list(map(add_fee, late_fees))
print("Updated late fees:", updated_fees)

# Step 4: Stop program early if chosen book is unavailable
chosen_book = "Percy Jackson"
if library.get(chosen_book, 0) == 0:
    print(f"Sorry, '{chosen_book}' is unavailable. Exiting program...")
    exit()

print(f"You can borrow '{chosen_book}'!")
