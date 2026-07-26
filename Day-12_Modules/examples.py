# ================================
# Day 12 - Modules & Packages
# examples.py
# ================================

# --------------------------------
# Example 1: Import Entire Module
# --------------------------------

import math

print("----- Example 1 -----")
print("Value of PI :", math.pi)
print("Square Root of 64 :", math.sqrt(64))
print()


# --------------------------------
# Example 2: Import Specific Function
# --------------------------------

from math import factorial, sqrt

print("----- Example 2 -----")
print("Factorial of 5 :", factorial(5))
print("Square Root of 100 :", sqrt(100))
print()


# --------------------------------
# Example 3: Import with Alias
# --------------------------------

import math as m

print("----- Example 3 -----")
print("Value of e :", m.e)
print("2 raised to 5 :", m.pow(2, 5))
print()


# --------------------------------
# Example 4: Random Module
# --------------------------------

import random

print("----- Example 4 -----")
print("Random Number :", random.randint(1, 100))

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Random Fruit :", random.choice(fruits))

random.shuffle(fruits)

print("Shuffled List :", fruits)
print()


# --------------------------------
# Example 5: Datetime Module
# --------------------------------

from datetime import datetime

print("----- Example 5 -----")

current = datetime.now()

print("Current Date & Time :", current)
print("Year :", current.year)
print("Month :", current.month)
print("Day :", current.day)
print()


# --------------------------------
# Example 6: Date Only
# --------------------------------

from datetime import date

print("----- Example 6 -----")
print("Today's Date :", date.today())
print()


# --------------------------------
# Example 7: Time Module
# --------------------------------

import time

print("----- Example 7 -----")
print("Current Timestamp :", time.time())
print()


# --------------------------------
# Example 8: OS Module
# --------------------------------

import os

print("----- Example 8 -----")
print("Current Working Directory :")
print(os.getcwd())
print()


# --------------------------------
# Example 9: Sys Module
# --------------------------------

import sys

print("----- Example 9 -----")
print("Python Version :")
print(sys.version)
print()


print("========== End of Examples ==========")