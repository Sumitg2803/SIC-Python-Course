a = [1,2,3,4,5.5,6,7, "DY", True]
a[0] = 100
print(a)

#list is collection data type use to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values.
#characteristics of list:
#1. Ordered
#2. Mutable
#3. Allow Duplicates
#4. Store different data types

a.pop()
print(a)

b = [1,2,3.4,4,5.6, "ABC", False]
b.remove(3.4)
print(b)


c = [1,2,3,4,5,6]
c.extend([7,8,9])
print(c)

d = [1,2,3,4,5]
d.insert(1, 70)
print(d)

