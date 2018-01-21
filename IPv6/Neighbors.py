from tikapy import TikapyClient
from tikapy import TikapySslClient

class Neighbors:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)


    def listNeighbor(self):
        """
        Method will list neighbors
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/neighbor/print'])
        if ipv6 == {}:
            print("No neighbor found")
        else:
            print("Address\tInterface\tMAC\tStatus")
            for i in ipv6:
                print(ipv6[i])
                print(ipv6[i]['address']+"\t"+ipv6['interface']+"\t"+ipv6[i]['mac-address']+"\t"+ipv6[i]['status'])
        return ipv6