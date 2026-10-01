# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")
# This comverts the string into all lowercase letters
print(f"Modified String 2: {user_string.upper()}")
# Thi converts the string into all uppercase letters
print(f"Modified String 3: {user_string.strip()}")
# This removes any whitespace from the beginning and end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}")
# This replaces all instance of letter 'a' with '@' 
print(f"Modified String 5: {user_string.capitalize()}")
# This capitalises the first letter of the string
print(f"Modified String 6: {user_string[::-1]}")
# This reverses the string
print(f"Modified String 7: {user_string.title()}")
# This capitalises the first letter of each word
print(f"Modified String 8: {len(user_string)}")
# This returns the length (number of charaacters) of the string
print(f"Modified String 9: {user_string.find('a')}")
# This finds the first occurrence of letter 'a', and returns its position (0 indexed, meaning first letter is position 0 rather then 1)
print(f"Modified String 10: {user_string.count('a')}")
# This counts the number of times letter 'a' appears in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")
# This checks if the string starts with the word 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}")
# This checks if the string ends with the character '!'
print(f"Modified String 13: {user_string.isalnum()}")
# This checks if the string contains only alphanumeric characters
print(f"Modified String 14: {user_string.isalpha()}")
# This checks if the string contains only alphabetic characters
print(f"Modified String 15: {user_string.isdigit()}")
# This checks if the string contains only digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!