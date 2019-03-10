#!/bin/bash
HOSTNAME="${COLLECTD_HOSTNAME:-localhost}"
INTERVAL="${COLLECTD_INTERVAL:-10}"

while :; do
    mem_avail=$(cat /proc/meminfo |grep Avail|awk '{print 1024 * $2}' | tr -d '\r\n\t')

    # <instance-id>/<plugin>-<plugin_instance>/<type>-<type_instance>
    echo "PUTVAL \"$HOSTNAME/memavail-default/memory-available\" interval=$INTERVAL N:$mem_avail"
    sleep $INTERVAL
done
