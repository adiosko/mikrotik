from tikapy import TikapyClient
from tikapy import TikapySslClient

class listsSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        iface = self.client.talk(['/interface/list/set','=numbers='+name,'=name='+newName])
        return iface

    def setInclude(self,name,incl="all"):
        """

        :param name:
        :param incl:all,dynamic,none
        :return:
        """
        iface = self.client.talk(['/interface/list/set', '=numbers=' + name, '=include=' + incl])
        return iface

    def setExclude(self,name,excl="all"):
        """

        :param name:
        :param excl: all, dynamic, none
        :return:
        """
        iface = self.client.talk(['/interface/list/set', '=numbers=' + name, '=exclude=' + excl])
        return iface