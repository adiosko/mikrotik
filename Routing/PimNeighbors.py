from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimNeighbors:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list pim neighbors
        :return:
        """
        pim = self.client.talk( ['/routing/pim/neighbors/print'] )
        if pim == {}:
            print("no neighbor found")
        else:
            for i in pim:
                print(pim[i])
        return pim