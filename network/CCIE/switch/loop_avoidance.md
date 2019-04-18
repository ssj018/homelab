## Transparent Bridging

##redundant path 
   - multiple frame copies
   - mac address table instability 
   - broadcast storms
   
## spanning tree protocol
   - BPDU: bridge protocol data unit. provides the exchange of information between switches 
     - config BPDU
     
      |Bytes|Field|
      |---|---|
      |2|Protocol_id|
      |1|version|
      |1|Message type
      |1|Flags
      |8|Root ID
      |4|Cost of path
      |8|Bridge ID|
      |2|Port ID
      |2|Message age
      |2|hello time|
      |2|Forward delay
      
     - TCN BPDU( when top changed)
    
      |Bytes|Field|
      |---|---|
      |2|Protocol_id|
      |1|version|
      |1|Message type
      
   - three parameters during election
      - BID: bridge id(priority(32768) + MAC). on cisco switches, very vlan has one BID
      - path cost:
         
         |link speed|cost|
         |---|---|
         |10G|2|
         |1G|4|
         |100M|19
         |10M|100
         
       - port id: priority(128)+ port number
      
   - spanning-tree operation
      - one root bridge per network
           1.  the switch who has a smaller priority is root bridge
           2.  if priority is equal, then who  has a smaller mac will be a root bridge
           3.  root bridge's id is root-id
      - one root port per nonroot bridge 
           1. Lowest RID
           2. Lowest path cost to root bridge
           3. Lowest sender BID
           4. Lowest sender port ID
           
      - one designated port per segment(link),ports on two devices           
           1. Lowest RID
           2. Lowest path cost to root bridge
           3. Lowest BID
           4. Lowest port ID
           
      - Nondesignated ports are blocked
      
   - pvst: per vlan spanning-tree
     - Priority = 32768+vlan_id; every vlan has an priority
   
       
   