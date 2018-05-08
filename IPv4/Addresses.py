from tikapy import TikapyClient
from tikapy import TikapySslClient
import tikapy

class Addresses:
    def __init__(self,address,username,password):
        self.client = tikapy.TikapySslClient( address)
        self.client.login( username,password)

    def listAddresses(self):
        """
        Method will list address
        :return:
        """
        ipv4 = self.client.talk(['/ip/address/print'])
        return ipv4

    def addAddress(self,address,interface):
        """
        Method will add address
        :param address:
        :param interface:
        :return:
        """
        ipv4 = self.client.talk(['/ip/address/add','=address='+address,'=interface='+interface])
        return ipv4

    def removeAddress(self,number):
        """
        Method will remove address
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/address/remove','=numbers='+number])
        return ipv4

    def enableAddress(self,number):
        """
        Method will enable address
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/address/enable', '=numbers=' + number] )
        return ipv4

    def disableAddress(self,number):
        """
        Method will disable address
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/address/disable', '=numbers=' + number] )
        return ipv4

    def commentAddress(self,number,comment):
        """
        Method will comment address
        :param number:
        :param comment:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/address/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv4

    def setAddress(self,number,address):
        """
        Method will set address
        :param number:
        :param address: x.y.z.k/l
        :return:
        """
        ipv4 = self.client.talk( ['/ip/address/set', '=numbers=' + number, '=address=' + address] )
        return ipv4

    def setNetwork(self,number,network):
        """
        Method will set network
        :param number:
        :param network: napr. 10.1.2.0
        :return:
        """
        ipv4 = self.client.talk( ['/ip/address/set', '=numbers=' + number, '=network=' + network] )
        return ipv4

    def setInterface(self,number,iface):
        """
        Method will set interface
        :param number:
        :param iface:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/address/set', '=numbers=' + number, '=interface=' + iface] )
        return ipv4
