# example of set methods
print("-----practical examples of set-----")


#1. Find absent students from the class
total = set(["Rohit", "Shubham", "Pooja", "Anjali"])
present = set(["Rohit", "Pooja"])
absent = total.difference(present)
print("Absent students are:", absent)

#2. Find mutual friends
friend1 = set(["Amit", "Suresh", "Ramesh", "Rajesh"])
friend2 = set(["Suresh", "Ramesh", "Vikram", "Ajay"])
mutual_friends = friend1.intersection(friend2)
print("Mutual friends are:", mutual_friends)

#3. Ensure usernames are unique
usernames = set(["alice", "bob", "charlie"])
newusername = "david"

if newusername in usernames:
    print(f"Username '{newusername}' is already taken.")
else:
    usernames.add(newusername)
    print(f"Username '{newusername}' has been added.")
print("Current usernames:", usernames)

#4. swap two numbers using set
a = 5
b = 10
a, b = b, a
print("After swapping: a =", a, "b =", b)

#5. Remove Duplicate word from a sentence
sentence = "python is easy and python is powerfull"
words = sentence.split()
unique_words = set(words)
print("Unique words are:", unique_words)

