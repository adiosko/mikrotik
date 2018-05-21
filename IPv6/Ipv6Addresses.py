from tikapy import TikapyClient
from tikapy import TikapySslClient

class Ipv6Addresses:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listAddresses(self):
        """
        Method will list all ipv6 addresses
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/address/print'])
        if ipv6 == {}:
            print("No address found")
        else:
            print("Address\tFrom pool\tInterface\tAdvertise")
            for i in ipv6:
                print(ipv6[i]['address']+"\t"+ipv6[i]['from-pool']+"\t"+ipv6[i]['interface']+"\t"+ipv6[i]['advertise'])
        return ipv6

    def addAddress(self,interface,address):
        """
        Method will add address
        :param interface:
        :param address: global address or link-local address
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/address/add','=interface='+interface,'=address='+address])
        return ipv6

    def removeAddress(self,number):
        """
        Method will remove address from table
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/remove', '=numbers='+number] )
        return ipv6

    def enableAddress(self,number):
        """
        Method will enable address
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/enable', '=numbers=' + number] )
        return ipv6

    def disableAddress(self,number):
        """
        Method will disable address
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/disable', '=numbers=' + number] )
        return ipv6

    def commentAddress(self,number,comment):
        """
        Method will comment address
        :param number:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv6

    def setAddress(self,number,address):
        """
        method will set existing address
        :param number:
        :param address:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=address=' + address] )
        return ipv6

    def setPool(self,number,pool):
        """
        Method will set ipv6 pool
        :param name:
        :param pool: ipv6 subnet
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=from-pool=' + pool] )
        return ipv6

    def setInterface(self,number,interface):
        """
        Method will set interface for address
        :param number:
        :param interface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=interface=' + interface] )
        return ipv6

    def setEui64(self,number):
        """
        Method will set eui64
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=eui64=yes'] )
        return ipv6

    def unsetEui64(self, number):
        """
        Method will set eui64
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=eui64=no'] )
        return ipv6

    def setAdvertise(self, number):
        """
        Method will set eui64
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=advertise=yes'] )
        return ipv6

    def unsetAdvertise(self, number):
        """
        Method will set eui64
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=advertise=no'] )
        return ipv6

    def setNoDAD(self,number):
        """
        Method will set parameter no DAD
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=no-dad=yes'] )
        return ipv6

    def unsetNoDad(self,number):
        """
        Method will unset no dad option
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/address/set', '=numbers=' + number, '=no-dad=no'] )
        return ipv6