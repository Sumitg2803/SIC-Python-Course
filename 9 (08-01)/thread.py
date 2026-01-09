'''
**What is Thread?
    *Thread is a sequence of instructions to be executed
    *It is a smallest unit of process
    *It is a light weight process
    *It is a part of process
    *It is a way to run multiple tasks
    *It is a way to run multiple threads
    *It is a way to run multiple processes

    *Thread is smallest unit of execution within a process
    *A process can have multiple threads
    *All thread share same memory same data
    *Each thread has its own execution path
    *Threading allows multiple task to run within a single program
    *Threading is used to perform multiple task at same time, using threading we can improve the performance of program

**Why do we need threading?
    *Improve application responses
    *Perform multiple task at same time.
    *Reduce the waiiting time
    *Perform background processing
    *Improve the performance of program

**Types of thread
    *Single thread
    *Multi thread

**Advantages of threading
    1.) Code Reusability
    2.) Easy to maintain
    3.) Easy to update
    4.) Easy to debug
    5.) Easy to read
    6.) Easy to write
    7.) Easy to understand
    8.) Easy to implement
    9.) Easy to test
    10.) Easy to debug
'''

import threading

#example
import time

def print_numbers():
    for i in range(1, 4):
        print("Number is {}" .format(i))
        time.sleep(1)

def print_letters():
    for letter in ['a', 'b', 'c']:
        print("Letter is {}" .format(letter))
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

'''
**What is join?
    *Join is a method that is used to wait for a thread to complete
    *Join is used to wait for a thread to complete before the main thread exits

*if join is not used then main thread will exit before the child thread.
*if join is used then main thread will wait for the child thread to complete before exiting.
*join is used to synchronize threads
'''

#example
def name():
    for ch  in ['a', 'b', 'c']:
        print(ch)

def number():
    for i in range(1, 4):
        print(i)

thread1 = threading.Thread(target=name)
thread2 = threading.Thread(target=number)

thread1.start()
thread2.start()

thread1.join()
thread2.join()