# Worksheet 1.2: Task 1 Solution

import sys

# Ask the user to input a grade between 0 and 100
grade = input("Enter your grade between 0 and 100: ")

# Validate that they have entered an integer.
if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

# Convert the grade input to an integer
grade = int(grade)

# Check that the grade is within the range
if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

# Determine the result based on the grade
if grade <= 39:
    result = "Fail"
elif grade <= 69:
    result = "Pass"
else:
    result = "Distinction"

# Display the grade and result 
print(f"{grade} is a {result}")