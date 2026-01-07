'''
**What is constructor?
    *Constructor is a special method that is called when object is created
    *Constructor is used to initialize object
    *Constructor is called automatically
    *Constructor is called only once
    *Constructor is called before object is created
    *Constructor is called after object is created
    *Constructor name is always __init__
'''

#example
class Parent():
    def __init__(self):
        print("Parent constructor")
    def display(self):
        print("Parent display method")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

c= Child()