### **Python Template: Introduction and Applied Linear Algebra with NumPy**

# Part 0: Very Basics of Python

# Introduction to basic data types: int, float, string
# An integer (int) is a whole number
my_int = 5
print("This is an integer:", my_int)

# A float is a number with a decimal point
my_float = 5.75
print("This is a float:", my_float)

# A string is a sequence of characters enclosed in quotes
my_string = "Hello, world!"
print("This is a string:", my_string)

# Using the input function to get user input
# input() reads user input as a string
user_input = input("Enter something: ")
print("You entered:", user_input)

# To convert user input to int or float, use int() or float() function
user_number = float(input("Enter a number: "))
print("You entered the number:", user_number)

# Part 1: Introduction to Python

# Basic Syntax and Operations

# Example 1: Convert temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Formula: (Celsius * 9/5) + 32 = Fahrenheit
    return (celsius * 9/5) + 32

# Example usage
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c} Celsius is {temp_f} Fahrenheit")

# Example 2: Calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"Factorial of {num} is {factorial(num)}")

# Data Structures

# Example 1: List of the first ten prime numbers and a function to check if a number is prime
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
test_num = 11
print(f"Is {test_num} a prime number? {is_prime(test_num)}")

# Example 2: Dictionary that maps student names to their grades
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

def add_student(name, grade):
    grades[name] = grade

def average_grade():
    return sum(grades.values()) / len(grades)

# Example usage
add_student("David", 90)
print(f"Average grade: {average_grade()}")

# Part 2: Introduction to NumPy

import numpy as np

# Getting Started with NumPy

# Example 1: Create a NumPy array of the first 20 even numbers
even_numbers = np.arange(2, 41, 2)
print("First 20 even numbers:", even_numbers)

# Example 2: Element-wise operations on NumPy arrays
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

print("Element-wise addition:", array1 + array2)
print("Element-wise subtraction:", array1 - array2)
print("Element-wise multiplication:", array1 * array2)

# Linear Algebra with NumPy

# Example 1: Dot product of two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

dot_product = np.dot(vector1, vector2)
print("Dot product:", dot_product)

# Example 2: Create a 3x3 matrix and compute its determinant
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

determinant = np.linalg.det(matrix)
print("Determinant of the matrix:", determinant)

# Example 3: Solve a system of linear equations
# System of equations:
# 2x + 3y = 8
# x - y = 2
A = np.array([[2, 3], [1, -1]])
b = np.array([8, 2])

solution = np.linalg.solve(A, b)
print("Solution to the system of equations:", solution)

# Applied Linear Algebra Example: Line of Best Fit (Least Squares Method)

import matplotlib.pyplot as plt

# Sample dataset
points = np.array([[1, 2], [2, 3], [3, 5], [4, 4], [5, 5]])

# Extracting X and y values
X = points[:, 0]
y = points[:, 1]

# Adding a column of ones to X for the intercept term
X_b = np.c_[np.ones((len(X), 1)), X]

# Using the normal equation to compute the coefficients (beta)
beta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Print the coefficients
print("Coefficients (beta):", beta)

# Plotting the points and the line of best fit
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, X_b.dot(beta), color='red', label='Line of best fit')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
