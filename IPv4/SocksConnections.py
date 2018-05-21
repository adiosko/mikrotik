from tikapy import TikapyClient
from tikapy import TikapySslClient

class SocksConnections:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listConnections(self):
        """
        Method will list socks connections
        :return:
        """
        socks = self.client.talk( ['/ip/socks/connections/print'] )
        for i in socks:
            print( socks[i] )
        return socks