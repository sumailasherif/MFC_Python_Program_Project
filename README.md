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
<img width="877" height="125" alt="image" src="https://github.com/user-attachments/assets/ebc238ca-5b60-4d11-91a5-1640198705a9" />

**Code screenshot**


<img width="800" height="1962" alt="screenshot_code" src="https://github.com/user-attachments/assets/2b946031-f050-494b-a9ef-7ffc3a9bd8c2" />

**Sample Output(terminal)**

<img width="680" height="520" alt="screenshot_terminal" src="https://github.com/user-attachments/assets/8262c4b7-15e5-401a-9914-76cd6792f8c3" />

**Graphs
After printing the results the program opens two side-by-side graphs:**

<img width="2084" height="947" alt="screenshot_graph" src="https://github.com/user-attachments/assets/ca9e723a-2d02-46d6-91bb-60d5b20254c9" />

Left — Z-Score Scatter Plot
Each dot is a student. The horizontal position is their raw score, the vertical position is their Z-score. The dashed black line marks Z = 0 (the class mean). The blue dotted line marks the Outstanding threshold (Z = 1.0) and the red dotted line marks the Needs Support threshold (Z = −1.0).
Right — Bar Chart
Each bar shows a student's raw score. The orange dashed line marks the class mean. Bars are color-coded to match the scatter plot so both graphs tell the same story at a glance.



**Author**
Sherif Sumaila
Repository: MFC_Python_Program_Project






