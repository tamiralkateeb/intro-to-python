# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
# Challenge 1
# Make a number Positive

# Create a variable called my_number and set it to any integer value.
my_number = -3  # Example input, you can change this to any integer

# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
if my_number < 0:
    my_number = -my_number

print(my_number)  # Output: 3 if input is -3, 5 if input is 5

# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
# Challenge 2
# BinGo!

# If the number is divisible by 3, print “Bin”
# If the number is divisible by 7, print “Go”
# For numbers which are divisible by 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”

number = 21  # Example input, you can change this to any integer

if number % 3 == 0 and number % 7 == 0:
    print("BinGo")
elif number % 3 == 0:
    print("Bin")
elif number % 7 == 0:
    print("Go")
else:
    print(f"{number} is just a number")

# ---------------------------------------------------------------------

# Challenge 3
# Challenge 3
# Find the middle number

# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.

x, y, z = 1, 5, 3  # Example input, you can change this to any three different integers

if (y < x < z) or (z < x < y):
    middle = x
elif (x < y < z) or (z < y < x):
    middle = y
else:
    middle = z

print(middle)  # Output: 3 if inputs are x=1, y=5, z=3

# ---------------------------------------------------------------------

# Challenge 4
# Challenge 4
# Palindrome Numbers

# Ask a user to input a number.
number = input("Enter a number: ")

# Write a program to check if the given number is a palindrome.
is_palindrome = number == number[::-1]

# It should print True if the number is a palindrome and False if it is not.
print(is_palindrome)  # Example: True if input is 121, False if input is 123

# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
# Challenge 5
# Reverse a string

# Example: "tcefreP!" -> Perfect!

review = "tcefreP!"  # Example input, you can change this to any string
# Strip punctuation from the beginning
punctuation = ''
while not review[0].isalpha():
    punctuation += review[0]
    review = review[1:]

# Reverse the string
corrected_review = review[::-1] + punctuation
print(corrected_review)  # Output: "Perfect!"
