# Check divisibility of a number by 3 and 5
# Prompt the user to enter a number
# Check if the number is divisible by 3, 5, or both, and print the appropriate message


number= int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 3 and 5.")
elif number % 5 == 0:
    print(f"{number} is divisible by 5.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 3 or 5.")

# The program prompts the user to enter a number and checks its divisibility by 3 and 5.
# It then prints whether the number is divisible by 3, 5, both, or neither.