import numpy as np
import matplotlib.pyplot as plt


# This helps to get user input to calculate
print("Enter numbers separated by spaces (e.g. 10 12 15 18 20):")
user_input = input(" ")

# This converts input string to NumPy arra
data_array = np.array([float(x) for x in user_input.split()])

# Calculate mean and standard deviation
mean = np.mean(data_array)
std_dev = np.std(data_array)

# Compute Z-scores
z_scores = (data_array - mean) / std_dev

print("Data:", data_array)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Z-scores:", z_scores)


# --- Graphic representation ---
plt.figure(figsize=(8, 5))

# Plot the data points
plt.scatter(data_array, z_scores, color='green', label='Data points')

# Add horizontal line at Z=0 (mean)
plt.axhline(0, color='red', linestyle='--', label='Mean (Z=0)')

# Annotate each point with its Z-score
for i, txt in enumerate(z_scores):
    plt.annotate(f"{txt:.3f}", (data_array[i], z_scores[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Labels and title
plt.title("Z-scores of Data Points")
plt.xlabel("Data Values")
plt.ylabel("Z-score")
plt.legend()
plt.grid(True)

plt.show()

