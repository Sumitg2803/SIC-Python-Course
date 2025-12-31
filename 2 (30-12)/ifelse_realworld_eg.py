# #1. check the username and password are correct to allow access
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" or username == "user" and password == "password123":
#     print("Access granted.")
# else:
#     print("Access denied.")

# #2. Display a action base on traffic light color
# traffic_light = input("Enter the traffic light color (red/yellow/green): ").lower()
# if traffic_light == "red":
#     print("Stop")
# elif traffic_light == "yellow":
#     print("Get Ready")
# elif traffic_light == "green":
#     print("Go")
# else:
#     print("Invalid color")


# #3. write a code for ATM cash withdrawal. Amount should be multiple of 100
# Balance = 5000
# withdraw_amount = int(input("Enter the amount to withdraw: "))
# if withdraw_amount <= Balance:
#     if withdraw_amount % 100 == 0:
#         Balance = Balance - withdraw_amount
#         print(f"Please collect your cash. Remaining balance is: {Balance}")
#     else:
#         print("Please enter the amount in multiples of 100.")
# else:
#     print("Insufficient balance.")


# #4. only age above 18 and having voting card are allowed to vote. (write code without nested if and without inbuilt functions AND, OR)
# age = int(input("Enter age: "))
# card = input("Do you have a voting card? (yes/no): ")

# eligible = 1   # assume eligible first

# if age < 18:
#     eligible = 0

# if card != "yes":
#     eligible = 0

# if eligible == 1:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# #5. only age above 18 and having voting card are allowed to vote. (write code using nested if and without inbuilt functions AND, OR)
# age = int(input("Enter age: "))
# if age >= 18:
#     card = input("Do you have a voting card? (yes/no): ")
#     if card == "yes":
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote.")
# else:   
#     print("Ghar ja aur pad le😂.")

# #6. apply discount based on total bill amount. if bill>10000 -> 20% discount, if bill>5000 -> 10% discount, if bill>1000 -> no discount
# bill = float(input("Enter the total bill amount: "))
# if bill > 10000:
#     discount = 20
# elif bill > 5000:
#     discount = 10
# else:
#     discount = 0
#     print("Intne chota bill leke aaya hai, koi discount nahi milega😂.")

# print(f"Your discount is {discount}%")
# final_amount = bill - (bill * discount / 100)
# print(f"Final amount to be paid: {final_amount}")
# print("Thank you for shopping with us! Visit again.")

#7. check whether a person is eligible for blood donation. Criteria: age between 18-65 and weight above 50kg
age = int(input("Enter your age: "))
if 18 <= age <= 65:
    weight = float(input("Enter your weight in kg: "))
    if weight > 50:
        print("You are eligible for blood donation.")
    else:
        print("You are not eligible for blood donation due to insufficient weight.")
else:
    print("Tu abhi andey mein hai, blood donation ke baare mein sochna band kar de.😂😂")

#