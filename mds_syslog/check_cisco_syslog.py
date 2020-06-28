#!/usr/bin/python3

import pymysql
import sys
import smtplib

def mail_logs(logs_info):
    mail_receiver= 'shuangjian@mds-trading.com'
    mail_host='smtp.qq.com'
#    mail_port= 25
    mail_user='659403872@qq.com'
    mail_pass='jplyivxwaosmbbed'
    mail_subject='Cisco syslog alter'
#    mail_message='From: {}\nTo: {}\nSubject:{}\n\n{}'.format(mail_user,mail_receiver,mail_subject,loginfo)
    mail_message = 'From: {}\nTo: {}\nSubject:{}\n\n'.format(mail_user,mail_receiver,mail_subject)
    for i in logs_info:
        mail_message += '{} {}\n'.format(i[0],i[1])

    try:
#        smtpobj=smtplib.SMTP()
#        smtpobj.connect(mail_host,mail_port)
        smtpobj=smtplib.SMTP_SSL(mail_host, smtplib.SMTP_SSL_PORT)
#        smtpobj.set_debuglevel(1)
        smtpobj.login(mail_user,mail_pass)
        smtpobj.sendmail(mail_user,mail_receiver,mail_message)
        smtpobj.close
    except smtplib.SMTPException as smtperr:
        error('can not send the mail: {}'.format(smtperr))

def error(msg):
    print(msg)
    sys.exit(1)

def query_cisco_syslogs(host, user, passwd, dbname):
    try:
        db = pymysql.connect(host=host, user=user, password=passwd, db=dbname)
    except Exception as e:
        error('Can not connected to mysql.\n {} '.format(e))

    cursor=db.cursor()

    sql='select SysLogTag,Message from SystemEvents where DeviceReportedTime > now()-interval 3 minute'
    try:
        cursor.execute(sql)
        logs=cursor.fetchall()
    except Exception as e:
        error('can not excute sql {}.\n {}'.format(sql,e))
    
    db.close()
    return logs

if __name__ == "__main__":
    logs_info={}
    logs=query_cisco_syslogs('utilserver2','rsyslog','Password', 'Syslog')
    if logs:
        mail_logs(logs)
