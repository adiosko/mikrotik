from tikapy import TikapyClient
from tikapy import TikapySslClient

class BridgeHosts:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listHosts(self):
        """
        Method will list hosts
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/host/print'])
        print("Mac\tOut iface\tAge\tBridge")
        for i in bridge:
            print(bridge[i]['mac-address']+"\t"+bridge[i]['on-interface']+"\t"+bridge[i]['age']+"\t"+bridge[i]['bridge'])
        return bridge