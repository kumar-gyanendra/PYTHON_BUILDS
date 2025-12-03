# 10. Write a program to store seven fruits in a list entered by the user. 

#Solution

#Method1
'''
fruits = []
f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)
f5 = input("Enter Fruit name: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)
f7 = input("Enter Fruit name: ")
fruits.append(f7)

print(fruits)
'''

#Method2
fruits = []
f1 = input("Enter Fruit name: ")
fruits.insert(0, f1)
f2 = input("Enter Fruit name: ")
fruits.insert(1, f2)
f3 = input("Enter Fruit name: ")
fruits.insert(2, f3)
f4 = input("Enter Fruit name: ")
fruits.insert(3, f4)
f5 = input("Enter Fruit name: ")
fruits.insert(4, f5)
f6 = input("Enter Fruit name: ")
fruits.insert(5, f6)
f7 = input("Enter Fruit name: ")
fruits.insert(6, f7)

print(fruits)


'''
EXPLANATION

1) This program stores seven fruits entered by the user into a list.
2) Method 1 uses append() to add fruits at the end of the list.
3) Method 2 uses insert() to add fruits at specific positions in the list.
4) Finally, it prints the complete list of fruits.
'''