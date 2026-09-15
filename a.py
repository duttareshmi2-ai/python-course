class Pet:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Age:", self.age)

# Example
p = Pet("Buddy", "Golden Retriever", 3)
p.show_info()
