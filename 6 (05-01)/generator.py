'''
**what is generator?
    *Generator is a function that returns an iterator.
    *Generator function uses yield keyword.
    *It is a special type of function that allows you to generate value once at a time instead of returning all values at once.
    *Instead return we use yield keyword.
    *They are memory efficient.
    *Don't store all values in memory at once. Generate value on demand.

**Why use Generator?
    *Save memory - useful for large datasets.
    *Faster execution for streaming data.
    *Easy to implement iterator protocol.

**What does yield keyword do?
    *Yield keyword is used to return a value from a generator function.
    *Yield keyword is used to pause the execution of a generator function.
    *Yield keyword is used to resume the execution of a generator function. 
    *Yield keyword is used to generate a value on demand.
    *Yield keyword is used to generate a value once at a time instead of returning all values at once.
'''
#generator example
def generator_example():
    for i in range(1,4):
        yield i
    
gen = generator_example()
print(next(gen))
print(next(gen))
print(next(gen))

#addition of two number by using generator
def add(x,y):
    return x+y

def generator_addition():
    yield add(10,20)
    yield add(30,40)
    yield add(50,60)
    
abc = generator_addition()
print(next(abc))
print(next(abc))
print(next(abc))
    
# finding cube using generator
def generator_cube(n):
    for i in range(n):
        yield i**3


cube = generator_cube(10)
print(next(cube)) #cube of 1
print(next(cube)) #cube of 2
print(next(cube)) #cube of 3
print(next(cube)) #cube of 4
print(next(cube)) #cube of 5
print(next(cube)) #cube of 6
print(next(cube)) #cube of 7
print(next(cube)) #cube of 8
print(next(cube)) #cube of 9
print(next(cube)) #cube of 10
