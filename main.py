import LoginManager
import apiList
import tikapy

login = LoginManager()
api = apiList()

port =  8728
username = "admin"
password = '"password"'
devices = login.listMikrotikDevices()
api = tikapy.TikapyClient(devices[0], port)
print ("Available devices are "+devices)

api.connectToMikrotik(devices[0],port,username,password)
api.listInterfaces()
api.listIpAddresses()
api.disconnectFromMikrotik()