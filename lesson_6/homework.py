# Homework: Lists

# Task 1. Create three lists
list_1 = []
list_1.append('Friend1')
list_1.append('Friend2')
list_1.append('Friend3')

list_2 = ['Friend1', 'Friend2', 'Friend3']

list_3 = [
    ['Friend1', 25],
    ['Friend2', 30],
    ['Friend3', 27],
]

# Task 2. Retrieve elements from a List
second_friend_name = list_2[1]
print(second_friend_name)  # Output: Friend2

last_friend_age = list_3[-1][1]
print(last_friend_age)  # Output: 27

# Task 3. Remove elements from a List
cities = ["Houston", "Dallas", "Austin"]
fruits = ["apple", "banana", "orange"]

cities.remove("Austin")
print(cities)  # Output: ["Houston", "Dallas"]

del fruits[-1]
print(fruits)  # Output: ["apple", "banana"]

# Task 4. Verify if an element exists in a list
pantry = ["ham", "bread", "cheese"]

if "cheese" in pantry:
    print('YES')  # Output: YES

# Task 5. Sorting and Reversing
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [2, 6, 9, 9, 11, 17, 32, 34, 57]

reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  # Output: [32, 9, 57, 11, 2, 9, 17, 34, 6]

numbers.sort()
print(numbers)  # Output: [2, 6, 9, 9, 11, 17, 32, 34, 57]

numbers.reverse()
print(numbers)  # Output: [57, 34, 32, 17, 11, 9, 9, 6, 2]

# Task 6. Stitching and Slicing
work_days = ['mon', 'tue', 'wed', 'thu', 'fri']
rest_days = ['sat', 'sun']

full_week = work_days + rest_days
print(full_week)  # Output: ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

print(full_week[:5])  # Output: ['mon', 'tue', 'wed', 'thu', 'fri']

# Task 7. Aggregators and Helpers
numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

print(min(numbers))  # Output: 2
print(max(numbers))  # Output: 57
print(sum(numbers))  # Output: 177
print(numbers.count(9))  # Output: 2
print(len(numbers))  # Output: 9

# Exercise 1. The Biography Creator
user_data = []

name = input("Name: ")
age = input("Age: ")
city = input("City: ")

user_data.append(name)
user_data.append(age)
user_data.append(city)

biography = f"My name is {user_data[0]}, I'm {user_data[1]} years old and I was born in {user_data[2]}."
print(biography)

# Exercise 2. The Card Deck
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
faces = ['J', 'Q', 'K']

card_deck = numbers + faces

print(card_deck[:6])  # Output: ['1', '2', '3', '4', '5', '6']
print(card_deck[-3:])  # Output: ['J', 'Q', 'K']
print(card_deck[-3:])  # Output: ['J', 'Q', 'K']
print(card_deck[1:-1])  # Output: ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q']
print(card_deck[::3])  # Output: ['1', '4', '7', '10', 'K']
print(card_deck[1:10:2])  # Output: ['2', '4', '6', '8', '10']

# Exercise 3. The Steps Tracker
monday = int(input('Steps for Monday: '))
tuesday = int(input('Steps for Tuesday: '))
wednesday = int(input('Steps for Wednesday: '))
thursday = int(input('Steps for Thursday: '))
friday = int(input('Steps for Friday: '))
saturday = int(input('Steps for Saturday: '))
sunday = int(input('Steps for Sunday: '))

steps = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

print(steps[2])  # Output: steps for Wednesday

work_days_steps = steps[:5]
print(sum(work_days_steps))  # Output: sum of steps from Monday to Friday

print(sum(steps))  # Output: sum of steps for the entire week

print(min(steps))  # Output: minimum steps in a day

print(max(steps))  # Output: maximum steps in a day

# Exercise 4. The Speech Reverser and Counter
user_input = input('Give me a phrase: ')

words = user_input.split()

reversed_words = list(reversed(words))
print(reversed_words)  # Output: list of words in reverse order

print(len(words))  # Output: number of words
