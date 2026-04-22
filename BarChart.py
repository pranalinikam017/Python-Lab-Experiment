import matplotlib.pyplot as plt

# 1. Data: Categories and their corresponding values
categories = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
usage_scores = [95, 70, 60, 85, 50]
colors = ['skyblue', 'peru', 'silver', 'gold', 'lightgreen']

# 2. Create the Bar Chart
# plt.bar() takes the categories and values
plt.bar(categories, usage_scores, color=colors, edgecolor='black')

# 3. Customization (Labels and Title)
plt.title("Programming Language Popularity", fontsize=14)
plt.xlabel("Languages", fontsize=12)
plt.ylabel("Popularity Score (%)", fontsize=12)

# 4. Adding a Grid for the Y-axis only
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 5. Show the plot
plt.show()