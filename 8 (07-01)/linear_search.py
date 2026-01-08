'''
**What is linear search?
    *Linear search is a simple search algorithm that is used to find the position of a target value within a list or array. It works by iterating through the list from the beginning to the end, comparing each element with the target value, and returning the index of the first occurrence of the target value.

**How does linear search work?
    *Linear search works by iterating through the list from the beginning to the end, comparing each element with the target value, and returning the index of the first occurrence of the target value.

**What are the advantages of linear search?
    *Linear search is a simple search algorithm that is used to find the position of a target value within a list or array. It works by iterating through the list from the beginning to the end, comparing each element with the target value, and returning the index of the first occurrence of the target value.

**What are the disadvantages of linear search?
    *Linear search is a simple search algorithm that is used to find the position of a target value within a list or array. It works by iterating through the list from the beginning to the end, comparing each element with the target value, and returning the index of the first occurrence of the target value.

'''
#example
arr =[5,8,2,9,1]
target = 9
for i in arr:
    if i == target:
        print("Element found at index", arr.index(i))
        break
    else:
        print("Element not found")

#linear serach using function
arr =[5, 8, 2, 9, 1]
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)
        else:
            return "Element not found"

print(linear_search(arr, 1))

#linear search using dictionary
dict1 = {"a": 1, "b": 2, "c": 3}
target =3
for i in dict1:
    if dict1[i] == target:
        print("Element found at index ", dict1[i])
        break
    else:
        print("Element not found")

#linear search using dictionary finding both key n value
dict2 = {"a": 1, "b": 2, "c": 3}
target = 2
for key in dict2:
    if dict2[key] == target:
        print("Element found, its key and value are {}: {}".format(key, dict2[key]))
        break
else:
    print("Element not found")


#linear search finding index of element in list
arr =[5,8,2,9,1]
target = 9
for i in arr:
    if i == target:
        print("Element found at index", arr.index(i))
        break
    else:
        print("Element not found")