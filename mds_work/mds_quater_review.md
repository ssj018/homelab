# 2020 quater 1
## what has been done
### system
- bench mark amd server test
- backup 2018pdata to tape
- move sched to gds
   -  Investigate / prepare hardware resources, server, network, power, etc. at gds
   -  designed and set up the network for new sched servers
   -  moved servers from ciy2 to gds and reinstall them
   - set up dns/ldap/nfs in gds
- update  documents sysadmin workbook
   - toplogic 
   - dns setup
   - openldap master/slave setup
   - ciara console management user guide
   - how to update ciara bios firmware
   - how to update hp rack server firmware
   - how upgrade cisco nxos
- daily hardware maintain（fixed or changed disks/memory/change/power supply,etc.）
- prepare servers for new production  
   - cwg: 3 servers
   - csz: 5 servers + 1 switch
- ctrix adc upgrade for secutrity bug and cert rnew
- helpdesk related
- subscription of secutriy site(ctrix and ...)


### network
- monitor traffic of all raw fiber in between colos

## what is in progress
- multicast acl  setup

## acknowledge
- thanks every one specially @wangyou @liusong for help of my daily works

-----------------------------------
# 2020 quater 2
## TODO

14. purchase workstation for ouyangliu
15. renew license of citrix

## what has been done

1. investigate fiber issue between cwg and gds
  - changed the fiber modules from 10KM to 40KM
2. investigate telecom internet down at middle night
  - mv qnap vpn from  telecom to unicome as a  workaround 
3. replace ciytradea4 with ciara server
4. added nic for hkgquote1
5. add 10g nic for mdstrademon3/4
6. migrate winvpn for mdstrademon3/4 to xenserver
7. upgrade wenjiao's workstation
8. add cable for mgmt0 of switches
9. fixed furion20 memory issue
10. optimate hubdc vpn setup
11. reset csz network
12. expend gds sched
13. added 3 new servers to csz
14. fixed haisw1 fan's issue
15. fixed gds servers cable issue
16. added 2 csztrade server in citic future
17. collectd switches syslog to office and added a logviewer
18. added a xenserver for dev machine
19. setup network for HK
20. debug multicast issue of hkgquote1 with core
21. create mail box for maidisheng
22. renew cert of citrix adc
23. test multicast acl setup
24. take back ciytradea3/a4/trip1

# 2020 quater 2
## TODO

1. add vpn network on gds
    - apply internet at gds
    - added a  layer 2 switch to gds
    - installed a pfsense -------------- 2020/7/23
    
2. replace X4 card with X5 card
  - cwgdatalog
  - ciydatalog2
  - cijquip4 and cijdatalog
3. investigate ilo sensor of 6148
  - ciy2 done
4. test snmp collect of switches ***
5. deploy ospf on colos
6. 2factor auth of wifi and openvpn pha
7. sudo user manangement with ldap
8. apply multicast acl to live
9. consider redundancy of live switches
10. switch ldap from utilserver to utilserver2
12. renew the license of citrix
13. add a ciara to cwg
### 8/10
14. test blackcore server
15. add remote virtualdevmachine for zhouhuan
16. upgrade wifi 


## what has been done
1. upgrade citrix adc
2. installed a  new ldap
3. installed a pfsense on gdsMds
### july, week 4
4. install citrix vhost for jialun
