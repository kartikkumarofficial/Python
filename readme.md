The Ultimate Python Guide for Developers
Welcome to the ultimate Python guide! This document serves as a comprehensive, all-in-one reference for Python programming, from the absolute basics to the most advanced concepts. It's designed for both beginners and experienced developers who need a quick refresher.

Table of Contents
Getting Started

Python Fundamentals

Control Flow

Functions

Data Structures

Advanced Concepts

Object-Oriented Programming (OOP)

Advanced OOP Concepts

Working with Files & Modules

Functional Programming

Advanced & Interview-Critical Topics

1. Getting Started
Introduction to Python
Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. It is dynamically-typed and garbage-collected.

Modules
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. We use modules to break down large programs into small, manageable, and organized files.

# math_operations.py
def add(a, b):
    return a + b

# main.py
import math_operations
print(math_operations.add(5, 3)) # Output: 8

Pip
Pip is the package installer for Python. You can use pip to install packages from the Python Package Index (PyPI).

# Install a package
pip install requests

# Uninstall a package
pip uninstall requests

# List installed packages
pip list

2. Python Fundamentals
Comments
Comments are used to explain code and are ignored by the interpreter.

# This is a single-line comment

"""
This is a
multi-line comment
or docstring.
"""

Escape Sequences
Escape sequences are used to insert special characters in strings.

# Newline, Tab, and Backslash
print("Hello\nWorld") # Prints on two lines
print("Hello\tWorld") # Prints with a tab
print("This is a backslash: \\")

Variables
Variables are containers for storing data values.

name = "Alice"  # String
age = 30         # Integer
is_student = True # Boolean

Data Types
Python has various built-in data types:

Text Type: str

Numeric Types: int, float, complex

Sequence Types: list, tuple, range

Mapping Type: dict

Set Types: set, frozenset

Boolean Type: bool

Binary Types: bytes, bytearray, memoryview

Typecasting
Typecasting is converting a variable from one data type to another.

x = "100"
y = int(x) # y is now an integer 100
z = float(y) # z is now a float 100.0

Taking User Input
The input() function is used to get input from the user.

name = input("Enter your name: ")
print(f"Hello, {name}!")

Strings
Strings are sequences of characters, enclosed in single or double quotes.

Slicing
Slicing extracts a portion of a string. string[start:stop:step]

s = "Hello, World!"
print(s[0:5])    # Output: Hello
print(s[7:])     # Output: World!
print(s[::-1])   # Output: !dlroW ,olleH (reverses the string)

String Operations
Strings can be concatenated and repeated.

s1 = "Hello"
s2 = "World"
print(s1 + ", " + s2) # Concatenation: Hello, World
print(s1 * 3)         # Repetition: HelloHelloHello

String Methods
Python provides many useful methods for string manipulation.

s = "  hello world  "
print(s.strip())          # Output: "hello world" (removes whitespace)
print(s.upper())          # Output: "  HELLO WORLD  "
print(s.lower())          # Output: "  hello world  "
print(s.replace("l", "L"))# Output: "  heLLo worLd  "
print("a,b,c".split(',')) # Output: ['a', 'b', 'c']

3. Control Flow
if-else Statements
Used for conditional execution.

age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

match-case Statements
A structural pattern matching statement, available from Python 3.10+.

status = 404
match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case _: # Default case
        print("Something else")

for Loops
Used for iterating over a sequence (like a list, tuple, or string).

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

break and continue
break: Exits the loop entirely.

continue: Skips the current iteration and proceeds to the next.

for i in range(10):
    if i == 5:
        break # Stops when i is 5
    if i % 2 == 0:
        continue # Skips even numbers
    print(i) # Output: 1, 3

4. Functions
Defining a Function
A function is a block of code that only runs when it is called.

def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

greet("Alice") # Call the function

Function Arguments and Parameters
Parameter: The variable listed inside the parentheses in the function definition.

Argument: The value that is sent to the function when it is called.

Types of arguments:

Positional Arguments: Passed in the correct order.

Keyword Arguments: Passed with a key=value syntax.

Default Arguments: Have a default value if none is provided.

Variable-Length Arguments: *args (for non-keyworded variable length argument list) and **kwargs (for keyworded variable length argument list).

def describe_pet(pet_name, animal_type="dog", **other_info):
    print(f"I have a {animal_type} named {pet_name}.")
    for key, value in other_info.items():
        print(f"{key}: {value}")

describe_pet("Willie", owner="John") # Positional, default, and kwargs

f-strings
Formatted string literals (f-strings) provide a concise way to embed expressions inside string literals.

name = "Eric"
age = 74
print(f"Hello, {name}. You are {age} years old.")

Docstrings
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. It is used to document what the code does.

def my_function():
    """This is a docstring. It explains the function's purpose."""
    pass

print(my_function.__doc__)

Recursion
A function that calls itself is recursive.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120

5. Data Structures
Lists
Lists are ordered, mutable (changeable) collections of items.

