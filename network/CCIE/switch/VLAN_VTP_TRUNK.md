##VLAN and TRUNK
1. basic function
   - Address learning . mac address table  (cam table)
   - Forward/filter decision
   - Loop avoidance 
   
2. how to forward
   - learning source mac address of the  packet  received on port(record the map of mac address and port in mac address table)
   - forward packet by destination mac address
   - one port can cache many mac address
   - one mac address can only match one port( the lasted map  will overwrite the previous state )
   - if the destination is a broadcast, forward to all interface(flooding)
   - if the destination mac is not in the mac address table. forwarding to all interface(flooding)

3. mac address of switch
   - one base mac
   - every port has a mac (basic mac + port number)
   - some special mac address like: 0100.0cXX.XXXX.XXXX is for cisco private protocols
   
4. vlan: isolate broadcast domain
   - a vlan is equivalent to a bridge
   - port mode:
      1. access
      2. trunk
   - trunk link protocol: ISL,802.1q
      - cmd: switchport encapsulation dot1q/isl
   - ISL: cisco private protocol,Implemented in hardware,has higher efficiency
       
       original frame:
       
       |1| 2|3 |4 | 5|
       |----|---|---|----|---|
       | dst mac|src mac|type|IP packet|FCS|
       
       packet format:
   
       | add ISL|1| 2|3 |4 | 5| add isl_crc|
       |---|----|---|---|----|---|---|
       |***ISL***| dst mac|src mac|type|IP packet|FCS|***ISLCRC***|
       
       ISL: 26bytes
       
       ISLCRC: 4bytes
       
   - 802.1q: stand protocol
   
       original frame:
       
       |1| 2|3 |4 | 5|
       |----|---|---|----|---|
       | dst mac|src mac|type|IP packet|FCS|
     
     packet format:
     
       |1 | 2|insert tag|3 |4 | 5(change FCS)|
       |----|---|---|---|----|---|
       | dst mac|src mac|tag|type|IP packet|FCS|
        
        - tag:
             - total: 4Byte
             - 2byte： etype=0X8100(802.1q)
             - 3bit：QOS
             - 1bit： keep for token ring
             - 12bit： VLAN id
             
      native vlan:
        - do not add tag for native vlan
        - in 802.1q, if switches received a frame with out tag, it will forward it to native vlan
        - native vlans' id between a trunk link show be same
        
   - vlan_id: 0 - 4095
      - 0,4095 reserved
      - 1 : cisco default
      - 2-1001: for ethernet vlans
      - 1002-1005: for FDDI and token ring
      - 1006-4096: extend vlans (switches of 3550 and above, and vtp should work on transparent mode)

   - DTP: provides the ability to negotiate the trunking method
     - cmd: switchport encapsulation  negotiate
      
   - Q-IN-Q:
      - 802.1q Tunneling
      - two vlan tags
  
##VTP
   - VLAN TRUNK PROTOCOL
   - Sync vlans between all switches
   - VTP domain XXXX
   - VTP mode:
       - server 
          1. creates/modifies/deletes vlans
          2. send/forward advertisements
          3. synchronizes vlan configurations
          4. save configuration in nvram
         
       - clients
          1. can not  creates/change/delete vlans
          2. forward advertisements 
          3. synchronizes vlan configurations
          4. does not save configuration in nvram(need to confirm)
        
       - Transparent
          1. create/modifies/deletes vlans(only effective in local )
          2. forward advertisements 
          3. does not synchronizes vlans
          4. saves configuration in nvram
       
   - sends advertisements on trunk ports only
   - VTP advertisements are sent as multicast frames(MAC)
   - VTP advertisements are sent every 5 minutes or when there is a change
   - VTP server and clients are synchronized to latest revision number (low revision number sync with higher revision number)
   - Set password to auth: vtp password XXXX
   - VTP pruning
