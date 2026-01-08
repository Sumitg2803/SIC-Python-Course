#convert list of strings to list of integers using map
list1 = ["1", "2", "3", "4", "5"]
r = map(int, list1)
print(list(r))

#convert list of integers to list of strings using map
list2 = [1,2,3,4,5]
r1 = map(str, list2)
print(list(r1))

#using lambda function
list3 = [1,2,3,4,5]
r2 = map(lambda x: x*2, list3)
print(list(r2))

#string reverse using lambda
str3 = "helloo"
r3 =(lambda s: s[::-1]) (str3)
print(r3)

#shallow copy
import copy
original = [[1,2,3], [4,5,6]]
shallow = copy.copy(original)

shallow[0][0]=99
print(original)
print(shallow)

#deep copy
import copy
original = [[1,2,3], [4,5,6]]
deep = copy.deepcopy(original)
deep[0][0]= 99
print(original)
print(deep)