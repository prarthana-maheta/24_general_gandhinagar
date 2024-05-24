example = "i a ROYAL student from Gandhinagar BRANCHaA"

# counting method:
# print(example.count('am'))

# # alignment method:

# print(len(example))
# print(example.center(100,"1"))
# print(example.rjust(100,"^"))
# print(example.ljust(100,"8"))


# security method
# sender          cipher text         
# plain text------encryption----- decryption---receiver
# abc             /0x00/01010     plain text

# encode()
print(example)
en=example.encode('UTF-16')
# base64,SHA256 ,SHA512, MD5

print(en.decode('UTF-16'))
print(example.encode('ascii'))


