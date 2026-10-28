
# Mini Project 3: ATM Withdrawal System

name = input("Enter account holder name: ")
balance = float(input("Enter current balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

print("\n----- ATM Transaction Details -----")
print("Account Holder:", name)

if withdrawal <= 0:
    print("Transaction Status: Failed")
    print("Reason: Withdrawal amount must be greater than ₹0.")

else:
    if withdrawal > balance:
        print("Transaction Status: Failed")
        print("Reason: Withdrawal amount exceeds current balance.")

    else:
        if withdrawal > 20000:
            print("Transaction Status: Failed")
            print("Reason: Maximum withdrawal allowed is ₹20,000.")

        else:
            balance = balance - withdrawal

            print("Transaction Status: Successful")
            print("Withdrawn Amount: ₹", withdrawal)
            print("Remaining Balance: ₹", balance)

            if balance < 1000:
                print("Low Balance Warning")
