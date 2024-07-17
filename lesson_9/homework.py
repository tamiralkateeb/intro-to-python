# HOMEWORK: Functions

# Basic Function
def say_hello():
    print("Hello")

say_hello()

# Basic Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Basic Function with Default Values
def greeting(name="stranger"):
    print(f"Hello, {name}!")

greeting()
greeting('Tom')

# Multiple Parameters
def add(a, b=0):
    print(f"The sum of {a} + {b} = {a + b}")

add(1, 2)
add(1)

# Parameters out of order
def full_name(first_name, last_name):
    print(f"{first_name} {last_name}")

full_name("Nelson", "Mandela")
full_name(first_name="Mandela", last_name="Nelson")

# Returning Values
def is_longer_than_8(word):
    return len(word) > 8

words = ["apple", "banana", "strawberry", "grape"]
for word in words:
    if is_longer_than_8(word):
        print(f"{word} is longer than 8 characters")

# FizzBuzz
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

for i in range(1, 21):
    print(fizzbuzz(i))

# Anagram
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

test_str1 = 'abcde'
test_str2 = 'edcba'
print(is_anagram(test_str1, test_str2))  # Output: True

# Find Max number
def find_max(numbers):
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result

numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
print(find_max(numbers))  # Output: 12

# Even/Odd Checker Function
def is_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even_odd(1)
is_even_odd(10)
is_even_odd(5)
is_even_odd(9)
