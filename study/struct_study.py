import struct
import sys

print('--'*18)
a = 1234
print("a:", a)
print(type(1))
print(id(a))
print(sys.getsizeof(a))

print('--'*18)
b = '\x4f'
print("b:", b)
print(type(b))
print(id(b))
print(sys.getsizeof(b))

b1 = b'\x4f'
print("b1:", b1)
print(type(b1))
print(id(b1))
print(sys.getsizeof(b1))

print('--'*18)
c = 0x4f
print("c:", c)
print(type(c))
print(id(c))
print(sys.getsizeof(c))