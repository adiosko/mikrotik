from tikapy import TikapyClient
from tikapy import TikapySslClient


class interfaceSstpClientSetGeneral:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def setName(self, name, newName):
        """
        Method will set name
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=name=' + newName] )
        return ppp

    def setUser(self, name, user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        ppp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=user=' + user] )
        return ppp