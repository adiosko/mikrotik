from tikapy import TikapyClient
from tikapy import TikapySslClient

class detectInternet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setInterfaceList(self,interfaceList="none"):
        """

        :param interfaceList: none,all,dynamic
        :return:
        """
        iface = self.client.talk(['/interface/detect-internet/set','=detect-interface-list='+interfaceList])
        return iface

    def setLanList(self,lanList="none"):
        """

        :param lanList: all,dynamic,none
        :return:
        """
        iface = self.client.talk(['/interface/detect-internet/set', '=lan-interface-list=' + lanList])
        return iface

    def setWanList(self,wanList="none"):
        """

        :param wanList: all ,dynamic,none
        :return:
        """
        iface = self.client.talk(['/interface/detect-internet/set', '=wan-interface-list=' + wanList])
        return iface

    def setInternetList(self,inetList="none"):
        """

        :param inetList: none,dynamic,all
        :return:
        """
        iface = self.client.talk(['/interface/detect-internet/set', '=internet-interface-list=' + inetList])
        return iface