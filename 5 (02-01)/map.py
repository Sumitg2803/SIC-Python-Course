'''
what is Map function in Python?
The map function applies a fuction to each element in an iterable (like a list or tuple) and returns a map object (which is an iterator). It is commonly used for transforming data in a concise way.

Synatx:
    map(function, iterable)
'''

#example 1: square of all emlements in a list using map function
num =[1,2,3,4,5,6,7,8,9,]
sq= list(map(lambda x: x**2, num))
print(sq)

#now using normal function
def square(x):
    return x**2
sq_normal = list(map(square, num))
print(sq_normal)

#convert all string elements to upper case using map function
fruits = ["apple", "bannana", "cherry", "date"]
upper_fruits= list(map(lambda x: x.upper(), fruits))
print(upper_fruits)