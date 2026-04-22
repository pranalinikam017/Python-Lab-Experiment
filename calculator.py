
def add_num(a , b):
    print("Result :" ,a + b)

def sub_num(a, b):
    print("Result : " ,a - b)

def mul_num(a ,  b):
    print("Result :", a * b)

def div_num(a, b):
    print("Result:" ,a / b)

def main():
    a = int(input("Enter your  first number:"))
    b = int(input("Enter your second number: "))
    
    while True:
        print("\n===== Calculator Functions =====")
        print("1. Addition ")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_num(a , b)
        elif choice == "2":
            sub_num(a, b)
        elif choice == "3":
            mul_num(a, b)
        elif choice == "4":
            div_num(a, b)
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

 