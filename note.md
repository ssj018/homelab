## mysql

### select the last 3 minutes data from database
- select SysLogTag,Message from SystemEvents where DeviceReportedTime > now()-interval 3 minute;
- select count(1) from myTable where Login_time > date_sub(now(), interval 3 minute)
- select * from myTable where Login_time > select max(time) - interval 3 minute ;(This query will work even if your table is not updated...) 

### create remote user
#### create
- CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';
- CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';

#### grant 
- GRANT ALL ON *.* TO 'myuser'@'localhost';
- GRANT ALL ON *.* TO 'myuser'@'%';
- GRANT SELECT, INSERT, UPDATE ON Syslog.* TO user1;
- flush privileges;

## git

### git push local branch to remote master
- git push origin  HEAD:master



## python
### str and bytes
1. To store anything in a computer, you must first encode it, i.e. convert it to bytes. For example:

- If you want to store music, you must first encode it using MP3, WAV, etc.
- If you want to store a picture, you must first encode it using PNG, JPEG, etc.
- If you want to store text, you must first encode it using ASCII, UTF-8, etc.

MP3, WAV, PNG, JPEG, ASCII and UTF-8 are examples of encodings. An encoding is a format to represent audio, images, text, etc in bytes.

2. human can not read/write by bytes. so every software we used  should decode byte to str for read and encode str to byte for write in computer

3. when we use python read or store `str`, python will auto encode/decode for us


```
>>> a = "a"
>>> a
'a'
>>> type(a)
<class 'str'>

>>> b = "禅"
>>> b
'禅'
>>> type(b)
<class 'str'>
```

4 python3 has a class `bytes` to define a data as bytes type, when use `bytes` means tell python do not auto encode/decode , we deal with it by ourself.
```
>>> c = b'a'
>>> c
b'a'
>>> type(c)
<class 'bytes'>

>>> d = b'\xe7\xa6\x85'
>>> d
b'\xe7\xa6\x85'
>>> type(d)
<class 'bytes'>
>>>

>>> e = b'禅'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
```
**In Python, a byte string is represented by a b, followed by the byte string's ASCII representation.If the bytes is out of ASCII, it will represent by hexadecimal data of the byes**
To  define a bytes type data, just add `b` before the object.The bytes type can be characters in the ASCII range and other hexadecimal  data

### data(bin, oct ,hex, decimal)
- represent:
```
bin: 0b1
oct: 0o1
hex: 0x1
dec: 0d1
```
- data type: The same data in different bases is the same in memory (address, size, type)
```
import sys
import prettytable as pt



mydict = {
    '1': 1,
    '0b1': 0b1,
    '0o1': 0o1,
    '0x1': 0x1,
    'int(\'f\',16)': int('f',16),
    'hex(int(\'17\',8))': hex(int('17',8)),
    '0xe7': 0xe7,
    '\'\\xe7\'': '\xe7',
    'b\'xe7\'': b'xe7'
}




if __name__ == "__main__":
    tb = pt.PrettyTable()
    tb.field_names= ["Expression","Value","Type","Memort address","Memory size"]
    for i in mydict:
        tb.add_row([i, mydict[i], type(mydict[i]), id(mydict[i]), sys.getsizeof(mydict[i])])

    print(tb)


output:
+------------------+--------+-----------------+-----------------+-------------+
|    Expression    | Value  |       Type      |  Memort address | Memory size |
+------------------+--------+-----------------+-----------------+-------------+
|        1         |   1    |  <class 'int'>  |     10914496    |      28     |
|       0b1        |   1    |  <class 'int'>  |     10914496    |      28     |
|       0o1        |   1    |  <class 'int'>  |     10914496    |      28     |
|       0x1        |   1    |  <class 'int'>  |     10914496    |      28     |
|   int('f',16)    |   15   |  <class 'int'>  |     10914944    |      28     |
| hex(int('17',8)) |  0xf   |  <class 'str'>  | 139754689103440 |      52     |
|       0xe7       |  231   |  <class 'int'>  |     10921856    |      28     |
|      '\xe7'      |   ç    |  <class 'str'>  | 139754720157328 |      74     |
|      b'xe7'      | b'xe7' | <class 'bytes'> | 139754689154264 |      36     |
+------------------+--------+-----------------+-----------------+-------------+
```
- convert
   - to dec(int()):
   ```
   >>> int('f',16) 
   15
   >>> int('10100111110',2)      
   1342
   >>> int('17',8)    
   15
   ```
   - to hex(hex()):
   ```
   >>> hex(1033)
   '0x409'
   >>> hex(int('101010',2)) #convert to decimal first
   '0x2a
   >>> hex(int('17',8)) #convert to decimal first
   '0xf'

   ```
   - to binary (bin()):
   ```
   >>> bin(10)
   '0b1010'
   >>> bin(int('ff',16))#convert to decimal first
   '0b11111111'
   >>> bin(int('17',8))#convert to decimal first
   '0b1111'

   ```
   - to oct(oct()):
   ```
   >>> oct(0b1010)        
   '012'
  >>> oct(11)
  '013'
  >>> oct(0xf) 
  '017'
   ```

### Conceptual misunderstanding

```
+------------------+-------------+-------------+-------------+-------------------------+-----------------+-----------------+-------------+
|    Expression    |    Value    | Bytes_value | Bytes_hex() |       Binary_value      |       Type      |  Memort address | Memory size |
+------------------+-------------+-------------+-------------+-------------------------+-----------------+-----------------+-------------+
|       0xe7       |     231     |   b'\xe7'   |      e7     |         11100111        |  <class 'int'>  |     10921856    |      28     |
|     b'\xe7'      |   b'\xe7'   |   b'\xe7'   |      e7     |         11100111        | <class 'bytes'> | 140499710520936 |      34     |
|      '\xe7'      |      ç      | b'\xc3\xa7' |     c3a7    |     1100001110100111    |  <class 'str'>  | 140499743555136 |      74     |
|   b'\xc3\xa7'    | b'\xc3\xa7' | b'\xc3\xa7' |     c3a7    |     1100001110100111    | <class 'bytes'> | 140499710519496 |      35     |
|       xe7        |     xe7     |    b'xe7'   |    786537   | 11110000110010100110111 |  <class 'str'>  | 140499710415512 |      52     |
|      b'xe7'      |    b'xe7'   |    b'xe7'   |    786537   | 11110000110010100110111 | <class 'bytes'> | 140499710520896 |      36     |
+------------------+-------------+-------------+-------------+-------------------------+-----------------+-----------------+-------------+
```
-  the first experssion is a hex data, type: int
- the sencond expression is a bytes sequence of the  hex data above, type: bytes
-  the third experssion is a character map with the unicode `\xe7`, type: str
-  the fourth experssion is a bytes sequence of the characert above **NOT the bytes of the hex data**, type: bytes 
-  the fifth experssion is a string 'xe7', type str
- the six is  experssion a bytes sequence of string above, type: bytes
-  the mac address **00:50:56:c0:00:01**  bytes in  memory or network should be the bytes of the hex data which the string representative 

## win10
- reset system:`Sysprep` 

##
qnap pass: M1das$@DR