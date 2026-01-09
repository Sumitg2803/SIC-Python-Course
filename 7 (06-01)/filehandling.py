'''
**What is File handling?
    *File handling is a process of reading and writing data to a file.

**Why use file handling?
    *To store data
    *To read data
    *To update data
    *To delete data

Python provides inbuilt functions to handle file operations.

**What is 'with' keyword?
    *'with' keyword is used to handle file operations.
    *It is used to open and close file automatically.
    *It is used to handle file operations in a safe way.

**Notation -
    r - read
    w - write
    a - append
    r+ - read and write
    w+ - write and read
    a+ - append and read

'''
#read file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#write file
with open("example.txt", "w") as file:
    file.write("\nHello World! Welcome to Python \nlorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.")

#append file
with open("example.txt", "a") as file:
    file.write("! Welcome to Python")

#File existence & deletion
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("File does not exist")

#example: count words in a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    words = content.split()
    print("Total words: ", len(words))

#example: count lines in a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    lines = content.split("\n")
    print("Total lines: ", len(lines))

#example: count characters in a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    characters = content.split(" ")
    print("Total characters: ", len(characters))

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    print("Total characters:", len(content))
    
with open("example.txt", "r") as file:
    content = file.read()
    char_count = len(content.replace(" ", "").replace("\n", ""))
    print("Characters (no spaces, no newlines):", char_count)