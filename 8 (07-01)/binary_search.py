'''
**What is binary search?
    *Binary search is a search algorithm that is used to find the position of a target value within a list or array. It works by repeatedly dividing the list into two halves and comparing the target value with the middle element of the list. If the target value is equal to the middle element, the algorithm returns the index of the middle element. If the target value is less than the middle element, the algorithm continues to search in the left half of the list. If the target value is greater than the middle element, the algorithm continues to search in the right half of the list.

**How does binary search work?
    *Binary search works by repeatedly dividing the list into two halves and comparing the target value with the middle element of the list. If the target value is equal to the middle element, the algorithm returns the index of the middle element. If the target value is less than the middle element, the algorithm continues to search in the left half of the list. If the target value is greater than the middle element, the algorithm continues to search in the right half of the list.

**What are the advantages of binary search?
    *Binary search is a search algorithm that is used to find the position of a target value within a list or array. It works by repeatedly dividing the list into two halves and comparing the target value with the middle element of the list. If the target value is equal to the middle element, the algorithm returns the index of the middle element. If the target value is less than the middle element, the algorithm continues to search in the left half of the list. If the target value is greater than the middle element, the algorithm continues to search in the right half of the list.

**What are the disadvantages of binary search?
    *Binary search is a search algorithm that is used to find the position of a target value within a list or array. It works by repeatedly dividing the list into two halves and comparing the target value with the middle element of the list. If the target value is equal to the middle element, the algorithm returns the index of the middle element. If the target value is less than the middle element, the algorithm continues to search in the left half of the list. If the target value is greater than the middle element, the algorithm continues to search in the right half of the list.

***important***
    *in binary search array should be sorted
'''

#example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high)//2
    if arr[mid] == target:
        print("Element found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")

#Binary search using function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    while low <=high:
        mid =(low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binary_search(arr, 9))