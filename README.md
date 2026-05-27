# MFC_Python_Program_Project
This is a  Python program that applies Z-Score Analysis to student exam results.
Enter any number of scores and the program will instantly calculate the class mean, standard deviation, and individual Z-scores — then classify every student as Outstanding, Average, or Needs Support, and display two visualisation graphs.

**Table of Contents**
- Overview
- The Mathematics
- Features
- Requirements
- How to Run
- Code Screenshot
- Sample Output
- Graphs
- Project Structure
- Author

**Overview**
This project was built to demonstrate the real-world application of Z-scores in a classroom setting.
A teacher can run the program, type in their students' exam scores, and immediately receive:

1. The class mean and standard deviation
2. A Z-score for every student
3. A performance classification per student
4. A formatted results table in the terminal
5. Two visualisation graphs — a scatter plot and a bar chart
6. The Mathematics

   
**The Z-Score Formula**
_Z  =  ( X − μ ) / σ_


**Symbol**                  **Meaning**

X   =                    Individual student score

μ   =                   Mean (average) of all scores

σ   =                   Standard deviation

Z   =                   Resulting Z-score

**Standard Deviation Formula**
_σ  =  √( Σ(Xᵢ − μ)²  /  N )_

**Classification Thresholds**

**Z-Score Range**       **Classification**

Z ≥ 1.0 =               ⬆️ Outstanding

−1.0 < Z < 1.0  =       ✅ Average

Z ≤ −1.0      =         ⬇️ Needs Support

