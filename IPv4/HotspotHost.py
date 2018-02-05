from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotHosts:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listHosts(self):
        """
        Method will list hosts
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/host/print'])
        if hotspot == {}:
            print("No host found")
        else:
            for i in hotspot:
                print(hotspot[i])
        return hotspot