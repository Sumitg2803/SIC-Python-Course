#for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
#and execute a block of code multiple times.

#you can itterate over each character in a string
my_string = "Hello"
for char in my_string:
    print(char)
    
#iterate through a list to modify each element
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2
print(my_list)

#interating through a list of numbers and printing their squares
numbers = [1,2,3,4,5]
for num in numbers:
    print(num**2)
    
#loop thorugh a list and check for a specific item.
friuts = ["apple", "banana", "cherry", "date"]
item_to_find = "cherry"

for fruit in friuts:
    if fruit == item_to_find:
        print(fruit, "item found!")
        break
else:
    print (f"{item_to_find} not found in the list.")
    
#ising break, cintue and pass statements in for loop
#1. break = exits the loop
#2. continue = skips the current iteration and moves to the next one
#3. pass = does nothing, used as a placeholder

#break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
for j in range(1, 100):
    if j == 25:
        pass
    print(j)

for k in range(1, 100):
    if k % 2 == 0:
        continue
    print(k)
    
#sum of using for loop
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

#flattening a list of lists
list1 = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = []
for sublist in list1:
    for item in sublist:
        flattened_list.append(item)
print (flattened_list)

#find the second higgest number in a list
numbers = [10, 20, 4, 45, 99, 99, 45]
print (numbers)
first = numbers[0]
second = numbers[0]
for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second highest number is:", second)

#find the third highest number in a list
numbers2 = [10, 20, 4, 45, 99, 99, 45]
print (numbers2)
first = numbers2[0]
second = numbers2[0]
third = numbers2[0]
for num in numbers2:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != second and num != first:
        third =num
print("Third highest number is:", third)
