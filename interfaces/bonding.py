from tikapy import TikapyClient
from tikapy import TikapySslClient

class bonding:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def listBonding(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/bonding/print'])
        for i in iface:
            print(iface[i])
        return iface

    def addInterface(self,slaveInterface):
        """

        :param slaveInterface:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/add','=slaves='+slaveInterface])
        return iface

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/remove','=numbers='+name])
        return iface

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/enable', '=numbers=' + name])
        return iface

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/disable', '=numbers=' + name])
        return iface

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/comment', '=numbers=' + name,'=comment='+comment])
        return iface