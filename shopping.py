# Shopping Discount Calculator

def calculate_discount(bill_amount, discount_percent):
    discount = (bill_amount * discount_percent) / 100
    final_amount = bill_amount - discount
    return final_amount

while True:   # repeat until valid input
    try:
        bill = float(input("Enter your shopping bill amount: "))
        discount = float(input("Enter discount percentage: "))

        if bill < 0 or discount < 0:
            raise ValueError("Negative values are not allowed.")

    except ValueError as ve:
        print("❌ Value Error:", ve)
        print("Please enter positive numbers only.\n")

    except TypeError as te:
        print("❌ Type Error:", te)
        print("Please enter numbers only.\n")

    else:
        # executed only if no error occurs
        final_bill = calculate_discount(bill, discount)
        print(f"✅ Final bill after {discount}% discount: {final_bill}")
        break   # stop loop once valid details are entered

    finally:
        # always runs, whether error or not
        print("Attempt finished.\n")
