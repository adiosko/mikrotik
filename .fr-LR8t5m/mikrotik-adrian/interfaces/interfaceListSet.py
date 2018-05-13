from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceListSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setList(self,number,list):
        """

        :param number:
        :param list:
        :return:
        """
        iface = self.client.talk(['/interface/list/member/set','=numbers='+number,'=list='+list])
        return iface

    def setInterface(self,number,interface):
        """

        :param number:
        :param interface:
        :return:
        """
        iface = self.client.talk(['/interface/list/member/set', '=numbers=' + number, '=interface=' + interface])
        return iface