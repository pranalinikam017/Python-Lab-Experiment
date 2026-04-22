import matplotlib.pyplot as plt

# Data: Exam scores of a class
scores = [45, 55, 62, 70, 75, 78, 82, 85, 88, 90, 92, 95, 98, 40, 50, 65, 75, 80]

# Create Histogram
# 'bins' defines how many groups to divide the data into
plt.hist(scores, bins=6, color='orange', edgecolor='black')

# Customization
plt.title("Distribution of Student Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")

plt.show()