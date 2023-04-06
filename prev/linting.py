"""This file shows example linting errors"""
MY_VARIABLE = 1


class MyClass:
    def __init__(self):
        self.my_variable = 1


from dataclasses import dataclass


def divide_numbers(a: int, b: float) -> float:
    """
    Return the quotient of a and b.

    Args:
        a (str): the numerator
        b (float): the denominator

    Returns:
        int: the quotient of a and b
    """  # noqa: DAR203
    return a / b


@dataclass
class Book:
    title: str
    num_pages: int
    author: str
    isbn: str
    location_of_writing: str
    genre: str
    rating: float
    weight: int
    price: float
    is_in_series: str
    aaa: int
    aab: int
    aac: int
    aad: int
    aae: int
    aaf: int


my_string = (
    "This is a very long string that should be split"
    + " into multiple lines to avoid pylint error C0301"
)


my_string = "Hello, World!   "


my_variable = 1


def my_function():
    print("Hello, World!")


if True:
    print("Hello, World!")
    print("Hello, World!")


class MyClass:
    def __init__(self):
        self.my_variable = 1


my_class = MyClass()
print(my_class.my_variable_does_not_exist)


def my_function(my_variable):
    print(my_variable)


my_function()


def my_function(my_variable):
    print(my_variable)


my_function(my_variable=1)


class MyClass:
    def my_method(self, my_variable):
        print(my_variable)


my_class = MyClass()
my_class.my_method()


my_variable = 1
for i in my_variable:
    print(i)


my_variable = 1
print(my_variable[0])


my_variable = 1
my_string = "Hello, World!"
print(my_variable + my_string)


my_string = "Hello, World!"
print(f"{my_string} {1}")


my_variable = 1
my_variable_2 = 2


try:
    my_variable = 1 / 0
except:
    pass


def my_function():
    pass


my_string = "Hello, World!   "


my_variable = 1


import os
import sys


from __future__ import print_function


def my_function():
    pass


if True:
    import os


class MyClass:
    def __init__(self):
        self.my_variable = 1


my_class = MyClass()
print(my_class.my_variable_does_not_exist)


def my_function(my_variable):
    print(my_variable)


my_function()


def my_function(my_variable):
    print(my_variable)


class MyClass:
    def my_method(self, my_variable):
        print(my_variable)


my_class = MyClass()
my_class.my_method()


my_variable = 1
for i in my_variable:
    print(i)


my_variable = 1
print(my_variable[0])


my_variable = 1
my_string = "Hello, World!"
print(my_variable + my_string)


my_string = "Hello, World!"
print(f"{my_string} {1}")


my_variable = 1
print(my_variable_does_not_exist)


my_variable = 1


my_variable = 1
print(my_variable_does_not_exist)


try:
    ...
except:
    ...

my_variable = 1
print(my_variable_does_not_exist)
