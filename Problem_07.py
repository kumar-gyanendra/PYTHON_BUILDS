# 7. Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''

#Solution
print(letter.replace("<|Name|>", "Gyanendra").replace("<|Date|>", "21 November 2025"))