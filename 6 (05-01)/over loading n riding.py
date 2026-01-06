#overloading 

class test:
    def show(self, a):
        print(a)

    def show(self, a, b):
        print(a,b)

t= test()
t.show(10,20) #valid - always the nearest function from the class
# t.show(10) #error - thus python does not support overloading

#overriding method
'''
**What is method overriding?
    *Overriding is a feature of OOPs where child class can override the method of the parent class
    *Child class can override the method of the parent class
    *To change the behaviour of parent class method in child class
    *To achieve runtime polymorphism
    *To provide specific implementation of method in child class

**Basic rule of method overriding
    *1. Method name should be same
    *2. Parameters should be same
    *3. Inheritance should be there
    *4. Child method has the priority
    *5. Method signature should be same
    *6. Method body should be different
'''
class test:
    def show(self, a):
        print(a)

class child(test):
    def show(self, a, b):
        print(a,b)

ob=child()
ob.show(10,20)