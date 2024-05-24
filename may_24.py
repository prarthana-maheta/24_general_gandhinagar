str1 = "i |m | royl student"

# special methods
str1 = "i am a royal student"
# []

print(str1.split('a'))
print(str1.split(' ',2))
print(str1.split('-')) #not prsent 

print(str1.partition(' '))
print(str1.partition('a'))

# join
print('-'.join('1234567890'))
print(str1.split())
print('-'.join(str1.split()))
# print('-'.join(12345))

str1= "123-456-789----"

print(str1.split('-'))

print(''.join(str1.split('-')))
# outpt="123456789"

# replace

str1="23-34-455"
print(str1.replace('-','*234567890'))

str1="$$$$$$$$$a$  $$$$$$$$$$   a234 6548u$$$$$$$$$$$$$a $$$$$$ $$$$$$$$$$$"
print(str1.strip('$'))