"""
All of the functions and methods examined in previous chapters return
a value that the caller can then use to complete its work.
Mutator methods (eg., insert, append, extend, pop, sort, and remove) usually
return no value of interest to the caller.
"""

aList = [4, 2, 10, 8]
aList = aList.sort()
print(aList)  # Output: None

name = "Bill"
name = name.replace("i", "a")
print(name)   # Output: Ball