#Digit Frequency
#Write a program that:
#Takes a number n
#Uses a loop to count how many times the digit n appears in n


#n = input("Enter a number: ")
#count = 0
#for digit in n:
  #  if digit == "5":
 #       count += 1
#print(f"The digit 5 appears {count} times in the number {n}.")


n = input("Enter a number: ")
target = input("Enter the digit to count: ")

count = 0
for digit in n:
    if digit == target:
        count += 1

print(f"The digit {target} appears {count} times in the number {n}.")
# The program prompts the user to enter a number n and a target digit.
# It then uses a loop to count how many times the target digit appears in n and prints