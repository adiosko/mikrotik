from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfVirtualLinks:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listVirtualLinks(self):
        """
        Method will list all virtual links
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/virtual-link/print'])
        print(ospf)
        return ospf

    def addVirtualLink(self,neighbor,transmitArea):
        """
        Method will add vlink
        :param neighbor:
        :param transmitArea:
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/virtual-link/add','=neighbor-id='+neighbor,'transmit-area='+transmitArea])
        return ospf

    def removeVirtualLink(self,number):
        """
        Method will remove Vlink
        :param number:
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/virtual-link/remove','=numbers='+number])
        return ospf

    def disableVirtualLink(self,number):
        """
        Method will disable vlink
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/disable', '=numbers=' + number] )
        return ospf

    def enableVirtualLink(self,number):
        """
        Method will enable vlink
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/enable', '=numbers=' + number] )
        return ospf

    def setNeighborId(self,number,neighbor="0.0.0.0"):
        """
        Method will set neighbor id
        :param number:
        :param neighbor:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number,'=neighbor-id='+neighbor] )
        return ospf

    def setTarnsitArea(self,number,area="backbone"):
        """
        Method will set transit area
        :param number:
        :param area: backbone and custom areas
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=transit-area=' + area] )
        return ospf

    def setAuthentication(self,number,auth="none"):
        """
        Method will set authentication type
        :param number:
        :param auth: none,simple,MD5
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=authentication=' + auth] )
        return ospf

    def setAuthKey(self,number,key):
        """
        Method will set auth key
        :param number:
        :param key:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=authentication-key=' + key] )
        return ospf

    def setAuthKeyId(self,number,ID="1"):
        """
        Method will set auth key id
        :param number:
        :param ID:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=authentication-key-id=' + ID] )
        return ospf

    def setInstanceId(self,number,ID="0"):
        """
        Method will set authentication id
        :param number:
        :param ID:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=instance-id=' + ID] )
        return ospf

    def setUseBfd(self,number):
        """
        Method will set usage of bfd
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=use-bfd=yes'] )
        return ospf

    def unsetUseBfd(self, number):
        """
        Method will set usage of bfd
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/virtual-link/set', '=numbers=' + number, '=use-bfd=no'] )
        return ospf

