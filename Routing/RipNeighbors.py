from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipNeighbors:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list all neighbors
        :return:
        """
        rip = self.client.talk(['/routing/rip/neighbor/print'])
        if rip == {}:
            print("No neighbor found")
        else:
            print(rip)