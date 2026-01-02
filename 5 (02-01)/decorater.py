'''
**What is Decorator function?
    *A decorator in Python is a special type of function that modifies the behavior of another function. Decorators allow you to wrap another function in order to extend its behavior without modifying its code directly. They are often used for logging, access control, instrumentation, and caching.
    *It is denoted by the "@" symbol above the function definition.
    *Decorator says you cannot change the original function, but you can wrap another function around it to modify its behavior. That means you cannnot change the source code of the original function, instead adding extra in original function you can create another function (wrapper) that adds the extra functionality and call the original function inside the wrapper function.
    
    Decorator is design factor in python that allow you to add new functionalty to existing function or method without modifying.
    Avoid code duplication
    1. decorator are possible in python because function are first class object.
    2. function can be pass as a arguement
    3. function can be written from another function
    4. nested function are allowed

**What is wrapper here?
    *A wrapper is a function defined inside a decorator that adds some functionality to the original function. The wrapper function typically takes the same arguments as the original function and calls it within its body, adding extra behavior before or after the call.
    *Wrap means to cover something. In programming, a wrapper function "covers" another function to add extra features without changing the original function's code.

Decorator Syntax:
    @decorator_function
    def function_to_be_decorated():
        # function body
'''

# Example of using decorator function
def first_decorator(say_hello):
    def wrapper():
        print("Before calling hello")
        say_hello()
        print("After calling hello")
    return wrapper
def second_decorator(say_hello):
    def wrapper():
        print("Before calling hello")
        say_hello()
        print("After calling hello")
    return wrapper

#covert lower to upper case
def convert_to_uppercase(func):
    def wrapper():
        result = func()
        modified = result.upper()
        return modified
    return wrapper

@convert_to_uppercase
def greet():
    return "ole ole.. hello helo.. ole ole" 
print(greet())

#covert to lower case
def convert_to_lowercase(func):
    def wrapper():
        result = func()
        modified = result.lower()
        return modified
    return wrapper

@convert_to_lowercase
def greet():
    return "OLE OLE.. HELLO HELO.. OLE OLE" 
print(greet())

#addition of two numbers using decorator
def decorator_add(func):
    def wrapper(a,b):
        print("Adding", a, "and", b)
        return func(a,b)
    return wrapper

def add(a,b):
    return a+b

add = decorator_add(add)
print(add(10,20))

#check athentication before showing Dashboard
def login_required(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            print("Access denied. Chal nikal. Aya gareeb")
            return None
        return func(user)
    return wrapper

@login_required
def dashboard(user):
    print("Welcome {} to Dashboard".format(user.get("name")))

#test case
user1 ={"name": "sumit", "is_logged_in": True}
user2 ={"name": "guest", "is_logged_in": False}
dashboard(user1)
dashboard(user2)