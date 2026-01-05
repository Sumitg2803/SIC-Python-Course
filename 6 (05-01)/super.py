'''
**What is super()?
    *Super is a buildin function in python that call method and constructor of parent class from inside child class
    *Super is used to call parent class method

**Why use super()?
    *Avoid duplication
    *To call paren constructor
    *Support multiple inheritance
    *To access overriden methods

**Advantages of super()
    *Code Reusability
    *Easy to maintain
    *Easy to update
    *Easy to debug
    *Easy to read
    *Easy to write
    *Easy to understand
    *Easy to implement
    *Easy to test
    *Easy to debug
'''

class parent():
    def display(self):
        print("This is parent")
class child(parent):
    def display(self):
        super().display()
        print("This is child")

ob=child()
ob.display()