import LoginManager
import apiList
import tikapy
import socket

login = LoginManager('admin','admin')
api = apiList()

port = 8728
username = "admin"
password = 'admin'
devices = login.listMikrotikDevices()
api = tikapy.TikapyClient(devices[0], port)
print ("Available devices are "+devices)

api.connectToMikrotik(devices[0],port,username,password)
api.listInterfaces()
api.listIpAddresses()
api.disconnectFromMikrotik()