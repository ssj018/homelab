#!/bin/bash

ping_host(){
    ping $1 -c 2
}
hosts="192.168.1.1 192.168.1.2"

for i  in $hosts
do
    ping_host $i 
done