# 4. Sequential execution: Write two functions, each printing a start message, sleeping for 2 seconds, and printing a completion message. Call them sequentially and measure the total time.

from threading import Thread
import time

def task1():
    print("Thread 1 started")
    time.sleep(2)
    print("Thread 1 complete")
    
def task2():
    print("Thread 2 started")
    time.sleep(2)
    print("Thread 2 complete")
    

task1()
task2()
#both threads started at same time and after 2 seconds they completed