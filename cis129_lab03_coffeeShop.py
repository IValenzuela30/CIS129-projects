"""
script: CIS129 Module 3 Lab
author: Israel Valenzuela
date: 10/11/2023
description: This program calculates the total cost of a customer's order at Dunkin Muffins, including tax.
"""

# Input
num_coffees = int(input("number of coffees purchased? "))
num_muffins = int(input("number of muffins purchased? "))
num_CheeseDanish = int(input("number of Cheese Danishes purchased? "))
num_Croissants = int(input("number of croissants purchased? "))

# Constants
coffee_price = 5.00
muffin_price = 4.00
CheeseDanish_price = 3.00
Croissant_price = 2.00
tax_rate = 0.06

# Calculate totals
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
CheeseDanish_total = num_CheeseDanish * CheeseDanish_price
Croissant_total = num_Croissants * Croissant_price
subtotal = coffee_total + muffin_total + CheeseDanish_total + Croissant_total
tax = subtotal * tax_rate
total = subtotal + tax

# Output
print("*******************************************")
print(" Dunkin Muffins ")
print(f"Number of coffees purchased: {num_coffees}")
print(f"Number of muffins purchased: {num_muffins}")
print(f"Number of Cheese Danishes purchased: {num_CheeseDanish}")
print(f"Number of Croissants purchased: {num_Croissants}")
print("********************************************")
print(" Dunkin Muffins Reciept")
print(f" {num_coffees} Coffee at ${coffee_price} each: ${coffee_total:.2f}")
print(f" {num_muffins} Muffins at ${muffin_price} each: ${muffin_total:.2f}")
print(f" {num_CheeseDanish} Cheese Danishes at ${CheeseDanish_price} each: ${CheeseDanish_total}")
print(f" {num_Croissants} Croissants at ${Croissant_price} each: ${CheeseDanish_total}")
print(f" 6% tax: ${tax:.2f}")
print(" ---------")
print(f" Total: ${total:.2f}")
print("********************************************")
print("Thank you for dunking by Dunkin Muffins!!!")
