# Homework Lesson 2 - Numbers - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 0 - This exercise is solved so you can have an ----------
# example of how we are expecting your answers to be.
#
# You are shopping online and found two items with prices $5.99
# and $3. Calculate and print the total cost.
item1_price = 5.99
item2_price = 3
total_cost = item1_price + item2_price
print(total_cost)

# ---------------------------------------------------------------------
# Exercise 1 - Travel Distance
# Alex is planning a road trip and wants to know the total distance
# he will be driving. He will travel at an average speed of 60 miles
# per hour and has 4 hours available for driving. Calculate the
# total distance he can cover and print the result.

average_speed = 60
hours_available = 4
total_distance = average_speed * hours_available
print(total_distance)

# ---------------------------------------------------------------------
# Exercise 2 - Pizza Slices
# A pizza is cut into 8 equal slices. Calculate and print how many
# slices each person will get if there are 4 people sharing the pizza.
pizza_slices = 8
people = 4
slices_per_person = pizza_slices / people
print(slices_per_person)

# ---------------------------------------------------------------------
# Exercise 3 - Shopping Discount
# Lisa wants to buy a pair of shoes that cost $80. The store is
# offering a 20% discount on the shoes.
# Create two variables: original_price and discount_percentage and
# assign the given values.
# Create final_price to calculate the price Lisa has to pay and
# print the result.
# The formula to count the discounted price:
# multiply the original price by the discount percentage and divide by 100.
original_price = 80
discount_percentage = 20
final_price = original_price * (100 - discount_percentage) / 100
print(final_price)


# ---------------------------------------------------------------------
# Exercise 4 - Temperature Conversion
# You are designing a weather app and need to convert temperature
# from Celsius to Fahrenheit for display. Convert a given
# temperature and print the result.
# To convert Celsis to Fahrenheit you need to multiply
# the temperature in Celsius by 9/5 and add 32 to the result

celsius_temperature = 25
fahrenheit_temperature = celsius_temperature * 9/5 + 32
print(fahrenheit_temperature)

# ---------------------------------------------------------------------
# Exercise 5 - Gardening
# You're planning a garden and need to calculate the area of
# a circular flowerbed with a radius of 3.5 meters. Calculate
# and print the area of the flowerbed.
# To calculate the area of a circle, multiply π (~3.141) with the square of
# the circle's radius.
import math

radius = 3.5
area = math.pi * radius ** 2
print(area)


# ---------------------------------------------------------------------
# Exercise 6 - Convert Temperature
# You're building a weather app, and you want to display the current
# temperature rounded to the nearest whole number. The
# temperature data you received from the weather service is a float.
# Your task is to convert the float temperature to an integer
# temperature for display.
# As an example, if the temperature is 24.8ºC, you need to print 24.
temperature = 24.8
rounded_temperature = round(temperature)
print(rounded_temperature)


# ---------------------------------------------------------------------
# Exercise 7 - Baking Cookies
# You are baking cookies and have 17 chocolate chips. You
# want to distribute them evenly into 5 cookies. Calculate and
# print the number of chocolate chips in each cookie and the
# remaining chips.
chocolate_chips = 17
cookies = 5
chips_per_cookie = chocolate_chips // cookies
remaining_chips = chocolate_chips % cookies
print(chips_per_cookie)
print(remaining_chips)


# ---------------------------------------------------------------------
# Exercise 8 - Fix the Code - Event total earnings
# FOR THIS EXERCISE YOU WILL HAVE AN EXISTING CODE THAT IS
# NOT WORKING CORRECTLY. YOUR TASK IS TO LOOK AT THE CODE
# AND FIX THE PROBLEM SO IT WORKS AS EXPECTED.
#
# Tip: Copy the code and try to run it alone. See the results
# and try to figure out why it is not working.
#
# You organized two events. The first event had 250 participants
# and the second event had 500 participants. With a ticket price
# of $1000, calculate and print the total earning of the two events
# together.
#
# For the values provided we are expecting a total earning of 750000,
# however the code is not working correctly. Can you fix it?
# Corrected code to calculate total earnings from two events
event1_participants = 250
event2_participants = 500
ticket_price = 1000

total_earnings = (event1_participants + event2_participants) * ticket_price
print(total_earnings)

# ---------------------------------------------------------------------
# Exercise 9 - Fix the Code - Student age mean
# FOR THIS EXERCISE YOU WILL HAVE AN EXISTING CODE THAT IS
# NOT WORKING CORRECTLY. YOUR TASK IS TO LOOK AT THE CODE
# AND FIX THE PROBLEM SO IT WORKS AS EXPECTED
#
# Tip: Copy the code and try to run it alone. See the results
# and try to figure out why it is not working.
#
# You're a teacher organizing a school event and need to
# calculate the mean age of three students participating in
# the event. The ages of the students are as follows:
#   Student 1: 15 years old
#   Student 2: 17 years old
#   Student 3: 13 years old
#
# For these ages, we expect an age mean of 15.0, but your code
# is returning 36.3. Fix the code to print the correct value.
student_1_age = 15
student_2_age = 17
student_3_age = 13

students_mean_age = (student_1_age + student_2_age + student_3_age) / 3
print(students_mean_age)

# ---------------------------------------------------------------------
# Challenge (OPTIONAL!): Separating Digits of a Number
# Given the number 1597, your task is to write a Python code
# that separates this number into four variables, each containing
# a digit of the number: 1, 5, 9, and 7. You'll use the
# knowledge of Python operators % and /, variable assignment,
# and working with integers to accomplish this task.

# Tip: To separate the digits of a number, think about how you
# can extract each digit using the remainder (%) and division (/)
# operators. Start by extracting the last digit and then move on
# to the next digits by dividing the number progressively.
# Remember that the remainder when dividing by 10 gives you
# the last digit, and integer division by 10 removes the last digit.
#
# The following code should help you to get an understanding on
# how to get the digits of the number
number = 1597

digit_1 = number % 10
number //= 10
digit_2 = number % 10
number //= 10
digit_3 = number % 10
number //= 10
digit_4 = number % 10
# print(digit_1) # will print 7
# print(number)  # will print 159

# If you repeat this operation with the second, the third and
# the fourth digits, you will be able to get all the digits.
# Your code here

# Print the result for all four digits
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
