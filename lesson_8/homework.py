# Homework Lesson 8 - Workshop - Homework

# Challenge 1: Two Lowest Elements
arr = [5, 2, 9, 1, 5, 6]
arr.sort()
smallest, second_smallest = arr[0], arr[1]
print(smallest, second_smallest)  # Output: 1, 2

# Challenge 2: Remove Spaces
file_name = "My Summer Photos 2023"
new_file_name = ""
for char in file_name:
    if char != " ":
        new_file_name += char
print(new_file_name)  # Output: MySummerPhotos2023

# Challenge 3: Sum of Digits
n = 5
result = 0
for i in range(1, n + 1):
    result += i
print(result)  # Output: 15

# Challenge 4: Isogram
word = "cat"
is_isogram = True
for char in word:
    if word.count(char) > 1:
        is_isogram = False
        break
print(is_isogram)  # Output: True

word = "mom"
is_isogram = True
for char in word:
    if word.count(char) > 1:
        is_isogram = False
        break
print(is_isogram)  # Output: False

# Challenge 5: Repeat Digits
string = "312"
result = ""
for char in string:
    current_num = int(char)
    result += char * current_num
print(result)  # Output: 333122
