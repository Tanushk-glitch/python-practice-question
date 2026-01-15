#Write a Python program that:
#Takes a string input from the user
#Counts how many vowels (a, e, i, o, u) are present

Displays the total number of vowels
text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

#After the running the code you will be able to the number of vovels present in the words given by you
