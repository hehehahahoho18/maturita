import snap7
from snap7.util import *
plc = snap7.client.Client()
ip_address = '192.168.0.1'
rack = 0
slot = 1
plc.connect("192.168.0.1", 0, 1)
print(plc.get_connected())

#data = plc.db_read(1,0,2)
#print (data)

size = plc.db_get(1)
data = plc.db_read(1,0,size)

value=get_bool(data,0)
print(value)