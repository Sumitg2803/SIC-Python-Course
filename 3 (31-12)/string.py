#String is immutable, means once a string is created, the elements within it cannot be changed or modified.
#1. Creating Strings: Strings can be created using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# single_quote_str = 'Hello, World!'
#String cannot be modified

#charactristics of string:
#1. Immutable
#2. Ordered
#3. Indexed
#4. Allows Duplicates
#5. Supports Various Methods
#6. Can be Multiline
#7. Supports Escape Characters
#8. Can be Concatenated and Repeated
#9. Supports Slicing and Indexing
#10. Unicode Support

#string slicing
my_string = "Hello, World!"
print (my_string [0:5])
print (my_string [:3])
print (my_string [3:])

#use startwith and endswith methods
text = "python programming"
print(text.startswith("py"))  # True
print(text.endswith("ing"))   # True

#isalpha and isdigit  isalnum methods
print ("abc".isalpha())  # True
print ("123".isdigit())  # True
print ("abc123".isalnum())  # True

#converting to string
num = 123
str_num = str(num)
print(str_num)  # '123'
print(type(str_num))  # <class 'str'>

#check for substring
sentence = "learning python is fun"
print("python" in sentence)
print("Java" not in sentence)

#replace
a = "hello world"
print(a.replace("world", "there"))
print(a.replace ('h', 'o'))
print (a)

#count 
a = "ppppython"
print(a.count("p"))  # 4

#string split
a = "hello,world,python"
print(a.split(","))  # ['hello', 'world', 'python']
