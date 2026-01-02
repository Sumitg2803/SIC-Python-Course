'''
What is Filter function?
The filter() function in Python is used to filter elements from an iterable (like a list, tuple, etc.) based on a specified condition. It takes two arguments: a function and an iterable. The function is applied to each element of the iterable, and only those elements for which the function returns True are included in the result.
Filter function select elements based on iterable condition.

Filter Syntax:
    filter(function, iterable)
'''
# Example of using filter() function
marks = [30,40,60,70,67,66]
def failingstd(score):
    return score <60
failing_students = filter(failingstd, marks)
print("Failing students marks are:", list(failing_students))

#marks greater than 50
marks1 = [30,40,60,70,67,66]
result1= list(filter(lambda x: x>50, marks1))
print("Marks greater than 50 are:", result1)



