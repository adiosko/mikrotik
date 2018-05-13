from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotActive:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listActive(self):
        """
        Method will list active users
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/active/print'])
        if hotspot == {}:
            print("No user found")
        else:
            for i in hotspot:
                print(hotspot[i])
        return hotspot