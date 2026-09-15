class DataHelper:
    def __init__(self, data):
        self.data = data
        print("Object created!")

    def show_data(self):
        for i, value in enumerate(self.data):
            print(i, value)

    def __del__(self):
        print("Object destroyed!")

# Example
helper = DataHelper(["Math", "Science", "English"])
helper.show_data()
