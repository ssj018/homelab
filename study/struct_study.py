import struct

a = 1234

bin_a = struct.pack('h',a)
bin_a = struct.pack('i',a)

print(bin_a)