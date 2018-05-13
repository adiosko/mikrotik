from tikapy import TikapyClient
from tikapy import TikapySslClient

class pppoe:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listPppoe(self):
        """
        Method will list pppoe server
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/print'])
        for i in ppp:
            print(ppp[i])
        pass

    def addPppoe(self,name,intterface):
        """
        Mehod will add pppoe server
        :param name:
        :param intterface:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/add','=service-name='+name,'=interface='+intterface])
        return ppp

    def removePppoe(self,name):
        """
        Method will remove pppoe interface
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/remove','=numbers='+name])
        return ppp


    def enablePppoe(self,name):
        """
        Method will enable server
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/enable', '=numbers=' + name])
        return ppp

    def disablePppoe(self,name):
        """
        Method will disable pppoe iface
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/disable', '=numbers=' + name])
        return ppp

    def commentPppoe(self,name,comment):
        """
        Method will comment iface
        :param name:
        :param comment:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/comment', '=numbers=' + name,'=comment='+comment])
        return ppp

