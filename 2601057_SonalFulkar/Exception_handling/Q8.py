# Create a custom exception named InsufficientBalanceError:

# Set balance = 10000.
# Accept a withdrawal amount.
# Raise your custom exception if withdrawal exceeds the balance.
# Otherwise deduct the amount and print the remaining balance.
# Handle your custom exception with except.
class InsufficientBalanceError(Exception):
    pass
bal = 10000
withdrawal_amt = int(input("enter the amount you want to withdraw: "))
try:
    if withdrawal_amt > bal:
        raise InsufficientBalanceError("insufficient balance")
    
except InsufficientBalanceError as e:
    print(e)
    
else:
    remaining_bal = bal - withdrawal_amt
    print("remaining balance: ",remaining_bal)
    

    