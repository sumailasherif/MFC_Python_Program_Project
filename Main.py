import numpy as np
import matplotlib.pyplot as plt


# --- User Input ---
print("=" * 50)
print("   Student Exam Score Z-Score Analyzer")
print("=" * 50)
print("\nEnter student scores separated by spaces (e.g. 55 60 72 88 95):")
user_input = input(" ")

# Sanitize input: replace commas used as decimals with periods
user_input = user_input.replace(",", ".")

# Convert input string to NumPy array
data_array = np.array([float(x) for x in user_input.split()])

# Generate student labels (S001, S002, ...)
students = [f"S{i+1}" for i in range(len(data_array))]