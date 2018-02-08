from tikapy import TikapyClient
from tikapy import TikapySslClient

class NeighborList:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list all neighbors
        :return:
        """
        neig = self.client.talk(['/ip/neighbor/print'])
        if neig == {}:
            print("No neighbor found")
        else:
            print("interface\tAddress\tMAC")
            for i in neig:
                print(neig[i]['interface']+"\t"+neig[i]['address']+"\t"+neig[i]['mac-address'])
        return neig