# The next code segment modifies the previous example
# to handle integers seperated by spaces and/or newlines

f = open("integers.txt", "r")
theSum = 0
lines = f.read()
# for line in f:
wordlist = lines.split()
for word in wordlist:
    number = int(word)
    theSum += number
    print("The sum is", theSum)
    f.close()