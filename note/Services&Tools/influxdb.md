### create user
- create database telegraf
- create user telegraf with password 'metricsmetricsmetricsmetrics'
- grant all on telegraf to telegraf

### query
- curl -G http://1.1.1.1:8086/query -u telegraf:metricsmetricsmetricsmetrics --data-urlencode "q=SHOW DATABASES"

### delete series
- > drop series from snmp_mroutetable where "group"='239.255.101.104.10.1.89.251.255.255.255.255'                                                                                 
