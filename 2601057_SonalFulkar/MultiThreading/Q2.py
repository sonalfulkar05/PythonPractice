#5. Two threads: Modify Question 4 to run the functions using two threads. Start both threads and use join() to wait for both. Measure and compare the time



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
    

t1 = Thread(target = task1)
t2 = Thread(target = task2)

t1.start()
t2.start()
t1.join()
t2.join()