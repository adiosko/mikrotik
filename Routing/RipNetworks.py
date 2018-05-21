from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipNetworks:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNetworks(self):
        """
        Method will list networks
        :return:
        """
        rip = self.client.talk(['/routing/rip/network/print'])
        if rip == {}:
            print("no network found")
        else:
            print("Network\tDIsbaled")
            for i in rip:
                print(rip[i]['network']+"\t"+rip[i]['disabled'])
        return rip

    def addNetwork(self,network):
        """
        Method will add network
        :param network: subnet/prefix
        :return:
        """
        rip = self.client.talk(['/routing/rip/network/add','=network='+network])
        return rip

    def removeNetwork(self,number):
        """
        Method will remove network
        :param number:
        :return:
        """
        rip = self.client.talk(['/routing/rip/network/remove','=numbers='+number])
        return rip

    def enableNetwork(self,number):
        """
        Method will enable network
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/network/enable', '=numbers=' + number] )
        return rip

    def disableNetwork(self,number):
        """
        Method will disable network
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/network/disable', '=numbers=' + number] )
        return rip

    def setNetwork(self,number,network):
        """
        Method will set existing network
        :param number:
        :param network:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/network/set', '=numbers=' + number,'=network='+network] )
        return rip