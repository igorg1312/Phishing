import binascii
filename = 'img.jpg'
filename1 = 'Test.png'
filename2 = 'aaa.png'
with open(filename, 'rb') as f:
    content = f.read()
c=(binascii.hexlify(content))

with open(filename1, 'rb') as f:
    content = f.read()
b=(binascii.hexlify(content))

with open(filename2, 'rb') as f:
    content = f.read()
a=(binascii.hexlify(content))


print(a)
print(b)
print(c)
print(len(a))
print(len(b))
print(len(c))

