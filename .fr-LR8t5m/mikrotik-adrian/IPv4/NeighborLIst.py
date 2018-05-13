from tikapy import TikapyClient
from tikapy import TikapySslClient

class NeighborList:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list all neighbors
        :return:
        """
        neig = self.client.talk(['/ip/neighbor/print'])
        return neig