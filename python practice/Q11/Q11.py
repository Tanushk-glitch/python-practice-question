#Write a program that:

#Stores a number n

#Uses a loop to calculate and print the sum of all even numbers from 1 to n

n = int(input("Enter a number: "))

sum_even = 0
for i in range(2, n+1, 2):
        sum_even += i
print(f"The sum of all even numbers from 1 to {n} is {sum_even}.")