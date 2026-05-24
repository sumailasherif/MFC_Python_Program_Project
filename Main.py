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
