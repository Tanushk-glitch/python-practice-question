# Program to sum odd or even numbers based on the input n
# Write a program that:
# Takes a number n
# Uses a loop to add:       
#Odd numbers if n is odd
#Even numbers if n is even
#(from 1 to n)


n = int(input("Enter a number: "))
if n % 2 == 0:
    sum_even = 0
    for i in range(2, n+1, 2):
        sum_even += i
    print(f"The sum of all even numbers from 1 to {n} is {sum_even}.")
else:
    sum_odd = 0
    for i in range(1, n+1, 2):
        sum_odd += i
    print(f"The sum of all odd numbers from 1 to {n} is {sum_odd}.")

# The program prompts the user to enter a number n.
# It checks if n is even or odd and then uses a loop to calculate the sum of either all even or all odd numbers from 1 to n, printing the result accordingly.