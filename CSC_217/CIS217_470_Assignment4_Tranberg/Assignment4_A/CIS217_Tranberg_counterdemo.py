## Program to test the counter program.
# Denise Tranberg
# 7/9/18
# Assignment 4-9.1
#
#  This program demonstrates the Counter class.
#

# Import the Counter class from the counter module. 
from CIS217_Assignment4A_P9_1_Tranberg import Counter

tally = Counter()
tally.reset()

result = tally.getValue()
print("Starting Value:", result)

tally.click()
print ("Adding 1 click")
result = tally.getValue()
print("Value:", result)

tally.click()
print ("\nAdding 1 click")
result = tally.getValue()
print("Value:", result)

tally.undo()
print ("\nUndoing 1 click")
result = tally.getValue()
print("Value:", result)

print ("\nUndoing 1 click")
tally.undo()
result = tally.getValue()
print("Value:", result)

print ("\nUndoing 1 click")
tally.undo()
result = tally.getValue()
print("Value:", result)

print ("\nUndoing 1 click")
tally.undo()
result = tally.getValue()
print("Value:", result)

print ("\nUndoing 1-final click")
tally.undo()
result = tally.getValue()
print("Value:", result)


