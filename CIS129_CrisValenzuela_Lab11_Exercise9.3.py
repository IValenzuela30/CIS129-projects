"""
script: CIS129 Module 11 Lab
author: Israel Valenzuela
date: 04/30/2025
description: This script creates student records in a CSV file.
"""

import csv

with open("grades.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    
    print("Enter student records. Type 'done' as the first name to finish.")
    while True:
        firstname = input("Enter first name: ")
        if firstname.lower() == "done":
            break
        lastname = input("Enter last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        writer.writerow([firstname, lastname, exam1, exam2, exam3])
print("Student records have been written to grades.csv.")