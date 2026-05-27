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

Why 1.0 and not 1.5?
With small class sizes (e.g. 7 students), a threshold of 1.5 is too strict. A score of 100 can produce a Z-score of exactly 1.5, which a > 1.5 check would incorrectly classify as Average. Using >= 1.0 gives fair, meaningful results for any class size.

**Worked Example**
For scores: 55  60  72  78  88  40  100

Mean    =  (55 + 60 + 72 + 78 + 88 + 40 + 100) / 7  =  70.43

Std Dev =  18.96

Z (S7, score=100):  (100 − 70.43) / 18.96  =  +1.560  →  Outstanding ⬆️

Z (S6, score=40):   (40  − 70.43) / 18.96  =  −1.605  →  Needs Support ⬇️

Z (S1, score=55):   (55  − 70.43) / 18.96  =  −0.814  →  Average ✅

**How to run**

Enter scores when prompted
=================================================
   Student Exam Score Z-Score Analyzer
==================================================

Enter student scores separated by spaces:
 55 60 72 78 88 40 100

 <img width="875" height="358" alt="image" src="https://github.com/user-attachments/assets/5df0eddf-0cad-41d4-bfec-197221b278d1" />



