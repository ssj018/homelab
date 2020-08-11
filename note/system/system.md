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


## win10
- reset system:`Sysprep` 

## qnap 
- pass: M1das$@DR

## Linux

- find /proc -name mountinfo |xargs grep home (kill process and rm )
- grep -h home /proc/\*/task/\*/mountinfo