# Homework Lesson 13 - Workshop - Homework

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Common Elements Finder
def find_common_elements(list1, list2):
    common = []
    for elem in list1:
        if elem in list2 and elem not in common:
            common.append(elem)
    return common


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1, list2))  # Output: [4, 5]


# Refresher
def find_makeable_recipes(recipes, ingredients):
    makeable_recipes = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe:
            if ingredient not in ingredients:
                can_make = False
                break
        if can_make:
            makeable_recipes.append(recipe)
    return makeable_recipes


# Example usage
test_recipes = [["yeast", "flour"], ["bread", "meat"], ["flour", "meat"]]
test_ingredients = ["yeast", "flour", "meat"]
print(find_makeable_recipes(test_recipes, test_ingredients))


# Challenge 2
# Missing ingredients
def find_missing_ingredients(recipes, ingredients):
    missing_ingredients = []
    for recipe in recipes:
        for ingredient in recipe:
            if ingredient not in ingredients and ingredient not in missing_ingredients:
                missing_ingredients.append(ingredient)
    return missing_ingredients


# Example usage
recipes = [["yeast", "flour"], ["bread", "meat", "flour"]]
ingredients = ["yeast", "bread"]
print(find_missing_ingredients(recipes, ingredients))  # Output: ["flour", "meat"]


# Challenge 3
# The best recipe
def find_best_recipe(recipes, ingredients):
    best_recipe = None
    max_used_ingredients = 0
    for recipe in recipes:
        used_ingredients = [ingredient for ingredient in recipe if ingredient in ingredients]
        if len(used_ingredients) > max_used_ingredients:
            max_used_ingredients = len(used_ingredients)
            best_recipe = recipe
    return best_recipe


# Example usage
recipes = [["yeast", "flour"], ["bread", "meat"], ["flour", "meat", "yeast"]]
ingredients = ["yeast", "flour", "meat", "salt"]
print(find_best_recipe(recipes, ingredients))  # Output: ["flour", "meat", "yeast"]


# Challenge 4
# Find a peak element
def find_peak_element(arr):
    n = len(arr)
    if n < 3:
        return -1
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i
    return -1


# Example usage
arr1 = [1, 3, 20, 4, 1, 0]
print(find_peak_element(arr1))  # Output: 2 (Peak element: 20)

arr2 = [1, 2, 3, 4, 5]
print(find_peak_element(arr2))  # Output: -1 (No peak elements)

arr3 = [5, 10, 20, 15]
print(find_peak_element(arr3))  # Output: 2 (Peak element: 20)


# Challenge 5 (optional)
# Delete duplicates in sorted lists
def delete_duplicates(arr):
    if not arr:
        return arr, 0

    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    return arr, write_index


# Example usage
sorted_list = [1, 2, 2, 3, 4, 4, 4, 5]
print(delete_duplicates(sorted_list))  # Output: ([1, 2, 3, 4, 5, 0, 0, 0], 5)
