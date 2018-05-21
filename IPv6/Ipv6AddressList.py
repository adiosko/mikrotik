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
        ipv6 = self.client.talk(['/ipv6/firewall/address-list/print'])
        if ipv6 == {}:
            print("No list found")
        else:
            print("Name\tAddress")
            for i in ipv6:
                print(ipv6[i]['list']+"\t"+ipv6[i]['address'])
        return ipv6

    def addAddressList(self,name):
        """
        Method will add address list
        :param name:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/address-list/add','=list='+name])
        return ipv6

    def removeList(self,number):
        """
        Method will remove address list
        :param number: numbe rof list to remove
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/address-list/remove','=numbers='+number])
        return ipv6

    def enableList(self, number):
        """
        Method will remove address list
        :param number: numbe rof list to remove
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/address-list/enable', '=numbers=' + number] )
        return ipv6

    def disableList(self, number):
        """
        Method will remove address list
        :param number: numbe rof list to remove
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/address-list/disable', '=numbers=' + number] )
        return ipv6

    def commentList(self,number,comment):
        """
        Methodwill comment address list
        :param number:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/address-list/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv6

    def setName(self,number,name):
        """
        Method will set address list issue
        :param number:
        :param name:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/address-list/set','=numbers='+number,'=list='+name])
        return ipv6

    def setAddress(self,number,address):
        """
        Method will set address
        :param number:
        :param address:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/address-list/set', '=numbers=' + number, '=address=' + address] )
        return ipv6

    def setTImeout(self,number,timeout="00:00:00"):
        """
        Method will se t timeout
        :param number:
        :param timeout:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/address-list/set', '=numbers=' + number, '=timeout=' + timeout] )
        return ipv6
