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

# 2020 quater 3
## TODO

NVME
    - apply internet at gds
    - added a  layer 2 switch to gds
    - installed a pfsense -------------- 2020/7/23
    
2. replace X4 card with X5 card
  - cwgdatalog@xiaoqingqq10.1D
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
17. renew hp warranty
18. buy a  ixia (10G Flex tap)
19. redundancy of fiber
20. clear qnap space 


## what has been done
1. upgrade citrix adc
2. installed a  new ldap
3. installed a pfsense on gdsMds
4. install citrix vhost for jialun
5. installed zhouhuanvlinux
6. install pc,printer,internet for mdsl
7. test blackcore server
8. take back zhyquip1
9. interview 1 time
10. fix ddc issue  and citrix split the ddc and database
11. add remote virtual devmachine for zhouhuan
12. expend citrix hosts
13. add a ciara to cwg
14. upgrade wifi 
15. added 4 vitural hosts for mdsl
16. replace and add testlab3/testlabg
17. upgrade office switch's os
18. renew cert of citrix adc
19. update scripts to backup/monitor network devices

# 2020 quater 4

## TODO
### 2020/10/10

1. 

### 2020/10/12

1. investigate nvme ssd
2. 
3. 

### 202010/19
1. replace X4 card with X5 card
  - cwgdatalog
  - ciydatalog2
  - cijquip4 and cijdatalog

### 2020/10/28
1. 
2. test nvme ssd
3. split /build from /scratch

### 2020/11/9
1. 
2. monitor multicast route table
3. 

### 2020/11/17


### 2020/11/20
1. 

### 2020/12/14
1. install trade server for csz 

### 2020/12/17
1. fix ciara motherboard issue
2. monitor ciara hardware logs

### 20202/12/25
1. test vpn of csz newservers
2. test intel nvme ssd

### 2020/12/28
1. backup 2019rdata

## What has been done
1. replaced rfa eed servers
2. installed printer for mdsl
3. replaced ciyconn4 with ciyconn24
4. prepare 3 servers for jiangdong
5. fix rfa server network link issue.
6. replaced ciyconn4
7. fix tingting's notebookbat
8. add simret mount point on zeus1
9. set acl for live
10. switch hkg vpn
11. fix citrixhost1 memory issue
12. added the furion21 and remove 3 old servers
13. added 2 hp server for vlinux
14. fix citrixhost7 hardware issue
15. replace the old servers(furion21 replaced furion2/12/13)
16. renew citrix adc cert and license

what has been done:
1. system related:
  - Investigated and wrote a script to collect multicast table with snmp
  - Wrote a script to collectd ciara ipmi logs
  - Tested new H3C server(with AMD cpu, 256 cores)
  - Installed virtual workstation for core and ops
  - Purchased/renew licenses for citrix virtual destops and citrix adc
  - Installed/Deployed 4 citrix virtual destops for mdsl colleague
  - Investigated the use of nvme ssd on the live machine and storage 
  - Tested the benchmark of ciara HF210-G5(10core, 5.3G)
  - Fixed  3 servers hardware issues(motherboard, memory and power supply failed) 
  - Installed and Removed about 20 servers for live colos and lab 
    - added 2 trade server to csz 
    - replaced ciyconn4 with ciyconn24 for ciy
    - upgraded 2 `rfa eed` servers
    - installed 4 test servers for jiangdong
    - Installed 2 citrix xenserver to install vms
    - added furion21 (H3C AMD server with 256 cores) 
    - removed 3 old super micro servers(furion2/furion12/furion13)
    - take 1 unused server backup to office from cdg 
  - Helpdesk related works

2. network
  - switch  vpn of hkg to new line
  - upgraded acl from office  to live
  - fixed network issue of rfa servers
    

 what is in progress:
 - migrate /scratch to nvme ssd(10%)
 - monitor multicast route and apply  multicast acl(70%)
 - deal with Scrapped servers (10%)

 what can be improve:
  - Learn and understand multicast related  live applications

  Acknowledgement:
  Thanks to @liusong @wangyou @xuqan for helped in my work. Especially many suggestions and reminders from @liusong. 

  # 2021 quater 1

### 202010/19
1. replace X4 card with X5 card
  - cwgdatalog
  - ciydatalog2
  - cijquip4 and cijdatalog

### 2020/10/28

2. test nvme ssd
3. split /build from /scratch

### 2020/11/9

2. monitor multicast route table

### 2021/1/11

1. test ciara 10980
2. update the ilo check job
3. use script to test network config after change networking

### 2021/1/15

### 2021/1/19
1. fix hpe server hardware issue

## What has been done 
1. set hkg network for sgx
2. add citrix remote access for annan
3. replace remote qnap disk
