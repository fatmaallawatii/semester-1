"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Fatma Allawati
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

try: 
    month_savings = int(input("What is the amount you want to save every month? "))
except:
    print ("Invalid amount")



# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
year_savings = month_savings * 12
print("The total money saved by the end of the year is: " , year_savings)

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest = year_savings * 0.008
final_total = year_savings + interest

print(f"Your total with 0.8% interest is £{final_total:.2f}")
