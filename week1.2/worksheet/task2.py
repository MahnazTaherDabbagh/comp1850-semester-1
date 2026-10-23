# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

# Read a list of numbers from the user
numbers = read_numbers()

# Check that at least one number was provided
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

# Calculate the minimum value
minimum = min(numbers)

# Calculate the maximum value
maximum = max(numbers)

# Calculate the mean 
mean = sum(numbers) / len(numbers)

# Sort the numbers into ascending order
numbers.sort()

# Find the index of the middle value
middle = len(numbers) // 2

# Calculate the median
if len(numbers) % 2 == 1:
    #   If numbers are odd, use the middle number
    median = numbers[middle]
else:
    # Even numbers are even, average the two middle number
    median = (numbers[middle - 1] + numbers[middle]) / 2

# Display the numbers
print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")