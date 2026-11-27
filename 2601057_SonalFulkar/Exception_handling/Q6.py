# Q6. Write a program
# Accept a number from the user.
# Convert it to an integer.
# Divide 100 by the number.
# Handle invalid input using ValueError.
# Handle division by zero using ZeroDivisionError.
# Print Calculation completed using finally.

try:
    num = input("Enter a number: ")
    num = int(num)  # Convert input to integer
    result = 100 / num  # Divide 100 by the number
    print("result:",result)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
finally:
    print("Calculation completed.")
    