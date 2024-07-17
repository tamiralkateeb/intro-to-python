# Homework Lesson 10 - Workshop - Homework

# Challenge 1: Multiplication of a Three-Digit Number
def multiplication_of_three(number):
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = number % 10
    return digit1 * digit2 * digit3

# Example
print(multiplication_of_three(349))  # Output: 108


# Challenge 2: Sum and Multiplication of Even and Odd Numbers
def sum_even_and_product_odd(arr):
    sum_even = 0
    product_odd = 1
    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            product_odd *= num
    return [sum_even, product_odd]

# Example
print(sum_even_and_product_odd([1, 2, 3, 4]))  # Output: [6, 3]


# Challenge 3: Invert a List of Numbers
def invert_list(arr):
    return [-num for num in arr]

# Example
print(invert_list([1, 5, -2, 4]))  # Output: [-1, -5, 2, -4]


# Challenge 4: Difference Between
def max_diff(arr):
    if len(arr) == 0:
        return 0
    return max(arr) - min(arr)

# Example
print(max_diff([3, 5, 7, 2]))  # Output: 5


# Challenge 5: Sum Between Range Values
def sum_between_range(arr, min_val, max_val):
    return sum(num for num in arr if min_val <= num <= max_val)

# Example
arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
print(sum_between_range(arr, min_val, max_val))  # Output: 25
