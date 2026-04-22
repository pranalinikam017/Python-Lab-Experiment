import matplotlib.pyplot as plt

# 1. Data: Temperature of two different cities over 5 days
days = [1, 2, 3, 4, 5]
city_a_temp = [30, 32, 31, 29, 30]
city_b_temp = [25, 26, 24, 27, 28]

# 2. Plotting the data
# The 'label' keyword is what the Legend will use
plt.plot(days, city_a_temp, label="Mumbai", color='orange', marker='o', linewidth=2)
plt.plot(days, city_b_temp, label="Bangalore", color='blue', marker='s', linestyle='--')

# 3. Customizing the Title and Axis Labels
plt.title("City Temperature Comparison", fontsize=14, fontweight='bold', color='darkblue')
plt.xlabel("Day Number", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

# 4. Adding the Legend
# 'loc' tells Matplotlib where to put the box (best, upper right, lower left, etc.)
plt.legend(loc="best", shadow=True, fontsize='medium')

# 5. Adding a Grid
plt.grid(True, linestyle=':', alpha=0.6)

# 6. Show the plot
plt.show()