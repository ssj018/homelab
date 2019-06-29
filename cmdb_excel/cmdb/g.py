#!/usr/bin/env python

infos={}
def get_account():
    with open('conf/account_info','r') as f:
        alines=f.readlines()
    
    for i in alines:
        print i.split(' ')[0]	    

alines=get_account()



