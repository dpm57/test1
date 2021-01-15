import ipaddress
addr4 = ipaddress.ip_address('192.168.1.2')
x = addr4 in ipaddress.ip_network('192.168.1.0/24')
print (x) 

