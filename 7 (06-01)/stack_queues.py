'''
**What is array?
    *Array is a collection of similar data type
    
**What is Stack?
    *Stack is a LIFO (Last In First Out) data structure

**What is queue?
    *Queue is a FIFO (First In First Out) data structure
    
'''
#stack example
class stack:
    def __init__(self):
        self.value=[]
    def push(self,x):
        self.value=[x]+self.value
    def pop(self):
        return self.value.pop(0)
    def peek(self):
        return self.value[0]
    def is_empty(self):
        return len(self.value)==0
    def size(self):
        return len(self.value)

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())

#check for palindrome using stack
class stack:
    def __init__(self):
        self.value=[]
    def push(self,x):
        self.value=[x]+self.value
    def pop(self):
        return self.value.pop(0)
    def peek(self):
        return self.value[0]
    def is_empty(self):
        return len(self.value)==0
    def size(self):
        return len(self.value)

def is_palindrome(s):
    st=stack()
    for i in s:
        st.push(i)
        print("Charater entered: {}".format(st.value))
    for i in s:
        if i!=st.pop():
            print("Charater poped: {}".format(st.value))
            return False
    return True

print(is_palindrome(input("Enter a string: ")))

#queue example
class queue:
    def __init__(self):
        self.value=[]
    def enqueue(self,x):
        self.value=self.value+[x]
    def dequeue(self):
        return self.value.pop(0)
    def peek(self):
        return self.value[0]
    def is_empty(self):
        return len(self.value)==0
    def size(self):
        return len(self.value)

q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.dequeue())
print(q.peek())
print(q.is_empty())
print(q.size())

#queue
class queue:
    def __init__(self):
        self.value=[]
    def en(self,x):
        self.value.append(x)
    def deque(self):
        front=self.value[0]
        self.value=self.value[1:]
        return front
    def peek(self):
        return self.value[0]
    def is_empty(self):
        return len(self.value)==0
    def size(self):
        return len(self.value)
q1=queue()
q1.en(10)
q1.en(20)
q1.en(30)
q1.en(40)
q1.en(50)
print(q1.deque())
print(q1.peek())
print(q1.is_empty())
print(q1.size())