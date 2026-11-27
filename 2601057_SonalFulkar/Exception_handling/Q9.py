# Q9. Write a program
# Create a marks-validation program:

# Accept marks from the user.
# Raise ValueError if marks are below 0 or above 100.
# Print marks if valid.
# Handle the exception with a meaningful message.

marks = int(input("Enter your marks:"))

try:
    if marks < 0 or marks > 100:
        raise ValueError("The marks must be between 0-100")
    print("marks:",marks)
    
except ValueError as e:
    print(e)
    
