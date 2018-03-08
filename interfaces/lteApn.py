from tikapy import TikapyClient
from tikapy import TikapySslClient

class lteApn:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listApn(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/print'])
        for i in iface:
            print(iface[i])
        return iface

    def addApn(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/add','=apn='+name])
        return iface

    def removeApn(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/remove','=numbers='+name])
        return iface