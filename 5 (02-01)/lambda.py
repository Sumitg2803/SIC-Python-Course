'''
What is lambda function?
A lambda function is a small anonymous function without a name.
It is mainly use for short logical functions.
It can have multiple argument but it return only one expression.

Why use lambda function?
1. It is use when you need a small function for a short period of time.
2. It is use to reduce code size.
3. It is use to improve code readability.
4. It is use to create higher order functions.

Benefits of lambda function over normal function
1. It is more concise and compact.
2. It is easier to read and understand.
3. It is more efficient in terms of performance.

syntax:
    lambda arguments: expression
'''

#square of a number using lambda function
square = lambda x: x*x
print(square(5))

#lambda function V/S normal function
def add(a,b): #normal function
    return a+b
print(add(3,4))

add_lambda = lambda a,b: a+b #lambda function
print(add_lambda(3,4))

#pass multiple value return in lambda function
cal=lambda x,y:(x+y, x-y, x*y, x/y)
q,r,s,t=cal(10,5)
print("Addition:",q)
print("Subtraction:",r)
print("Multiplication:",s)
print("Division:",t)

#default keyword argument in lambda function
de_lam= lambda x, y=2: x+y
print (de_lam(5))
print (de_lam(5,3)) #overriding default value of y