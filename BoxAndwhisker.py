import matplotlib.pyplot as plt

# 1. Data: Monthly rainfall in millimeters
# Notice how 80 is much higher than the others (an outlier)
rainfall = [20, 25, 30, 35, 32, 28, 22, 26, 29, 80]

# 2. Create the Box Plot
# 'patch_artist=True' allows us to fill the box with color
plt.boxplot(rainfall, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2))

# 3. Customization
plt.title("Monthly Rainfall Distribution")
plt.ylabel("Rainfall (mm)")

# 4. Show the plot
plt.show()