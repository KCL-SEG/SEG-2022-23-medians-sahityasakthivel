import math
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
print(numbers)

if(len(numbers)% 2 == 0):
    value = int(len(numbers) / 2)
    print((numbers[value] + numbers[value -1])/2)
else:
     print(numbers[math.floor(len(numbers) / 2)])
