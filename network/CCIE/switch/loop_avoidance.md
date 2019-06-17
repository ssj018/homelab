#STP
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
   - port roles
      - root ports
      - designated ports
      - nodesignated ports
      
       
## pvst: per vlan spanning-tree
  
   - Priority = 32768+vlan_id; every vlan has an priority
   
     
   - change setup of stp
      - change priority of vlan 1
         1. :
               ```
            switch(config)# spanning-tree vlan 1 priority  20480 
            ```
            > % Bridge Priority must be in increments of 4096.
            > 
            > % Allowed values are:
            >
            >   0     4096  8192  12288 16384 20480 24576 28672  
            >
            >   32768 36864 40960 45056 49152 53248 57344 61440
         
         2. :
         
             ```
              switch(config)# spanning-tree vlan 1 root primary/second
             ```
             > this command will download priority , but only execute once. this switch not always be the root
       
       - change the cost or priority of ports
          
            ```
               Switch(config-if)#spanning-tree vlan 1 cost 1000
               Switch(config-if)#spanning-tree port-priority 64
            ``` 
            >% Port Priority in increments of 64 is required
            
            
   - spanning tree port  states change process, when a link is down
      - blocking (loss of BPDU detected,max age=20 sec)(if link is none direct connection with the nondesignated ports,waiting 20s, otherwise it will not blocking )
      - Listening (forward delay = 15 sec)
      - Learning (forward delay = 15 sec)
      - Forwarding
      - (None direct: total time 50s; direct: total time 30 )
      
   - portfast:  Port does not participate in spanning tree calculations
      - in global mode, all access interface will enable portfast
     ```
     switch(config)#spanning-tree portfast default
     ```
     - in interface mode
     ```
     switch(config-if): spanning-tree portfast 
     ```
     
   - uplink-fast: if only 2 uplink, one of them down, the backup link states will changed from "blk" to "fwd". 
     >  will automatically increase the priority number
     >  
     > used for directly failure 
     - in global mode
     ``` 
     switch(config)#spanning-tree uplinkfast
     ```
     
   - backbonefast:
     > let switch quickly detect a indirectly failed,  ports change from "blk" to "lsn". save 20s
     > 
     > use secondary BPDU
     - in global mode: 
     ``` 
     switch(config): spanning-tree backbonefast
     ```
     
   - Rapid spanning-tree protocol(Stand fast stp),RSTP
     - port states
       - discarding(block+listen)
       - learning
       - forwarding
       
      - pot roles:
        - root port
        - designated port
        - alternative port
        - Backup port
      
     - Edge port (be equal to fast_port of cisco )
     
     - backbone 
     
     - RSTP link Types
       - p2p : full duplex
       - shared: half duplex
     
        > only p2p link can fast convergence
        >
        > in rstp, only none-endport(not connect to a host, but bridge/switch and etc. ) change to forwarding status,
          it will  send TC BPDU 
        > 
        >every switch could send config BPDU( where top changed), so fast convergence
        
        
   - Multiple spanning tree protocol, MST(add vlans to some instances)
      - MST config on each switch(MST Regions)
        - name
        - revision number
        - vlan association table
        
       ```
       switch(config)#spanning-tree mst configuration
       switch(config-mst)#instance 1 vlan 10,20
       switch(config-mst)#instance 2 vlan 30,40 
       ```
        - IST: MST0 default mst for all vlans which do not assign to other instance
        
        
 ## protecting the operation of stp
   
   - BPDU guard: used for portfast, do not allow receive BPDU, if received, port change to err-disabled
       > how to restore err-disabled port
       >
       >1. shutdown/no shutdown
       >
       >2. errdisable recovery cause bpduguard (auto recovery, default inventory 300s)
       
       - BPDU filter : used for portfast, avoid this port send portfast
       > in global mode:
       >  ports received BPDU, ports wil participate in STP elections
       > 
       > in ports mode:
       > when ports received BPDU, it will drop it, do nothing.  this may cause loop
       
       **if guard and filter setup on a same port, filter is effective , guard will not be effective**
       
   -  Describing Root Guard
       >  setup on a port which will connected to a new added switch
       >  
       > if the new switch's priority is lower than root bridge, the port will be block.
       ``` 
        switch(config-if)# spanning-tree guard root
       ```
   - loop guard
       >
       >unidirectional link failure:
       >
       >  a link (receive or transfer,only one direction failed)
       > this will cause loop path
       ````
       in global mode:
          siwtch(config)#spanning-tree loopguard default
          
       in port mode:
         switch(config-if)#spanning-tree guard loop
         
       ````
       
   - UDLD
       >
       >detect  if a link has unidirectional link failed
       >
       ```
        in global, only for fiber
          switch(config)#udld enable
        for rj45:
           switch(config)#uuld port (aggressive)
           
       ``` 