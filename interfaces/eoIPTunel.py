from tikapy import TikapyClient
from tikapy import TikapySslClient


class eoIPTunel:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listInterfaces(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/eoip/print'])
        for i in iface:
            print(iface[i])
        return iface

    def addInterface(self,remoteAddress,tunelId):
        """

        :param remoteAddress:
        :return:
        """
        iface = self.client.talk(['/interface/eoip/add','=remote-address='+remoteAddress,'=tunnel-id='+tunelId])
        return iface

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/eoip/remove','=numbers='+name])
        return iface

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/eoip/enable', '=numbers=' + name] )
        return iface

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/eoip/disable', '=numbers=' + name] )
        return iface

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk( ['/interface/eoip/comment', '=numbers=' + name,'=comment='+comment] )
        return iface