"""
script: CIS129 Module 11 Lab
author: Israel Valenzuela
date: 04/30/2025
description: This Script prompts the user to enter grades and writes them to a file named grades.txt.
"""

with open("grades.txt", "w") as grades_file:
    print("Enter grades one by one. Type 'done' to finish.")
    while True:
        grade = input("Enter a grade: ")
        if grade.lower() == "done":
            break
        grades_file.write(grade + "\n")
print("Grades have been written to grades.txt.")