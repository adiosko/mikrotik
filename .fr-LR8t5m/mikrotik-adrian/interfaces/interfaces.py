from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaces:
    def __init__(self, address, username, password):
        self.client = TikapySslClient(address, 8729)
        self.client.login(username, password)

    def listInterfaces(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/print'])
        return iface

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/enable','=numbers='+name])
        return iface

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/disable','=numbers='+name])
        return iface

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk(['/interface/comment','=numbers='+name,'=comment='+comment])
        return iface