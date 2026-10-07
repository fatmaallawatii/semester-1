# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

numbers.sort()

if len(numbers) % 2 == 1:
    median = numbers[len(numbers) // 2]
else:
    middle = len(numbers) // 2
    median = (numbers[middle - 1] + numbers[middle]) / 2

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")