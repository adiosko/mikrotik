import LoginManager
import tikapy
import pprint


class apiList():
    #port = 8728  # or 8729 for SSL
    #api = tikapy.TikapyClient(address[0], port)
    #global api

    def __init__(self,login,password,api,address):
        self.user = login
        self.pwd = password
        self.address = login.listMikrotikDevices()
        self.API = tikapy.TikapyClient(address[0], 8728)

    login = LoginManager('admin','admin')

    def connectToMikrotik(self,address,port,username,password):
        connect = api.login(user=username,password=password)
        return connect


    def disconnectFromMikrotik(self):
        disconnect = api.disconnect()
        return disconnect

    def listInterfaces(self):
        listOfInterfaces = pprint ['/interface/print']
        return listOfInterfaces

    def listIpAddresses(self):
        listOfIPAddresses = pprint ['/ip/address/print']
        return listOfIPAddresses