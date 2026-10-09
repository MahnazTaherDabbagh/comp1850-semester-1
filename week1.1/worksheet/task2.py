"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mahnaz Taher Dabbagh
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
try:
    monthly_savings = int(input("Please enter your monthly saving amount: "))
except ValueError:
    print("Invalid amount.")
    exit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
yearly_total = monthly_savings * 12
# print this out for the user with a suitable message.
print(f"Your total yearly savings is: £{yearly_total}")
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
interest_total = (yearly_total * 1.008)
# print this out in the format £X.XX (to two decimal places).
print(f"Your total yearly savings with interest is: £{interest_total:.2f}")

