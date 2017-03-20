"""
Write a program to calculate the average age of a group of people,
of unknown size
Use a negative number as the 'sentinel' (when to stop)
"""

total = 0
age = int(input("Age: "))
while age >= 0:
    total += age
    age = int(input("Age: "))

print("Total age is {}".format(total))
