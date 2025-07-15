# Kristina Chorna
# Programming Exercise 12
# The purpose of this code is to calculate the statistics of the student grades using numpy and display the results.

import numpy as np
import csv

grades = []

with open('grades.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        exams = list(map(int, row[2:]))
        grades.append(exams)

grades = np.array(grades)

# display first few rows
print("First few rows of exam scores:\n", grades[:5])

# get the statistics for each exam
print("\n--- Per Exam Statistics ---")
for i in range(3):
    exam_scores = grades[:, i]
    print(f"\nExam {i+1} Statistics:")
    print(f"Mean: {np.mean(exam_scores):.2f}")
    print(f"Median: {np.median(exam_scores)}")
    print(f"Std Dev: {np.std(exam_scores):.2f}")
    print(f"Min: {np.min(exam_scores)}")
    print(f"Max: {np.max(exam_scores)}")

# calculate the overall statistics of the exams
all_scores = grades.flatten()
print("\n--- Overall Statistics Across All Exams ---")
print(f"Mean: {np.mean(all_scores):.2f}")
print(f"Median: {np.median(all_scores)}")
print(f"Std Dev: {np.std(all_scores):.2f}")
print(f"Min: {np.min(all_scores)}")
print(f"Max: {np.max(all_scores)}")

# determine which students passed/ failed each exam and display the results
print("\n--- Pass/Fail Counts per Exam (Pass = 60+) ---")
for i in range(3):
    exam_scores = grades[:, i]
    passed = np.sum(exam_scores >= 60)
    failed = np.sum(exam_scores < 60)
    print(f"Exam {i+1}: Passed = {passed}, Failed = {failed}")

# calculate the overall pass percentage
total_scores = grades.size
total_passes = np.sum(grades >= 60)
pass_percentage = (total_passes / total_scores) * 100

# display the result 
print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")
