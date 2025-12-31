# This is a tuple containing different data types
#*****important*****#
a = ("ABC", 1, 2, 3.5, True)
print(a)

#tuple is a collection data type which is ordered and unchangeable. Allows duplicate members.
#characteristics of tuple:
#1. Ordered
#2. Unchangeable
#3. Allow Duplicates
#4. Store different data types
#5. Immutable
#6. heterogeneous - can store different data types

#empty tuple
b = ()
print (f"b is {type(b)}")

#nested tuple
c = (1,2, ("A", "B", "C"), 3.5)
print(c)

#implicit type casting [tuple -> list]
a = (1,2,3)
b = list(a)
print(b)
print (type(b))

print("\n")

print ("-----practical examples of tuple-----")
#create an empty tuple
empty_tuple = ()

print("\n")

# access value using indexing
my_tuple1 = (10, 20, 30, 40, 50)
print(my_tuple1[2]) 

print("\n")

#check existance of an item in a python tuple using if else
my_tuple2 = (10, 20, 30, 40, 50)
if 30 in my_tuple2:
    print("30 is present in the tuple") 
else:
    print("30 is not present in the tuple")
    
print("\n")

#fetch the spicific element using indexing
my_tuple3 = (10, 20, 30, 40, 50)
print(my_tuple3[1])

print("\n")

#negative indexing in tuple
my_tuple4 = (10, 20, 30, 40, 50)
print(my_tuple4[-2])

print("\n")

#slicing in tuple
my_tuple5 = (10, 20, 30, 40, 50)
print(my_tuple5[1:4])

print("\n")

#can we update tuple value?
#no, we cannot update tuple value as tuple is immutable
my_tuple6 = (10, 20, 30, 40, 50)