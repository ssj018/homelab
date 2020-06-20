
### select the last 3 minutes data from database
- select SysLogTag,Message from SystemEvents where DeviceReportedTime > now()-interval 3 minute;
- select count(1) from myTable where Login_time > date_sub(now(), interval 3 minute)
- select * from myTable where Login_time > select max(time) - interval 3 minute ;(This query will work even if your table is not updated...) 

### mysql  create remote user
#### create
- CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';
- CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';

#### grant 
- GRANT ALL ON *.* TO 'myuser'@'localhost';
- GRANT ALL ON *.* TO 'myuser'@'%';
- GRANT SELECT, INSERT, UPDATE ON Syslog.* TO u1;
- flush privileges;

### git push local branch to remote master
- git push origin master