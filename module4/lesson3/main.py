# Dictionary : It's a collection that stores data in key value pairs . 
# data={
#     "name" : "Adwaita Das",
#     "age" : 10,
#     "school" : "South Point",
#     "class" : 5
# }
# print(data["name"])
# print(data.get("age"))
# print(data)
# data["hobby"]="chess"
# print(data)
# data["age"]=11
# print(data)
# data.pop("school")
# print(data)
# del data["age"]
# print(data)
# data.clear()
# print(data)
# print(len(data))
# for key in data:
#     print(key)
# for value in data.values():
#     print(value)
# for key,value in data.items() : 
#     print(key , ": " , value)
# Activity : Outline : 
# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
# Activity : Outline:
# Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
# Activity : Outline:
# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

# Dictionary of students (id -> details)

student_data = {

"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},

"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},

"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"}, # duplicate of id1

"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},

}

result = {}

seen_keys = [] # using a list instead of set

for student_id, details in student_data.items():

    unique_key = (details["name"], details["class"], details["subject_integration"])
    print(unique_key)
    if unique_key not in seen_keys:

        seen_keys.append(unique_key)

        result[student_id] = details

# print output line by line

for k, v in result.items():

    print(k, ":", v)