'''
OOPs is a programming approach where we organize code using class and object just like real world entity.

class example - car
object example - audi, bmw, mercedes

**Advantages of OOPs
    1. Write clean and structure code
    2. Reuse code, no repition
    3. Make code easy to understand
    4. Make code easy to maintain

**Key concept of OOPs
    1. class - blueprint of object
    2. object - instance of class
    3. constructor - (initialize object) special method that is called when object is created
    4. encapsulation - (data hiding) bundling data and function together
    5. inheritance - Reusing code
    6. polymorphism - many forms
    7. abstraction - hiding complex internal implementation details
'''

###################################################################################################################
#inheritance (Single level)
class father():
    def king(self):
        print("I am king of my family")
    def dy(self):
        print("DY Patil college")
class son(father):
    def ni(self):
        print("Hi i am son")

d=son()
d.ni()
d.king()

#multilevel inheritance
class GrandFather():
    def abc(self):
        print("I am god father")
class Father(GrandFather):
    def xyz(self):
        print("I am Father")
class son(Father):
    def rst(self):
        print("I am Son")

f=son()
f.abc()
f.xyz()
f.rst()

#multiple inheritence
'''
multiple inheritance is a type of inheritance where child class inherit property from more than one parent class
'''
class father():
    def skills(self):
        print("Father paisa")
class mother():
    def skills(self):
        print("Mother ka paisa")
class bro():
    def bhai(self):
        print("-")
class child(father):
    def abc(self):
        print("Child ka paisa nhi hai")

ob=child()
ob.abc()
ob.skills()



#hierarchy inheritance
'''
Hierarchy inheritance is a type of inheritance where one class is inherited by more than one class.
'''
class father():
    def abc(self):
        print("I am father")
class son1(father):
    def xyz(self):
        print("I am rahul")
class son2(father):
    def pqr(self):
        print("I am prathmesh")
class son3(father):
    def mno(self):
        print("I am sonal")

ob=son1()
ob.xyz()
ob.abc()

ob2=son2()
ob2.pqr()
ob2.abc()      

ob3=son3()
ob3.mno()
ob3.abc()

#hybrid inheritance
'''
hybrid inheritance means combination of different inheritance like single level, multilevel or multiple inheritance
'''
class A():
    def a(self):
        print("I am A")
class B(A): #single level
    def b(self):
        print("I am B")
class D():
    def d(self):
        print("I am D")
class C(D,B): #multiple
    def c(self):
        print("I am C")

obj=C()
obj.a()
obj.b()
obj.c()
obj.d()

obj2=B()
obj2.b()
obj2.a()

obj3=A()
obj3.a()

obj4=D()
obj4.d()

#polymorphism 
'''
polymorphism means one to many
'''
def animal_sound(animal):
    animal.make_sound()
class Dog:
    def make_sound(self):
        print("Bark")

class Cat:
    def make_sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)


#example
class Bank():
    def interest(self):
        print("Bank interest is 4%")
class SBI(Bank):
    def interest(self):
        print("SBI bank interest is 6%")
class HDFC(Bank):
    def interest(self):
        print("HDFC bank interest is 7%")

b=SBI()
b.interest()

h=HDFC()
h.interest()

ob=Bank()
ob.interest()

#example
class parent():
    def __init__(self):
        print("Parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

ob=child()