# A for loop can be used to read
# one line at a time from a file

f = open("myfile.txt", "r")
for line in f:
    print(line)
f.close()
