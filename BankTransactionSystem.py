accounts = {}


def Create_Account():
    Name = input("\nEnter Account holder name: ")
    ACno = int(input("Enter Account number: "))

    if ACno in accounts:
        print("Account already exists!")
    else:
        accounts[ACno] = {
            "name": Name,
            "balance": 0,
            "transactions": []
        }
        print("\nAccount created successfully!")


def Deposit():
    ACno = int(input("\nEnter Account Number: "))
    if ACno not in accounts:
        print("Account not found!")
    else:
        DeNo = int(input("\nEnter deposit amount: "))
        accounts[ACno]["balance"] += DeNo
        print(f"Deposit successful! New balance: {accounts[ACno]['balance']}")

def Withdraw():
    ACno = int(input("\nEnter Account Number: "))
    if ACno not in accounts:
        print("\nAccount not found!")
        return

    WD = int(input("\nEnter withdraw money:"))
    if WD <= 0:
        print("\nInvalid amount!")
    elif WD > accounts[ACno]["balance"]:
        print("\nInsufficient balance!")
    else:
        accounts[ACno]["balance"] -= WD
        print(f"Withdrawal successful! New balance: {accounts[ACno]['balance']}")

def CheckBalance():
    ACno = int(input("\nEnter Account Number: "))
    if ACno not in accounts:
        print("\nAccount not found!")
        return
    else:
        print("\nCurrent balance: ", accounts[ACno]['balance'])

def ViewTransaction():
    ACno = int(input("\nEnter Account Number: "))
    if ACno not in accounts:
        print("Account not found!")
    else:
        print(f"Transaction history for account {ACno}:")
        if not accounts[ACno]["transactions"]:
            print("No transactions yet.")
        else:
            for trans in accounts[ACno]["transactions"]:
                print(trans)



def main():
    
    while True:
        print("\n===== Banking Operations  =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3.  Withdraw Money")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            Create_Account()
        elif choice == "2":
            Deposit()
        elif choice == "3":
            Withdraw()
        elif choice == "4":
            CheckBalance()
        elif choice == "5":
            ViewTransaction()
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()