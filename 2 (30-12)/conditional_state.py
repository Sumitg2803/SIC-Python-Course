#conditional statements allows us to execute certain code based on certain conditions in python.
#conditinoal statements controls the flow of execution of the program.
#we have different types of conditional statements in python
#1. if statement
#2. if else statement
#3. if elif else statement
#4. nested if statement

age = 18
if age >= 18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible to vote.")
    

#example 
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
elif marks < 35:
    print("Fail")
else:
    print("Grade F")
    
#nested if example
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))

if num1 > num2:
    if num1 > num3:
        print("{} is the largest".format(num1))
    else:
        print("{} is the largest".format(num3))
else:
    if num2 > num3:
        print("{} is the largest".format(num2))
    else:
        print("{} is the largest".format(num3))
        
#print postive, negative numbers or zero using nested if
number = int(input("Enter a number: "))
if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
    
#check whether number is even or odd using nested if
num = int(input("Enter a number: "))
if num >= 0:
    print ("Positive number")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("Please enter a non-negative number.")

#using logical opeator
age = 20
if age <= 18 and age >= 10:
    print("You are young adult.")
else:
    print("You are not young adult.")
    
#at least one condition must be true
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's a weekend!")
else:
    print("It's not a weekday.")
    
