import matplotlib.pyplot as plt

# Data: Monthly expenses
labels = ['Rent', 'Food', 'Travel', 'Entertainment', 'Savings']
sizes = [3000, 1500, 800, 1200, 2000] # Actual values
colors = ['lightcoral', 'gold', 'lightskyblue', 'lightgreen', 'mediumpurple']

# Create Pie Chart
# autopct='%1.1f%%' formats the number as a percentage automatically
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, shadow=True)

# Customization
plt.title("Monthly Expense Breakdown")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()