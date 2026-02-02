def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")    
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice(1/2/3/4): ")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if choice == '1':
    print(f"{number1} + {number2} = {add(number1, number2)}")
elif choice == '2':
    print(f"{number1} - {number2} = {subtract(number1, number2)}")
elif choice == '3':
    print(f"{number1} * {number2} = {multiply(number1, number2)}")
elif choice == '4':
    try:
        print(f"{number1} / {number2} = {divide(number1, number2)}")
    except ValueError as e:
        print(e)

# By doing this, we learn how to create basic arithmetic functions and handle user input in Python.
# This is a simple calculator program that performs addition, subtraction, multiplication, and division.
# basic error handling 
# conditional statements to choose operations        