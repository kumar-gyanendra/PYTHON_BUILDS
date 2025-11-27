# 6. Write a python program to display a user entered name followed by Good Afternoon using input () function. 

#Solution

#method 1
'''a = input("Enter name: ")
print("Good Afternoon", a)''' 

# Method 2(Fastest)
a = input("Enter name: ")
print(f"Good Afternoon {a}")

# REMEMBER
# An f-string (formatted string literal) is a way to create strings in Python that let you easily insert variables or expressions directly inside the string. They start with the letter f before the opening quote.

# Why use f-strings?
# 1)They are easy to read
# 2)Faster than older formatting methods
# 3)Allow expressions inside { }

# method3   (This is very traditional way, no need to remember this, just wrote here for information)
'''a = input("Enter name: ")
print("Good Afternoon"+ a + "")'''