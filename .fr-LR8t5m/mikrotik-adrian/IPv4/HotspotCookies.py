from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotCookies:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listCookies(self):
        """

        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/cookie/print'])
        for i in hotspot:
            print(hotspot[i])
        return hotspot