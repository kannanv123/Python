import config
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.7', config.username,config.password)
iosvl2.open()
 
print iosvl2.get_facts()
 
ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))
 
iosvl2.close()
