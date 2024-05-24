str1="2345678ertyuicvbnm"

# print(str1[10:5:-1])


example = "i am ROYAL student from Gandhinagar BRANCH"

# print(example[2:4].upper())

# ouput : Gandhinagar but in upper case
#         all example string in lower case 
#         ROYAL student --- ROYAL should be lower case and student should be upper case
# print(example[-6:])
# output: ROYAL
#         BRANCH 
#         ROYAL BRANCH

# methods/functions of string 
# 1. casing methods

# captialize()

print(example.capitalize())
print(example.upper())
print(example.lower())
print(example.swapcase())
print(example.title())