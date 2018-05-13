from tikapy import TikapyClient
from tikapy import TikapySslClient

class BridgeHosts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listHosts(self):
        """
        Method will list hosts
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/host/print'])
        return bridge