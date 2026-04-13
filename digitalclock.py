from datetime import datetime
import time
 

while True:
    current_time = datetime.now()  # Gets current date & time
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
      # Pauses the for 1 second
    if hour >= 12:
      am_pm = "PM"
    else:
      am_pm = "AM"

      # Convert to 12-hour format
    hour = hour % 12
    if hour == 0:
        hour = 12

    print(f"{hour:02d}:{minute:02d}:{second:02d} {am_pm}", end="\r")
    time.sleep(1)