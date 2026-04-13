import random

num = random.randint(1,100)
print(num)

count = 0
while True:
    n = int(input("Enter your number:"))
    if(1 <= n <= 100):
        print()
        count += 1

    else:
        print("invalid choice")
    if(num == n):
        print("You guessed the Number")
        print(f"You tried {count} time")
        break
    elif(n < num):
        print("Too low")
    else:
        print("Too high")

