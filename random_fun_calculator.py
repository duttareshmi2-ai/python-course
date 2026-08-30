import random
import math

# --- Step 1: Lucky Number ---
lucky_number = random.randint(1, 100)
print("🎲 Your Lucky Number is:", lucky_number)

# --- Step 2: Random Activity ---
activities = ["Play football", "Read a book", "Draw a picture", "Listen to music", "Dance"]
chosen_activity = random.choice(activities)
print("🎉 Random Activity for you:", chosen_activity)

# --- Step 3: Number Guessing Game ---
secret_number = random.randint(1, 10)
print("\n🔢 Guess the secret number between 1 and 10!")

guess = int(input("Enter your guess: "))
if guess == secret_number:
    print("✅ Correct! You guessed it!")
else:
    print("❌ Wrong! The secret number was:", secret_number)

# --- Step 4: Explore math functions ---
print("\n🧮 Exploring math functions:")

num1 = 5.7
num2 = -3.2
num3 = 12
num4 = 18

print("ceil(5.7):", math.ceil(num1))       # rounds up
print("floor(5.7):", math.floor(num1))     # rounds down
print("copysign(5.7, -3.2):", math.copysign(num1, num2))  # gives 5.7 with sign of -3.2
print("fabs(-3.2):", math.fabs(num2))      # absolute value
print("gcd(12, 18):", math.gcd(num3, num4)) # greatest common divisor
