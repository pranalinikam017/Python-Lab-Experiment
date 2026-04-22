import random

choices = [ "rock",
           "paper",
           "scissor"]

while True:
    user = input("Enter your Choice: ").strip().lower()
    if user not in choices :
      print("Invalid User Choice !")
      break
    computer = random.choice(choices)
    print(" Computer Choice:",computer)

    if(user == computer):
       print("Match Tie")

    elif(( user == "rock" and computer == "scissor") or (user == "scissor" and  computer =="paper") or ( user =="paper" and computer == "rock" )):
      print("You Win!")
    else:
      print("Computer Win !")

    again = input("Want to try again ! (y/n): ")
    if again =='y':
       continue
    else:
       print("Thanks for playing!")
       break
   

