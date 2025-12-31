#*****important *****#

grades = [85, 90, 78, 92, 88]
print(f"Original grades: {grades}")
average_grade = sum(grades) / len(grades)
print(f"The average grade is: {average_grade}")

attendence = ["p", "p", "a", "p", "p", "a", "p"]
present_days = attendence.count("p")
print(f"Number of present days: {present_days}")

for i in range(len(grades) // 2):
    j = len(grades) - 1 - i
    grades[i], grades[j] = grades[j], grades[i]
print(f"Reversed grades: {grades}")

#reverse a string without using inbuilt function
s = "hello" 
result = ""
for i in range (len (s)-1, -1, -1):
    result += s[i]
print(f"Reversed string: {result}")
    
    