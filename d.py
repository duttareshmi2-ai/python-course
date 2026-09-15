class Account:
    def __init__(self, pin):
        self.__pin = pin

    def set_pin(self, new_pin):
        self.__pin = new_pin

    def __str__(self):
        return "Account PIN is hidden for safety."

# Example
a = Account(1234)
print(a)
a.set_pin(5678)
print(a)
