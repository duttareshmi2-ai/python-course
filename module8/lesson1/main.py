# API : What is an API ? API stands for Application Programming Interface . It is a set of rules that allow one software application to communicate with another . It specifies how components interact and how data can be requested and exchanged between system . APIs allow developers to access the functionality of external services without needing to know their implementation details . APIs make it easy to interact with third-party services like payment gateways , weather services , social media platforms , data storage and more . 
# API Request and Responses : An API Request is made to an API Endpoint (A specific URL provided by the API) . The Endpoint defines where the request is sent and what data is expected . 
# Types of HTTP Methods : HTTP stands for Hyper Text Transfer Protocol . Get Method : Get Method retrieves data from the server . Post Method : Sending data to server . Put Method : It updates existing data on server . Delete Method : Deletes the data from server . 
# API Response : Whe we make an API Request , the server responds with data . Most API's return responses in JSON format . JSON stands for JavaScript Object Notation . It is a lightweight data used for easy data exchange between system . 200 - stands for success ; 404 - stands for not found ; 500 - stands for internal server error .
import requests
def get_random_jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200 : 
        print(f"JSON Response : {response.json()}")
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    else : 
        return "Failed to catch joke . "
def main():
    print("Welcome to random joke generator . ")
    while True : 
        user_input = input("Press Enter to get a new joke or type q or exit to quit : ").strip().lower()
        if user_input in ("q" , "exit") : 
            print("Goodbye")
            break
        joke = get_random_jokes()
        print(joke)
if __name__ == "__main__" : 
    main()