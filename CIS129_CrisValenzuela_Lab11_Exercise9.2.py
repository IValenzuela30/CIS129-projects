"""
script: CIS129 Module 11 Lab
author: Israel Valenzuela
date: 04/30/2025
description: This script reads a file containing grades, and gives statistics about them.
"""
with open("grades.txt", "r") as grades_file:
    grades = [float(line.strip()) for line in grades_file]

print("Grades:", grades)
print("Total:", sum(grades))
print("Count:", len(grades))
print("Average:", sum(grades) / len(grades) if grades else 0)