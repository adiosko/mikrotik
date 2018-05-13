from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfNetworks:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNetworks(self):
        """
        Method will list networks
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/network/print'])
        if ospf == {}:
            print("No network set")
        else:
            print("Network\tArea")
            for i in ospf:
                print(ospf[i]['network']+"\t"+ospf[i]['area'])
        return ospf

    def addNetwork(self,area="backbone"):
        """
        Method will add default network
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/network/add','=area='+area])
        return ospf

    def removeNetwork(self,number):
        """
        Method will remove network
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/network/remove', '=numbers=' + number] )
        return ospf

    def disableNetwork(self,number):
        """
        Method will disable net
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/network/disable', '=numbers=' + number] )
        return ospf

    def enableNetwork(self,number):
        """
        Method will enable net
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/network/enable', '=numbers=' + number] )
        return ospf

    def commentNetwork(self,number,comment):
        """
        Method will commentnetwork
        :param number:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/network/comment', '=numbers=' + number,'=comment='+comment] )
        return ospf

    def setNetwork(self,number,net):
        """
        Method will set new network
        :param number:
        :param net:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/network/set', '=numbers=' + number, '=network=' + net] )
        return ospf

    def setArea(self,number,area="backbone"):
        """
        Method will set area
        :param number:
        :param area:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/network/set', '=numbers=' + number, '=area=' + area] )
        return ospf