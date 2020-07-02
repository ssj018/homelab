import struct
from functools import reduce
import sys
import optparse

def Str_to_Int(string):
	if ord(string[0]) > 90:
		int1 = ord(string[0]) - 87
	else:
		int1 = ord(string[0]) - 48

	if ord(string[1]) > 90:
		int2 = ord(string[1]) - 87
	else:
		int2 = ord(string[1]) - 48
	int_final = int1 * 16 + int2
	return int_final

def Change_MAC_To_Bytes(MAC):
	section1 = Str_to_Int(MAC.split(':')[0])
	section2 = Str_to_Int(MAC.split(':')[1])
	section3 = Str_to_Int(MAC.split(':')[2])
	section4 = Str_to_Int(MAC.split(':')[3])
	section5 = Str_to_Int(MAC.split(':')[4])
	section6 = Str_to_Int(MAC.split(':')[5])
	Bytes_MAC = struct.pack('!6B', section1, section2, section3, section4, section5, section6)
	return Bytes_MAC

if __name__ == "__main__":
    mbytes = Change_MAC_To_Bytes('40:8d:5c:11:fa:1d')
    print(mbytes)