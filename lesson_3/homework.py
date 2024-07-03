# Homework Lesson 2 - Strings

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Personalized Greeting
# Write a program that takes a user's name as input
# and then greets them using an f-string: "Hello, [name]!"
#
# Example Input: "Alice"
# Example Output: "Hello, Alice!"
name = input("Enter your name: ")
print(f"Hello, {name}!")

# ---------------------------------------------------------------------
# Exercise 2: Greeting with User's Favorite Activity
# Write a program that takes a user's name and their
# favorite activity as input, and then greets them
# using the formatting method of your choice as:
# "Hello, [name]! Enjoy [activity]!"

# Example Input:
# Name: Emily
# Favorite Activity: hiking
# Example Output: "Hello, Emily! Enjoy hiking!"
name = input("Enter your name: ")
activity = input("Enter your favorite activity: ")
print("Hello, {}! Enjoy {}!".format(name, activity))


# ---------------------------------------------------------------------
# Exercise 3: Membership Cards
# You are designing a simple registration system for a club.
# When new members sign up, you want to ensure their names
# are displayed in uppercase on their membership cards.
# Write a program that takes the new member's name as
# input and prints it in uppercase and prints a welcome message
# using .format()

# Example Input:
# Name: Emily
# Example Output: "Welcome, Emily! Your name in uppercase is: EMILY!"
name = input("Enter your name: ")
print("Welcome, {}! Your name in uppercase is: {}".format(name, name.upper()))


# ---------------------------------------------------------------------
# Exercise 4: User Profile Creation
# Build a user profile generator. Ask
# the user for their first name, last name, and age. Create
# a profile summary using .title(), .upper(), and .format().
#
# Example Input:
# First name: john
# Last name: smith
# Age: 28
#
# Example Output:
# Name: John Smith
# Age: 28
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

profile = "Name: {} {}\nAge: {}".format(first_name.title(), last_name.title(), age)
print(profile)


# ---------------------------------------------------------------------
# Exercise 5: Text message limits
# You are developing a text messaging application that limits the
# number of characters in a single message. Your task is to create
# a Python program that takes a message as input from the user.
# The program should calculate and display the number of characters
# in the message, including spaces, and format the output using
# an f-string. This character count will help users ensure their
# messages fit within the allowed limit.
message = input("Enter your message: ")
message_length = len(message)
print(f"Your message has {message_length} characters.")


# ---------------------------------------------------------------------
# Exercise 6: Text Transformation Game
# Create a text transformation game. Ask the user
# to enter a sentence. Replace all vowels with '*'. Display the
# modified sentence.
#
# Example Input: "Hello, world!"
# Example Output: "H*ll*, w*rld!"
sentence = input("Enter a sentence: ")
vowels = 'aeiouAEIOU'
transformed_sentence = ''.join(['*' if char in vowels else char for char in sentence])
print(transformed_sentence)

# ------------------------------# ---------------------------------------------------------------------
# Exercise 7: Extracting Information
# The variable 'data' is a student record in the format "name:age"
# Use string slicing and string methods to extract the name and the age
# and print the result formatted.
#
# data = "lucy smith:28"
#
# Expected output:
# Name: Lucy Smith
# Age: 28
data = "lucy smith:28"
name, age = data.split(':')
print(f"Name: {name.title()}\nAge: {age}")


# ---------------------------------------------------------------------
# Exercise 8: Miles to Kilometers Conversion
# Write a program that converts a distance in miles to kilometers.
# Take the distance in miles as input, convert it to kilometers
# using the formula miles * 1.6, and display the
# result using f-strings.

# Example Input: 10
# Example Output: 10 miles is approximately 16.0 kilometers.

# We are converting the input string to float:
# Input: float("1.23")
# Output: 1.23
miles = float(input("Enter distance in miles: "))
kilometers = miles * 1.6
print(f"{miles} miles is approximately {kilometers} kilometers.")



# ---------------------------------------------------------------------
# Exercise 9: Workouts calculator
# Write a Python program that asks the user to input the number
# of minutes spent on three different exercises: cardio, strength
# training, and yoga using the input() function. Convert the input
# strings to integers using the int() function. Calculate the
# total time spent on workouts by summing up the minutes from all
# three activities. Based on the total workout time, provide a
# motivational message using an f-string that encourages the user
# to stay consistent and reach their fitness goals. Display the
# motivational message to the user.
cardio = int(input("Enter minutes spent on cardio: "))
strength_training = int(input("Enter minutes spent on strength training: "))
yoga = int(input("Enter minutes spent on yoga: "))

total_minutes = cardio + strength_training + yoga
print(f"Great job! You spent a total of {total_minutes} minutes working out today. Keep it up and stay consistent to reach your fitness goals!")


# ---------------------------------------------------------------------
input_number = -324

# Convert the integer to a string to handle the negative symbol separately
num_str = str(input_number)

# Reverse the digits (excluding the negative symbol) using slicing [::-1]
reversed_str = num_str[1:][::-1]

# Add the negative symbol back to the reversed string
reversed_num = int(num_str[0] + reversed_str)

# Output the result
print(reversed_num)


# ---------------------------------------------------------------------
# Challenge 2 (OPTIONAL!): Formatting Average Speed
# Taking input for miles and hours
miles = int(input("Enter the number of miles: "))
hours = int(input("Enter the total number of hours: "))

# Calculating average speed
average_speed = miles / hours

# Formatting and displaying the result
rounded_speed = round(average_speed, 1)
print(f"The average speed is {rounded_speed} miles per hour")
