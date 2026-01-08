'''
**What is excepton handling?
    *It is a process of handling errors in a program.

**Blocks
    *there are 5 blocks in exception handling-
    *try - it is used to enclose the code that may raise an exception
    *except - it is used to handle the exception
    *else - it is used to execute the code if no exception is raised
    *finally - it is used to execute the code finally
    *raise - it is used to raise an exception

**There are 2 optional blocks in exception handling-
    *else
    *finally

**Types of exceptions-
    *Built-in exceptions
    *User-defined exceptions

**Built-in exceptions-
    1.) ArithmeticError - wrong math operation
    2.) AssertionError - assert statement failed
    3.) AttributeError - attribute not found
    4.) EOFError - end of file
    5.) FloatingPointError - floating point operation failed
    6.) GeneratorExit - generator exit
    7.) ImportError - import failed
    8.) IndexError - index out of range
    9.) KeyError - key not found
    10.) KeyboardInterrupt - keyboard interrupt
    11.) MemoryError - memory error
    12.) NameError - name not found
    13.) None
    14.) NotImplementedError - not implemented
    15.) OSError - os error
    16.) OverflowError - overflow error
    17.) ReferenceError - reference error
    18.) RuntimeError - runtime error
    19.) StopAsyncIteration - stop async iteration
    20.) StopIteration - stop iteration
    21.) SyntaxError - syntax error
    22.) SystemExit - system exit
    23.) TabError - tab error
    24.) TimeoutError - timeout error
    25.) TypeError - type error
    26.) UnboundLocalError - unbound local error
    27.) UnicodeError - unicode error
    28.) UnicodeEncodeError - unicode encode error
    29.) UnicodeDecodeError - unicode decode error
    30.) UnicodeTranslateError - unicode translate error
    31.) ValueError - invalid value
    32.) ZeroDivisionError - division by zero
'''

'''
**What is exception?
    *Exception is an error that happens while the program is running.
    *If we dont handel it the program will stop running.

**What is exception handling?
    *Exception handling allow to detect error and handel them properly and prevents the program from crashing.

**Why use exception handling?
    *To detect error
    *To handel error
    *To prevent program from crashing
    *To make program more robust
'''

#example
a=10
b=25
try:
    x=a/b
    print(x)
except ZeroDivisionError:
    print("something went wrong")
    print("Cannot divide by zero")    
else:
    print("No error")
finally:
    print("Execution completed")

#handling value-error
try:
    x= int(input("Enter a number: "))
except ValueError as e:
    print(e)
    print("Can't use string as a number")
else:
    print("No error")
finally:
    print("Execution completed")

#handling multiple errors
try:
    x= int(input("Enter a number: "))
    result = 10/x
    print(result)
except ValueError as e:
    print("Value error: {}".format(e))
except ZeroDivisionError as er:
    print("Cannot divide by zero: {}".format(er))
else:
    print("No error")
finally:
    print("Execution completed")

#handling index error
try:
    x=[1,2,3,4,5]
    print(x[10])
except IndexError as e:
    print("Something went wrong")
    print("Index error: {}".format(e))
else:
    print("No error")
finally:
    print("Execution completed")

#handling key error
try:
    dict1= {"name":"Sumit", "age":21, "gender":"Male"}
    print(dict1["name"])
    print(dict1["height"])
except KeyError as e:
    print("Something went wrong")
    print("Key error: {}".format(e))
else:
    print("No error")
finally:
    print("Execution completed")

#handling type error
try:
    x= 10
    y= "20"
    print(x+y)
except TypeError as e:
    print("Something went wrong")
    print("Type error: {}".format(e))
else:
    print("No error")
finally:
    print("Execution completed")