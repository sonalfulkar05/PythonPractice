#6. Thread arguments: Write a function display_student(name, roll_number) that prints a student's name and roll number. Run it in a thread by passing arguments using args.

from threading import Thread

def display_student(name, roll_number):
    print("Name:",name,"\nroll no:",roll_number)
    
t1 = Thread(target = display_student,args=("Sonal",57))

t1.start()