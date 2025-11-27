# 8. Write a program to detect double space in a string.

# Solution
name = "Harry is a good boy and "
print(name.find("  "))

# output = -1
# Returns the position of the first double space, or -1 if not found.

name = "Harry is a good boy  and  "
print(name.find("  "))

# Replace the double space from problem 8 with single spaces.
print(name.replace("  "," "))