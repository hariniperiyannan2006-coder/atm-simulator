# ATM Simulation System
balance = 5000
pin = 1234
user_pin = int(input("Enter your PIN: "))
if user_pin == pin:
    print("1. Check Balance")
    print("2. Withdraw Money")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid option")
else:
    print("Wrong PIN")
