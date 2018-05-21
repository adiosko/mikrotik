from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallAddressList:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listAddressList(self):
        """
        Method will list address lists
        :return:
        """
        ip = self.client.talk(['/ip/firewall/address-list/print'])
        return ip

    def addAddressList(self,name,address):
        """
        Method will add address list
        :param name:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/address-list/add','=list='+name,'=address='+address])
        return ip

    def removeList(self,number):
        """
        Method will remove address list
        :param number: numbe rof list to remove
        :return:
        """
        ip = self.client.talk(['/ip/firewall/address-list/remove','=numbers='+number])
        return ip

    def enableList(self, number):
        """
        Method will remove address list
        :param number: numbe rof list to remove
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/address-list/enable', '=numbers=' + number] )
        return ip

    def disableList(self, number):
        """
        Method will remove address list
        :param number: numbe rof list to remove
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/address-list/disable', '=numbers=' + number] )
        return ip

    def commentList(self,number,comment):
        """
        Methodwill comment address list
        :param number:
        :param comment:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/address-list/comment', '=numbers=' + number,'=comment='+comment] )
        return ip

    def setName(self,number,name):
        """
        Method will set address list issue
        :param number:
        :param name:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/address-list/set','=numbers='+number,'=list='+name])
        return ip

    def setAddress(self,number,address):
        """
        Method will set address
        :param number:
        :param address:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/address-list/set', '=numbers=' + number, '=address=' + address] )
        return ip

    def setTImeout(self,number,timeout="00:00:00"):
        """
        Method will se t timeout
        :param number:
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/address-list/set', '=numbers=' + number, '=timeout=' + timeout] )
        return ip