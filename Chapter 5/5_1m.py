"""
Researchers who do quantitative analysis are
often interested in the median of a set of numbers.
Median - the value that is less than half the numbers
in a set and greater than the other half.
"""

fileName = input("Enter the name of a file: ")
f = open(fileName, "r")

# Input the text, convert to numbers, and add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))
numbers.sort()
midpoint = len(numbers) // 2
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint-1]) / 2)