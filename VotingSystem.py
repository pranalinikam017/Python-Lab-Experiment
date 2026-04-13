voters = {
    'candidate1': 0,
    'candidate2': 0,
    'candidate3': 0
}

vno = int(input("Enter the number of voters: "))

list1 = ['candidate1', 'candidate2','candidate3']

for i in range(vno):
    while True:
       select = input("Select one candidate: ")
       if select not in list1:
           print("Invalid Candidate . Enter again")
       else:
           voters[select] += 1
           break

print("\nVoting Results: ")
for candidate, votes in voters.items():
        print(candidate, ":" ,votes)

