from tikapy import TikapyClient
from tikapy import TikapySslClient

class SocksAccess:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listAccess(self):
        """
        Method will list socks access
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/print'] )
        print( "Src address\tSrc port\tDstAddress\tDst port\taction" )
        for i in socks:
            print( socks[i]['src-address'] + "\t" + socks[i]['src-port'] + "\t" + socks[i]['dst-address'] + "\t" +
                   socks[i]['dst-port'] + "\t" + socks[i]['action'] )
        return socks

    def addAccess(self, action="allow"):
        """
        Method will set access
        :param action: allow,deny
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/add', '=action=' + action] )
        return socks

    def removeAccess(self, number):
        """
        Method will remove access
        :param number:
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/remove', '=numbers=' + number] )
        return socks

    def enableAccess(self, number):
        """
        Method will enable access
        :param number:
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/enable', '=numbers=' + number] )
        return socks

    def disableAccess(self, number):
        """
        Method will disable access
        :param number:
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/disable', '=numbers=' + number] )
        return socks

    def commentAccess(self, number, comment):
        """
        Method will comment access
        :param number:
        :param comment:
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/comment', '=numbers=' + number, '=comment=' + comment] )
        return socks

    def setSrcAddress(self, number, address):
        """
        Method will se tsrc address
        :param number:
        :param address: !, !address
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/set', '=numbers=' + number, '=src-address=' + address] )
        return socks

    def setSrcPort(self, number, port="0-65535"):
        """
        Method will set src port
        :param number:
        :param port: !, port
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/set', '=numbers=' + number, '=src-port=' + port] )
        return socks

    def setDstAddress(self, number, address):
        """
        Method will se tsrc address
        :param number:
        :param address: !, !address
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/set', '=numbers=' + number, '=dst-address=' + address] )
        return socks

    def setDstPort(self, number, port="0-65535"):
        """
        Method will set src port
        :param number:
        :param port: !, port
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/set', '=numbers=' + number, '=dst-port=' + port] )
        return socks

    def setAction(self, number, action="allow"):
        """
        Method will set action
        :param number:
        :param action: allow, deny
        :return:
        """
        socks = self.client.talk( ['/ip/socks/access/set', '=numbers=' + number, '=action=' + action] )
        return socks