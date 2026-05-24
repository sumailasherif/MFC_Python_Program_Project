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

# -------------------------------------------------------
# --- Visualization ---
# Two side-by-side graphs: scatter plot + bar chart
# -------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Student Exam Score Z-Score Analyzer", fontsize=14, fontweight="bold")

# Color coding: blue = outstanding, green = average, red = needs support
colors = ["blue" if z >= 1.0 else "red" if z <= -1.0 else "green" for z in z_scores]

# -- Graph 1: Z-Score Scatter Plot --
ax1 = axes[0]
ax1.scatter(data_array, z_scores, color=colors, s=100, zorder=5)

# Reference lines at mean and classification thresholds
ax1.axhline(0, color="black", linestyle="--", linewidth=1, label="Mean (Z=0)")
ax1.axhline(1.0, color="blue", linestyle=":", linewidth=1, label="Outstanding (Z≥1.0)")
ax1.axhline(-1.0, color="red", linestyle=":", linewidth=1, label="Needs Support (Z≤-1.0)")

# Annotate each point with student label and Z-score value
for i in range(len(data_array)):
    ax1.annotate(
        f"{students[i]}\n{z_scores[i]:.2f}",
        (data_array[i], z_scores[i]),
        textcoords="offset points",
        xytext=(0, 12),
        ha="center",
        fontsize=8
    )

ax1.set_title("Z-Scores of Student Scores")
ax1.set_xlabel("Exam Score")
ax1.set_ylabel("Z-Score")
ax1.legend(fontsize=8)
ax1.grid(True, linestyle="--", alpha=0.5)

# -- Graph 2: Bar Chart with Mean Line --
ax2 = axes[1]
bars = ax2.bar(students, data_array, color=colors, edgecolor="black", alpha=0.8)

# Orange dashed line showing the class mean
ax2.axhline(mean, color="orange", linestyle="--", linewidth=2, label=f"Mean = {mean:.1f}")

# Label each bar with the actual score
for bar, score in zip(bars, data_array):
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f"{score:.0f}",
        ha="center", va="bottom", fontsize=9
    )

ax2.set_title("Student Scores with Mean Line")
ax2.set_xlabel("Student")
ax2.set_ylabel("Score")
ax2.legend(fontsize=8)
ax2.grid(True, axis="y", linestyle="--", alpha=0.5)
