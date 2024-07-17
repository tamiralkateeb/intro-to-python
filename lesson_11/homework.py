# HOMEWORK: Dictionaries

# Basic Dictionary
# Create an empty dictionary and then add a few of your friends.
friends_dict = {}
friends_dict['john@example.com'] = 'John'
friends_dict['jane@example.com'] = 'Jane'
friends_dict['doe@example.com'] = 'Doe'

# Pre-populated dictionary
friends_dict_prepopulated = {
    'john@example.com': 'John',
    'jane@example.com': 'Jane',
    'doe@example.com': 'Doe'
}

# Nested Dictionary
# Create a nested dictionary for a list of 5 company employees.
employees = {
    1: {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    2: {'name': 'Bob', 'department': 'IT', 'salary': 60000},
    3: {'name': 'Charlie', 'department': 'Finance', 'salary': 55000},
    4: {'name': 'David', 'department': 'IT', 'salary': 70000},
    5: {'name': 'Eve', 'department': 'Marketing', 'salary': 45000}
}

# Accessing Values
# Print list of employee IDs
print(list(employees.keys()))  # Output: [1, 2, 3, 4, 5]

# Print employee data for employee with ID 3
print(employees[3])  # Output: {'name': 'Charlie', 'department': 'Finance', 'salary': 55000}

# Loop over employees and print names and salaries
for emp_id, emp_info in employees.items():
    print(f"Name: {emp_info['name']}, Salary: {emp_info['salary']}")

# Updating Values
salaries = {
    'james': 10000,
    'tom': 15000,
    'ryan': 16000,
    'julia': 17000
}

# Increase everyone's salary by 1,000 and add Joseph
for key in salaries.keys():
    salaries[key] += 1000
salaries.update({'joseph': 18000})

print(salaries)  # Output: {'james': 11000, 'tom': 16000, 'ryan': 17000, 'julia': 18000, 'joseph': 18000}

# Deleting Values
# Remove Julia from salaries
del salaries['julia']

print(salaries)  # Output: {'james': 11000, 'tom': 16000, 'ryan': 17000, 'joseph': 18000}

# Iterating over Dictionaries
films = {
    2016: "Star Wars: Episode VII - The Force Awakens",
    2017: "Star Wars: Episode VIII - The Last Jedi",
    2018: "Black Panther",
    2019: "Avengers: Endgame",
    2020: "Bad Boys for Life"
}

# Is Black Panther in the list of movies?
print("Black Panther" in films.values())  # Output: True

# Is there any movie for the year 2021?
print(2021 in films.keys())  # Output: False

# Print year, title, and position
for i, (year, title) in enumerate(films.items(), 1):
    print(f"{i}. {year}: {title}")

# Exercise 1: Animal Shelter Volunteer
shelter_pets = {
    'Whiskers': {'Age': 2, 'Type': 'Cat', 'Adopted': False},
    'Fido': {'Age': 4, 'Type': 'Dog', 'Adopted': True},
    'Patch': {'Age': 1, 'Type': 'Dog', 'Adopted': False},
    'Snowball': {'Age': 3, 'Type': 'Rabbit', 'Adopted': True}
}

# Access and print the age of Whiskers
print(shelter_pets['Whiskers']['Age'])  # Output: 2

# Access and print if Patch is a dog or cat
print(shelter_pets['Patch']['Type'])  # Output: Dog

# Access and print if Snowball is adopted or not
print(shelter_pets['Snowball']['Adopted'])  # Output: True

# Find out which pets are not yet adopted and print their names
for pet, info in shelter_pets.items():
    if not info['Adopted']:
        print(pet)  # Output: Whiskers, Patch

# Exercise 2: Best-Selling Books
best_selling_books = {
    1997: "Harry Potter and the Philosopher's Stone",
    1984: "Neuromancer",
    2003: "The Kite Runner",
    2015: "Go Set a Watchman"
}

# Update the title for 1997
best_selling_books[1997] = "Harry Potter and the Sorcerer's Stone"

# Update multiple titles at once
best_selling_books.update({
    1984: "The Hunt for Red October",
    2003: "The Da Vinci Code"
})

# Delete the book published in 2015
del best_selling_books[2015]

# Print the updated dictionary
print(best_selling_books)

# Exercise 3: Manage Music Collection
dylan_albums = {
    1962: "Bob Dylan",
    1963: "The Freewheelin' Bob Dylan",
    1975: "Blood on the Tracks",
    1997: "Time Out of Mind"
}

# Print all the release years
for year in dylan_albums.keys():
    print(year)

# Print all the album names
for album in dylan_albums.values():
    print(album)

# Print both the release years and album names together
for year, album in dylan_albums.items():
    print(f"{year}: {album}")

# Check if a particular year or album exists in the collection
print(1962 in dylan_albums.keys())  # Output: True
print("Blood on the Tracks" in dylan_albums.values())  # Output: True

# Exercise 4: Remove Duplicates
person = {
    'first': 'Jeff',
    'name': 'Jeff',
    'last': 'Smith',
    'last_name': 'Smith',
    'state': 'CA',
    'age': 55
}

# Remove duplicates
result = {}
for key, value in person.items():
    if value not in result.values():
        result[key] = value

print(result)  # Output: {'first': 'Jeff', 'last': 'Smith', 'state': 'CA', 'age': 55}

# Exercise 5: Find the Highest Score
def find_max_score(scores_dict):
    max_score = 0
    result = {}
    for name, score in scores_dict.items():
        if score >= max_score:
            max_score = score
            result = {name: score}
    return result

test_scores = {
    'James': 83,
    'Julia': 91,
    'Ryan': 90,
    'Maria': 80,
    'David': 79,
    'Adam': 96,
    'Jennifer': 97,
    'Susan': 77
}

print(find_max_score(test_scores))  # Output: {'Jennifer': 97}
