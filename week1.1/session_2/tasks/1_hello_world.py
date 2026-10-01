# a basic Hello World program - write your code under this line

name = input("What is your name? ")
print(f"Hello, {name}!") 


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    answer = num1 + num2
    print(f"The answer is {answer}")
except:
        print("Please enter a valid number.")
