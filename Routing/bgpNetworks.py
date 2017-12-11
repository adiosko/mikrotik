from tikapy import TikapyClient
from tikapy import TikapySslClient

class bgpNetworks:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def  listNetworks(self):
        """
        Method will list networks
        :return:
        """
        net = self.client.talk(['/routing/bgp/network/print'])
        if net == {}:
            print("No network added")
        else:
            print("Network\tSynchronize")
            for i in net:
                print(net[i]['network']+"\t"+net[i]['synchronize'])
        return net

    def addNetwork(self,network):
        """
        Method will add network
        :param network:
        :return:
        """
        net = self.client.talk(['/routing/bgp/network/add','=network='+network])
        return net

    def removeNetwork(self,number):
        """
        Method will remove network
        :param number:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/remove', '=numbers=' + number] )
        return net

    def enableNetwork(self,number):
        """
        Method will enable network
        :param number:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/enable', '=numbers=' +number] )
        return net

    def disableNetwork(self, number):
        """
        Method will enable network
        :param number:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/disable', '=numbers=' + number] )
        return net

    def commentNetwork(self,number,comment):
        """
        Method will comment network
        :param number:
        :param comment:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/comment', '=numbers=' + number,'=comment='+comment] )
        return net

    def setNetwork(self,number,network):
        """
        Method will reset network
        :param number:
        :param network:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/set', '=numbers=' + number,'=network='+network] )
        return net

    def unsetSynchronize(self,number):
        """
        method will unset synchronize
        :param number:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/set', '=numbers=' + number,'=synchronize=no'] )
        return net

    def setSynchronize(self,number):
        """
        Method will set synchronize of network
        :param number:
        :return:
        """
        net = self.client.talk( ['/routing/bgp/network/set', '=numbers=' + number, '=synchronize=yes'] )
        return net

