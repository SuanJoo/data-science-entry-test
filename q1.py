# -*- coding: utf-8 -*-
"""q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pg9ls1Sr94xMKvGVfGtvOKwthnwqHIhE
"""

"""
Task 1
  - Create a function that would swap the value of x and y using only x and y as variables.
  - x and y must be numeric.
  - Return -1 if x and y is not numeric, and
  - print the swapped values if both x and y are numeric.
"""
#Answers
x = 11
y = 33
#x and y are swapped without a temporary variable, aka Tuple unpacking
#Technique called assign multiple variables at once using a tuple on the right side of the assignment operator
x, y = y, x
def swap_values(x, y):
    #isinstance function(object, type), object=variable and type must a numeric, numeric=int or flo
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
      # isinstance() function returns True if the specified object is of the
      # specified type, otherwise False -1
      return -1
#Output Print
print("After swapped, value of x is", x)
print("After swapped, value of y is", y)

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
#Answers:
swap("Apple", 10)
swap(9, 17)
print()