#Set is collection which is unordered, unindexed. No duplicate members.
#Characteristics of set:
#1. Unordered
#2. Unindexed
#3. No Duplicates
#4. Mutable
#5. Heterogeneous - can store different data types
#searching is faster in set as compared to list and tuple
# s = {1,2,3,4,5}

#empty set
s = set()
z= ([5,6,7,8])
print(f"s is {type(s)}")
print(f"z is {type(z)}")

a = set([1,2,3,4,5,5,5])
print(a)
print(type(a))

a.add(6)
a.add(7)
print(a)


#remove
a.remove(3)
print(a)

a.update([8,9,10,11])
print(a)

print(a.pop())
print(a)

#discard
a.discard(4)
print(a)
a.discard(15) #does not raise error if item not found
print(a)

#uninon
b = {11,12,13,14,15}
c = a.union(b)
print(c)

#intersection
d = a.intersection(b)
print(d)


