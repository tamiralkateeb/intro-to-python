# Homework: Loops

# Task 1. Create a basic for loop
name = "Joseph"
for char in name:
    print(char)

# Task 2. Create a basic `for` loop with a counter
name = 'Tom'
counter = 0

for char in name:
    counter += 1

# This should print '3'
print(counter)

# Task 3. Create a basic 'while' loop
counter = 0

while counter < 5:
    counter += 1
    print(counter)

# Task 4. Exit a loop using break
counter = 0

while True:
    counter += 1
    if counter > 5:
        break
    print(counter)

# Task 5. Range
print(list(range(6)))  # Output: [0, 1, 2, 3, 4, 5]
print(list(range(0, 6)))  # Output: [0, 1, 2, 3, 4, 5]
print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]

# Task 6. Using range() in a loop
for num in range(0, 11, 2):
    print(num)  # Output: 0, 2, 4, 6, 8, 10

# Exercises 🏋🏻

# Exercise 1. Digits Only!
my_string = 's0m3 str1ng w1th numb3r5'
numbers = '1234567890'

for char in my_string:
    if char in numbers:
        print(char)

# Print the first digit only
for char in my_string:
    if char in numbers:
        print(char)
        break

# Exercise 2. Vowel Counter
quote = "Life is like riding a bicycle. To keep your balance, you MUST keep moving."
vowel_count = 0

for char in quote:
    if char in 'aeiouAEIOU':
        vowel_count += 1

print(f"The number of vowels in the quote is: {vowel_count}")

# Exercise 3. Sum of all Digits
mixed_string = "abc123xyz456"
digits = "0123456789"
found_digits = []

for char in mixed_string:
    if char in digits:
        found_digits.append(int(char))

print(f"The total sum of numbers in the string is: {sum(found_digits)}")

# Exercise 4. Password Strength Checker
passwords = ['Passw0rd', 'hello', 'strongPass1', 'weak']
strong_password_count = 0

for password in passwords:
    if len(password) >= 8:
        strong_password_count += 1

print(f"Number of strong passwords: {strong_password_count}")

# Exercise 5. The Red Crayon
colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]
index = 0

while colors[index] != "Red":
    print(f"Found {colors[index]} crayon. Still looking for Red.")
    index += 1

print("Found the Red crayon!")
