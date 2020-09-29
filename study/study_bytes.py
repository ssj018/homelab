#! /usr/bin/env python3

def write_bytes(bytesstr):
    with open('/tmp/test.bin','wb') as f:
        f.write(bytesstr)

def write_str(str):
    with open('/tmp/test','w') as f:
        f.write(str)

a = b'hello, world!' #bytes: use ascii-code to  encode, can not store non-ascii characters.
b = '你好, world'    # str:   use unicode(utf-8) to  encode, can store non-ascii characters.
'''
Bytes一般来自网络读取的数据、从二进制文件（图片等）读取的数据、以二进制模式读取的文本文件(.txt, .html, .py, .cpp等)。
'''

#write_bytes(d)
#write_str(c)
