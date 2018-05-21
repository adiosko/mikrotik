from tikapy import TikapyClient
from tikapy import TikapySslClient

class Arp:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listArp(self):
        """
        Method will list arp records
        :return:
        """
        ipv4 = self.client.talk(['/ip/arp/print'])
        return ipv4

    def addArp(self,interface,address,mac):
        """
        Method will add arp entry
        :param interface:
        :param address:
        :param mac:
        :return:
        """
        ipv4 = self.client.talk(['/ip/arp/add','=interface='+interface,'=address='+address,'=mac-address='+mac])
        return ipv4

    def removeArp(self,number):
        """
        Method will remove arp entry
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/remove', '=numbers=' + number] )
        return ipv4

    def enableArp(self,number):
        """
        Method will enable entry
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/enable', '=numbers=' + number] )
        return ipv4

    def disableArp(self,number):
        """
        Method will disable arp
        :param number:
        :return:
        """
        self.listArp()
        ipv4 = self.client.talk( ['/ip/arp/disable', '=numbers=' + number] )
        return ipv4

    def commentArp(self,number,comment):
        """
        Method will comment entry
        :param number:
        :param comment:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv4

    def setAddress(self,number,address):
        """
        Method will set ip address of entry
        :param number:
        :param address: IP address
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/set', '=numbers=' + number,'=address='+address] )
        return ipv4

    def setMacAddress(self,number,mac):
        """
        Method will set mac addess of entry
        :param number:
        :param mac:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/set', '=numbers=' + number, '=mac-address=' + mac] )
        return ipv4

    def setInterface(self,number,interface):
        """
        Method will set interface of arp entry
        :param number:
        :param interface:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/set', '=numbers=' + number, '=interface=' + interface] )
        return ipv4

    def setPublished(self,number):
        """
        Method will set pusblish arp record
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/set', '=numbers=' + number, '=published=yes'] )
        return ipv4

    def unsetPublish(self,number):
        """
        Method will unset publish
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/arp/set', '=numbers=' + number, '=published=no'] )
        return ipv4