import random

num = "123"              # treat as string
digits = list(num)       # convert to list of characters
random.shuffle(digits)   # shuffle the list
shuffled_num = "".join(digits)  # join back into string

print(shuffled_num)