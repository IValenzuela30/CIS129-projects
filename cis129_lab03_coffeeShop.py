num_coffees = int(input("number of coffees purchased? "))
num_muffins = int(input("number of muffins purchased? "))

coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06

coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
subtotal = coffee_total + muffin_total
tax = subtotal * tax_rate
total = subtotal + tax

print("*******************************************")
print(" My coffee and muffin shop")
print(f"Number of coffees purchased: {num_coffees}")
print(f"Number of muffins purchased: {num_muffins}")
print("********************************************")
print(" My Coffee and Muffin Shop Receipt")
print(f" {num_coffees} Coffee at ${coffee_price} each: ${coffee_total:.2f}")
print(f" {num_muffins} Muffins at ${muffin_price} each: ${muffin_total:.2f}")
print(f" 6% tax: ${tax:.2f}")
print(" ---------")
print(f" Total: ${total:.2f}")
print("********************************************")
