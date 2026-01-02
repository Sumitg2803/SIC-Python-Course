'''
what is function?
function is a block of code which is used to perform a specific task.
function is used to make the code reusable.
function is used to make the code readable.
function is used to make the code maintainable.
function is used to make the code testable.
a function help reduce code repetition.
improve readability of the code.
easy debuging and testing
make the code reusable.
make the code maintainable.
make the code testable.
save time n effort.

types of functions
1. built-in functions-
print, sum, length, etc.
2. user-defined functions-
created by the user
'''

#function without arguments
def abc():
    print("Hello")
    print("Welcome to Python")
    
abc()

def add1():
    a = 10
    b = 20
    print(a + b)
    
add1()

#function with arguments
def add2(a,b):
    print(a + b)
    
add2(10,20)

#finding factorial of 5 using function
def fact(n):
    f = 1
    for i in range(1,n+1):
        f= f*i
    return f

print(fact(5))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  

#default parameter
def greet(name = "user"):
    print("hello {}".format(name))
    
greet() #by default user
greet("sumit")  #the arguement which is passed will override the default value

#reverse a string using function
def rev_str(str1):
    return str1[::-1]

print(rev_str("hello"))

#reverse a list using function
def rev_list(list1):
    return list1[::-1]

print(rev_list([1,2,3,4,5,6,7,8,9,0]))

#reverse a string using function without slicing
def rev_str1(str2):
    rev = ""
    for i in str2:
        rev = i +rev
    return rev

print(rev_str1("hello"))

#reverse a list using function without slicing
def rev_list1(list2):
    rev = []
    for i in list2:
        rev = [i] + rev
    return rev

print(rev_list1([1,2,3,4,5,6,7,8,9,0]))

#by using functions find odd even numbers
def odd_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "odd"

a = int(input("Enter a number:"))
print(odd_even(a))

#palindrome using function
def palin(str3):
    pal = ""
    for i in str3:
        pal = i + pal
    if str3 ==pal:
        print("{} is a plaindrome".format(str3))
    else:
        print("{} is not a plaindrome".format(str3))

b = input(str("Enter a string:"))
palin(b)


#build a calculator using functions
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "cannot divide by 0"
    else:
        return x/y

x= int(input("Enter a number1: "))
y= int(input("Enter a number2: "))
operator = input("Enter an operator (+, -, *, /):")
if operator == "+":
    print(add(x,y))
elif operator == "-":
    print(sub(x,y))
elif operator == "*":
    print(mul(x,y))
elif operator == "/":
    print(div(x,y))
else:
    print("Invalid operator")


#prime number using function
def prime(num):
    if num == 1:
        print("{} is not a prime number".format(num))
    for i in range (2,num):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            return False
    print("{} is a prime number".format(num)) 

p= int(input("Enter a number:"))
prime(p)

#find largest amongs three numbers
def largest(a,b,c):
    return max(a,b,c)

e = int(input("Enter a number1: "))
f = int(input("Enter a number2: "))
g = int(input("Enter a number3: "))
print("The largest number is", largest(e,f,g))

#find smallest amongs three numbers
def smallest(a,b,c):
    return min(a,b,c)

h = int(input("Enter a number1: "))
i = int(input("Enter a number2: "))
j = int(input("Enter a number3: "))
print("The smallest number is", smallest(h,i,j))

#sum of all numbers
def sum_all(*numbersq):
    return sum(numbersq)

print(sum_all(1,2,3,4,5,6,7,8,9))

'''
What is **kwargs keyword arguments?
**kwargs is used to pass key-value pairs to a function.

what is *args?
*args is used to pass single value to a function.
It is use when yoou have to assign multiple values to one parameter.

what is global variable?
global variable is a variable which is accessible from any where in the program.

what is local variable?
local variable is a variable which is accessible only inside the function.
'''

#kwargs for variable number of keyword arguments
def show_info(**info):
    for key, value in info.items():
        print(key,value)

show_info(name="sumit", age=21, city="indore")


#local variable
def myfunction():
    x = 10
    print(x)

myfunction()
'''              
print(x) #error! is define inside "myfunction" so it is not accessible outside

'''

a=10
def myfunc():
    global a
    b=10+a
    print(b)

myfunc()
print(a)
'''
print(b) #error! is define inside "myfunc" so it is not accessible outside
'''

#atm withdrawl using function
balance = 10000

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawal successfull. \nRemaining blanance is {} \nTHANK YOU for banking with us".format(balance))
    else:
        print("Insufficient balance. \nSaala Gareeb.")

cash = int(input("Enter the amount to withdraw: "))
withdraw(cash)

'''
What is pass statement?
pass statement is used as a placeholder for future code.
It is used when a statement is required syntactically but you do not want any code to be executed.
'''
#using pass example
def myfunct():
    pass
          #placeholder for future implementation

for i in range(100):
    if i%20==0:
        print(i)
    else:
        pass

myfunct()

#counting the number of vowels in a string using function
def vol():
    str7= input("Enter a string:")
    count = 0
    for i in str7:
        if i in "aeiouAEIOU":
            count = count +1
    return count

print("Number of vowels in the string is {}".format(vol()))