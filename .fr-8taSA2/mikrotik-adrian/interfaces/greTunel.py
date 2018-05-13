from tikapy import TikapyClient
from tikapy import TikapySslClient


class greTunel:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listInterfaces(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/gre/print'])
        for i in iface:
            print(iface[i])
        return iface

    def addInterface(self,remoteAddress=""):
        """

        :param remoteAddress:
        :return:
        """
        iface = self.client.talk(['/interface/gre/add','=remote-address='+remoteAddress])
        return iface

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/gre/remove','=numbers='+name])
        return iface

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/enable', '=numbers=' + name] )
        return iface

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/disable', '=numbers=' + name] )
        return iface

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/comment', '=numbers=' + name,'=comment='+comment] )
        return iface