my_list = [1, "apple", 3.14]
my_list.append("new")    # Add item to the end
my_list.insert(1, "orange") # Insert at index 1
my_list.pop()            # Remove last item
print(my_list)

Tuples
Tuples are ordered, immutable (unchangeable) collections of items.

my_tuple = (1, "apple", 3.14)
print(my_tuple[1]) # Access item

# Tuples are immutable, so this would raise an error:
# my_tuple[1] = "orange"

Sets
Sets are unordered, unindexed collections of unique items.

my_set = {1, 2, 3, 3, 4} # Duplicates are removed
print(my_set) # Output: {1, 2, 3, 4}
my_set.add(5)
my_set.remove(2)

Dictionaries
Dictionaries are unordered collections of key-value pairs. They are mutable.

my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"]) # Access value by key
my_dict["city"] = "New York" # Add a new key-value pair
my_dict.pop("age") # Remove a key-value pair
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

6. Advanced Concepts
for Loop with else
The else block executes after the for loop completes normally (i.e., not terminated by a break statement).

for i in range(5):
    print(i)
else:
    print("Loop finished without a break.")

Exception Handling (try...except...finally)
Used to handle errors gracefully.

try: Code that might raise an exception.

except: Code that runs if an exception occurs.

finally: Code that always runs, regardless of an exception.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution finished.")

Raising Custom Errors
You can raise your own exceptions using the raise keyword.

x = -1
if x < 0:
    raise ValueError("Number cannot be negative")

List/Dict/Set Comprehensions
A concise way to create lists, dictionaries, or sets.

# List comprehension
squares = [i**2 for i in range(5)] # [0, 1, 4, 9, 16]

# Dict comprehension
square_dict = {i: i**2 for i in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

Short Hand if-else (Ternary Operator)
A one-liner for an if-else statement.

age = 20
message = "Adult" if age >= 18 else "Minor"
print(message)

enumerate Function
Used to get both the index and value of an item in a sequence.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

Virtual Environments (venv)
A self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

# Create a virtual environment
python -m venv myenv

# Activate it (on Windows)
myenv\Scripts\activate

# Activate it (on Unix or MacOS)
source myenv/bin/activate

# Deactivate
deactivate

The if __name__ == "__main__" block
This code block is executed only when the Python script is run directly, not when it is imported as a module.

# my_module.py
def some_function():
    print("Function is running.")

if __name__ == "__main__":
    print("This script is being run directly.")
    some_function()

7. Object-Oriented Programming (OOP)
OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods).

Classes and Objects
Class: A blueprint for creating objects.

Object: An instance of a class.

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor / Initializer
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return "Woof!"

# Create an object (instance) of the Dog class
my_dog = Dog("Buddy", 3)
print(f"{my_dog.name} is {my_dog.age} years old.")
print(my_dog.bark())

Constructors (__init__)
The __init__ method is a special method that is called when an object is created. It is used to initialize the object's attributes.

Decorators
A decorator is a function that takes another function and extends its behavior without explicitly modifying it.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

Getters and Setters
Methods used to control access to an object's attributes. Often implemented using @property.

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """This is the 'getter' method."""
        return self._value

    @value.setter
    def value(self, new_value):
        """This is the 'setter' method."""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

obj = MyClass(10)
print(obj.value) # Getter
obj.value = 20   # Setter

Inheritance
A mechanism where a new class inherits attributes and methods from an existing class.

Single Inheritance: A class inherits from one superclass.

Multiple Inheritance: A class inherits from multiple superclasses.

Multilevel Inheritance: A class inherits from a derived class, forming a chain.

Hierarchical Inheritance: Multiple classes inherit from a single superclass.

Hybrid Inheritance: A combination of two or more types of inheritance.

# Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

# Child class
class Dog(Animal):
    def bark(self):
        return "Dog barks"

d = Dog()
print(d.speak()) # Inherited from Animal
print(d.bark())

Access Modifiers
Python doesn't have strict access modifiers like public, private, or protected. Instead, it uses naming conventions:

Public: Accessible from anywhere. (e.g., name)

Protected: Should only be accessed within the class and its subclasses. (prefix with _, e.g., _name)

Private: Should only be accessed within the class. (prefix with __, e.g., __name)

8. Advanced OOP Concepts
Static Methods
A method that belongs to the class rather than an instance of the class. It doesn't take self or cls as the first parameter.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3)) # Called on the class

Class Methods
A method that is bound to the class and not the object of the class. It takes cls as the first parameter. Often used as alternative constructors.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)

person = Person.from_birth_year("Alice", 1990)
print(person.age)

super()
A function that allows a subclass to call methods of its superclass.

class Parent:
    def show(self):
        print("Parent's show method")

class Child(Parent):
    def show(self):
        super().show() # Calls the parent's show method
        print("Child's show method")

c = Child()
c.show()

Magic/Dunder Methods
Special methods with double underscores at the beginning and end of their names (e.g., __init__, __str__). They allow you to emulate the behavior of built-in types.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self): # Called by print() or str()
        return f"{self.title} by {self.author}"

    def __len__(self): # Called by len()
        return len(self.title)

