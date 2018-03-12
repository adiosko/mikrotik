from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceList:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listInterafce(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/list/member/print'])
        for i in iface:
            print(iface[i])
        return iface

    def addInterface(self,list,interface):
        """

        :param list
        :param interface:
        :return:
        """
        iface = self.client.talk(['/interface/list/member,add','=list='+list,'=interface='+interface])
        return iface

    def removeList(self,number):
        """

        :param number:
        :return:
        """
        iface = self.client.talk(['/interface/list/member/remove','=numbers='+number])
        return iface

    def enableList(self,number):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/list/member/enable', '=numbers=' + number])
        return iface

    def disableList(self,number):
        """

        :param number:
        :return:
        """
        iface = self.client.talk(['/interface/list/member/disable', '=numbers=' + number])
        return iface

    def commentList(self,number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        iface = self.client.talk(['/interface/list/member/comment', '=numbers=' + number,'=comment='+comment])
        return iface