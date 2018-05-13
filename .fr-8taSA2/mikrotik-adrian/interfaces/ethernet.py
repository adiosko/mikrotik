from tikapy import TikapyClient
from tikapy import TikapySslClient


class ethernet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def printInterface(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/ethernet/print'])
        return iface

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/ethernet/enable','=numbers='+name])
        return iface

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/ethernet/disable', '=numbers=' + name] )
        return iface

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk( ['/interface/ethernet/comment', '=numbers=' + name,'=comment='+comment] )
        return iface

    def resetMac(self,number):
        iface = self.client.talk(['/interface/ethernet/reset-mac-address','=numbers='+number])
        return iface