book = Book("The Hobbit", "J.R.R. Tolkien")
print(book) # Output: The Hobbit by J.R.R. Tolkien
print(len(book)) # Output: 10

Operator Overloading
Defining how operators (+, -, *, etc.) work with your custom objects by implementing dunder methods (__add__, __sub__, etc.).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 4)
v2 = Vector(3, 5)
v3 = v1 + v2
print(v3.x, v3.y) # Output: 5 9

9. Working with Files & Modules
File I/O
Reading from and writing to files.

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a new line.")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()      # Reads the entire file
    # content = f.readline()  # Reads a single line
    # content = f.readlines() # Reads all lines into a list
print(content)

seek() and tell()
tell(): Returns the current position of the file cursor.

seek(): Changes the position of the file cursor.

with open("example.txt", "r") as f:
    print(f.tell()) # 0
    f.read(5)       # Read 5 characters
    print(f.tell()) # 5
    f.seek(0)       # Go back to the beginning
    print(f.tell()) # 0

OS Module
Provides a way of using operating system dependent functionality.

import os

print(os.getcwd()) # Get current working directory
# os.mkdir("new_dir") # Create a directory
# os.rename("old.txt", "new.txt") # Rename a file
print(os.path.exists("example.txt")) # Check if a file exists

Shutil Module
Offers high-level file operations.

import shutil

# Copy a file
shutil.copy("source.txt", "destination.txt")

# Move a file
shutil.move("source.txt", "new_folder/source.txt")

Requests Module
A simple, yet elegant, HTTP library.

import requests

response = requests.get("https://api.github.com")
print(response.status_code) # 200
print(response.json())      # Parse JSON response

10. Functional Programming
Lambda Functions
Small anonymous functions defined with the lambda keyword.

add = lambda a, b: a + b
print(add(5, 3)) # Output: 8

map()
Applies a function to all the items in an input list.

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared) # Output: [1, 4, 9, 16]

filter()
Creates a list of items for which a function returns true.

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # Output: [2, 4, 6]

reduce()
A function that performs a repetitive operation over the pairs of the list. (Located in functools module).

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Output: 24

11. Advanced & Interview-Critical Topics
is vs ==
==: Checks if the values of two operands are equal.

is: Checks if two variables point to the same object in memory.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) # True (values are the same)
print(a is b) # False (different objects in memory)
print(a is c) # True (same object in memory)

Walrus Operator :=
Assignment expressions, introduced in Python 3.8. It assigns a value to a variable as part of a larger expression.

# Old way
n = len([1, 2, 3])
if n > 2:
    print(f"List is too long ({n} elements, expected <= 2)")

# With walrus operator
if (n := len([1, 2, 3])) > 2:
    print(f"List is too long ({n} elements, expected <= 2)")

Generators
A special type of iterator, created using a function with the yield keyword. They generate items one at a time and only when required, making them very memory efficient.

def my_generator(n):
    for i in range(n):
        yield i**2

for num in my_generator(5):
    print(num) # 0, 1, 4, 9, 16

Function Caching
Memoization technique to store the results of expensive function calls and return the cached result when the same inputs occur again.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def heavy_computation(n):
    time.sleep(2) # Simulate a slow function
    return n * n

print(heavy_computation(5)) # Takes 2 seconds
print(heavy_computation(5)) # Returns instantly from cache

Regular Expressions (re module)
Used for pattern matching in strings.

import re

text = "The rain in Spain"
# Find all occurrences of "ai"
matches = re.findall("ai", text)
print(matches) # Output: ['ai', 'ai']

# Search for the first white-space character
search = re.search(r"\s", text)
print(f"First white-space at position: {search.start()}")

Multithreading vs Multiprocessing
Multithreading: Running multiple threads (smaller units of a process) in parallel within the same process. Good for I/O-bound tasks. Subject to the Global Interpreter Lock (GIL).

Multiprocessing: Running multiple processes in parallel. Each process has its own memory space and interpreter. Good for CPU-bound tasks. Bypasses the GIL.

# Example of Multithreading
import threading

def task(name):
    print(f"Running task: {name}")

threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join() # Wait for all threads to complete

AsyncIO
A library to write concurrent code using the async/await syntax. It's a single-threaded, single-process design that uses an event loop. Ideal for high-performance I/O-bound applications.

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())

Creating a Command-Line Utility
Using modules like argparse to create professional command-line tools.

# cli_tool.py
import argparse

parser = argparse.ArgumentParser(description="A simple CLI tool.")
parser.add_argument("message", help="The message to display.")
parser.add_argument("-c", "--capitalize", help="Capitalize the message", action="store_true")

args = parser.parse_args()

output = args.message
if args.capitalize:
    output = output.upper()

print(output)

# Run from terminal:
# python cli_tool.py "hello world" -c
# Output: HELLO WORLD
