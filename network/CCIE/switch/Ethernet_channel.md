#Etherchannel
  - protocol:
     - LACP
        -  IEEE standard proprietary
        
     - pagp
        - cisco proprietary
  - logical aggregation of similar links
  - load balances
  - viewed as one logical port
  - redundancy
  - max port number of a channel is : 8
  - do not support 10M port
  - support layer2 and layer3
  - all ports within a channel should have the same duplex and speed. LACP can only be full duplex
  ```
   interface port-range
    swicth(config-if-range)#channel-group id mode XXXX
  ```
  >mode:
  >
  >  **active:**     Enable LACP unconditionally
  >
  >   **auto:**       Enable PAgP only if a PAgP device is detected
  >
  >   **desirable:**  Enable PAgP unconditionally
  >
  >   **on:**         Enable Etherchannel only
  >
  >  **passive:**    Enable LACP only if a LACP device is detected

  - channel config mismatch will cause port in: err-disable 