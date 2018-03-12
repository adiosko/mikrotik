from tikapy import TikapyClient
from tikapy import TikapySslClient

class lists:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listLists(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/list/print'])
        for i in iface:
            print(iface[i])
        return iface

    def addList(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/list/add','=name='+name])
        return iface

    def removeList(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/list/remove', '=numbers=' + name])
        return iface

    def commentList(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        iface = self.client.talk(['/interface/list/comment', '=numbers=' + name,'=comment='+comment])
        return iface