import time 
duration = int(input("Enter countdown time in seconds: "))
while duration > 0:
    # Convert seconds to minutes:seconds
    minutes = duration // 60
    seconds = duration % 60
    print(f"{minutes:02d}:{seconds:02d}", end="\r")  # '\r' keeps it in the same line
    time.sleep(1)
    duration -= 1

print("Time is Up!")