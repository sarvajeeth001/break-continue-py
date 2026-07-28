Balance = 1000
transaction = []
while True:
    print("FIFA world cup Bank")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transaction History")
    print("5. Exit")

    choose = input("Enter your refrence number: ")
    if choose == "1":
        print("Your current balance is: ₹", Balance)
    elif choose == "2":
        amount = float(input("Enter the amount to deposit: ₹"))
        Balance += amount
        transaction.append(f"Deposited: ₹{amount}")
        print("Amount deposited successfully.")
    elif choose == "3":
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount > Balance:
            print("Insufficient balance.")
        else:
            Balance -= amount
            transaction.append(f"Withdrew: ₹{amount}")
            print("Amount withdrawn successfully.")
    elif choose == "4":
        print("Transaction History:")
        for t in transaction:
            print(t)
    elif choose == "5":
        print("Thank you for using FIFA world cup Bank.")
        break