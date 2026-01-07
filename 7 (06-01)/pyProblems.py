#password strength checker
password = input("Enter your password: ")
if len(password)>= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
    print("Its is a strong password")
elif first char is not uppercase:
    print("First char should be uppercase")
elif not any(char.isdigit() for char in password):
    print("Password should contain at least one digit")
elif not any(char.islower() for char in password):
    print("Password should contain at least one lowercase letter")
elif not any(char.isupper() for char in password):
    print("Password should contain at least one uppercase letter")
else:
    print("Its not a strong password. Kya admin banega re tu?")

#Contact search in Phonebook
contacts = {
    "Sumit": "9856231478",
    "Prathmesh": "1234567890",
    "Rahul": "1234596490",
    "Sonal": "1278167890",
    "Pratik": "1234965190",
    "Kumari": "1278901234"
}
name = input("Enter the name to search: ")
if name in contacts:
    print(contacts[name])
else:
    print("Name not found")

**fiizbuz

def fizzBuzz(n):
    result = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result   
print(fizzBuzz(15))