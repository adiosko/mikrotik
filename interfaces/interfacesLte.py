from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacesLte:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/enable','=numbers='+name])
        return iface

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/disable', '=numbers=' + name])
        return iface

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk(['/interface/lte/comment', '=numbers=' + name, '=comment='+comment])
        return iface