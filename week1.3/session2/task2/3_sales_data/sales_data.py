# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv
import csv
# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

try:
    with open("sales.csv", "r") as file:  
        reader = csv.DictReader(file)  
        data = list(reader)  

    largest = max(data, key=lambda row: int(row["Sales_Amount"])) 
    total = sum(int(row["Sales_Amount"]) for row in data)
    average = total / len(data)  

    widgets = {}

    for row in data:  
        product = row["Product"]
        units = int(row["Units_Sold"])
        widgets[product] = widgets.get(product, 0) + units  

    most_sold = max(widgets, key=widgets.get) 

    # Display the results
    print(f"Largest sale: {largest['Sales_Amount']} on {largest['Date']}")
    print(f"Average sale amount: {average:.2f}")
    print(f"Most sold widget: {most_sold} ({widgets[most_sold]} units)")

except FileNotFoundError:
    print("File not found")  # handles missing files
except ValueError:
    print("Invalid sales data")  # handles invalid numbers

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows