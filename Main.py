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

# -------------------------------------------------------
# --- Mathematical Computation ---
# -------------------------------------------------------

# Calculate mean (average score)
mean = np.mean(data_array)

# Calculate standard deviation (spread of scores)
std_dev = np.std(data_array)

# Compute Z-scores: how far each score is from the mean
z_scores = (data_array - mean) / std_dev

# -------------------------------------------------------
# --- Classify Students Based on Z-Score ---
# Threshold of 1.0 (1 standard deviation) used for fairness
# with small class sizes (avoids misclassifying scores like 100)
# -------------------------------------------------------
classifications = []
for z in z_scores:
    if z >= 1.0:
        classifications.append("Outstanding  ⬆️")
    elif z <= -1.0:
        classifications.append("Needs Support ⬇️")
    else:
        classifications.append("Average       ✅")

# -------------------------------------------------------
# --- Output / Results ---
# -------------------------------------------------------
print("\n--- Z-Score Summary ---")
print(f"Mean Score:             {mean:.2f}")
print(f"Standard Deviation:     {std_dev:.2f}")
print(f"Highest Score:          {np.max(data_array):.2f}")
print(f"Lowest Score:           {np.min(data_array):.2f}")

print("\n--- Student Performance Report ---")
print(f"{'Student':<10} {'Score':<10} {'Z-Score':<10} {'Status'}")
print("-" * 55)
for i in range(len(data_array)):
    print(f"{students[i]:<10} {data_array[i]:<10.1f} {z_scores[i]:<10.3f} {classifications[i]}")
