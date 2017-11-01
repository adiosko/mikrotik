import LoginManager
import tikapy
import pprint


class apiList():
    login = LoginManager()
    address = login.listMikrotikDevices()
    port = 8728  # or 8729 for SSL
    api = tikapy.TikapyClient(address[0], port)
    global api

    def __init__(self,login,password):
        self.user = login
        self.pwd = password

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