# Q7. Write a program
# Write a driving-license eligibility program:

# Accept the user's age.
# If age is less than 18, raise a ValueError.
# Handle the exception and print an appropriate message.
# Otherwise, display Eligible for driving license.

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise ValueError("you are under 18. NOT ELIGIBLE FOR DRIVING LICENSE")
except ValueError as e:
    print(e)
else:
    print("YOU ARE ELIGIBLE FOR A DRIVING LICENSE")
    
