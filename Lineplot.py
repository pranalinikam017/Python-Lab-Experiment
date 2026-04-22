import matplotlib.pyplot as plt

# 1. Prepare the Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [22, 24, 21, 25, 28, 26, 27]

# 2. Create the Plot
# 'marker' adds dots at the data points, 'color' sets the line color
plt.plot(days, temperature, marker='o', linestyle='-', color='red')

# 3. Add Labels and Title (The "Metadata")
plt.title("Weekly Temperature Report")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature in Celsius (°C)")

# 4. Add a Grid (makes it easier to read)
plt.grid(True)

# 5. Display the Plot
plt.show()