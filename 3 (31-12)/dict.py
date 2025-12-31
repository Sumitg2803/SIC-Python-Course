# Dictionary operations in Python
#Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#characteristics of dictionary
#1. Ordered: As of Python 3.7, dictionaries maintain the insertion order of items. But in earlier versions, they are unordered.
#2. Changeable: Dictionaries are mutable, meaning you can change their content without changing their
#3. Indexed: Dictionaries are indexed by keys, which can be of any immutable type (like strings, numbers, or tuples).
#4. No duplicate members: Dictionaries cannot have two items with the same key. If you try to assign a value to an existing key, the old value will be overwritten.

#why dict is imp in industry
#1. Fast Lookups: Dictionaries provide average O(1) time complexity for lookups, making them ideal for scenarios where quick access to data is crucial.
#2. Flexible Data Structures: They allow for the creation of complex data structures, such as nested dictionaries, which can represent real-world entities more effectively.
#3. Data Integrity: By using unique keys, dictionaries help maintain data integrity and prevent duplication
#4. Easy to Use: The syntax for dictionaries is straightforward, making them easy to implement and understand, which is beneficial for rapid development.
#5. API responses: Many web APIs return data in JSON format, which maps directly to Python dictionaries, making it easy to work with API responses.

# #empty dict
# empty_dict = {}
# print(empty_dict)   

# #accessing items
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(my_dict["name"])  # Accessing value by key
# print(my_dict.get("age"))  # Accessing value using get() method

# #adding items
# my_dict["email"] = "alice@hotmail.com"
# print(my_dict)

# #updating items
# my_dict["age"] = 31
# print(my_dict)

# #deleting items means removing key-value pairs
# #pop method means removes the item with the specified key name

# #deleteing without pop method
# del my_dict["city"]
# print(my_dict)

# #deleting with pop method
# removed_value = my_dict.pop("email")
# print(removed_value)

# #fetching key values pairs
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

# #merge two dict
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict1.update(dict2)
# print(dict1)

# #merge two dict with update operator
# dict3 = {"x": 10, "y": 20}
# dict4 = {"y": 30, "z": 40}
# merged_dict = dict3 | dict4
# print(merged_dict)

# #nested dict
# dict5 = {
#     "person1": {
#         "name": "john",
#         "age": 25
#     },
#     "person2": {
#         "name": "Jane",
#         "age": 28
#     },
#     "person3": {
#         "name": "Doe",
#         "age": 22
#     },
#     "person4": {
#         "name": "Smith",
#         "age": 35
#     },
#     "person5": {
#         "name": "Emily",
#         "age": 27
#     }
# }

# print(dict5["person3"]["name"])  # Accessing nested dictionary value
# print(dict5["person4"]["age"])   # Accessing nested dictionary value
# print(dict5)  # Print the entire nested dictionary

# #use get method to access value without key error
# print(dict5.get("person6", "Not Found"))  # Accessing non-existing key with default value


# #verify username and password using dict
# credentials = {
#     "admin": "password123",
#     "user": "userpass",
#     "guest": "guestpass"
# }
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if credentials.get(username) == password:
#     print("Access granted.")
# else:
#     print("Access denied.")
    
# # employee salary increment by 10%
# salaries = {
#     "Alice": 50000,
#     "Bob": 60000,
#     "Charlie": 55000
# }
# for employee in salaries:
#     new_salary = salaries[employee] * 0.10  # Increment salary by 10%
#     print("Incremented salaries:{employee}: {new_salary}".format(employee=employee, new_salary=new_salary))
#     salaries[employee] = salaries[employee] + new_salary
# print(salaries)

#inventory management
stock = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}
item = input("Enter the item to check stock: ").lower()
if item in stock:
    print(f"Stock for {item}: {stock[item]}")
else:
    print("Item not found in stock.")
    

