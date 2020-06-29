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

- bytes: bit stream, like:01010001110.  Everything in computer are stored as bytes
- human can not read/write by bytes. so every software we used  should decode byte to str for read and encode str to byte for write in computer
- there are many encoding methods : ascii, GBK,unicode(utf-8)
- when we use python read or store `str`, python will auto encode/decode for us


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

- python3 has a class `bytes` to define a data as bytes type, when use `bytes` means tell python do not auto encode/decode , we deal with it by ourself.
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
To  define a bytes type data, just add `b` before the object.The bytes type can be characters in the ASCII range and other hexadecimal character data