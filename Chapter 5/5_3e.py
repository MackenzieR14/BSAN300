# When a for loop is used with a dicionary, the loop's variable is
# bound to each key in an unspecified order.

# To print all of hte keys and their values:
info = {"name":"Sandy", "occupation":"manager"}

for key in info:
    print(key, info[key])

# Alternative: Use the dictionary method items()
print(list(info.items()))

# Access the key and value of each entry in the list within a for loop
for (key, value) in info.items():
    print(key, value)