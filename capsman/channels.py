from tikapy import TikapyClient
from tikapy import TikapySslClient

class channels:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listChannels(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/channel/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addChannel(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/channel/add','=name='+name])
        return wifi

    def removeChannel(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/remove', '=numbers=' + name] )
        return wifi

    def commentChannel(self,name,comment):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/remove', '=numbers=' + name,'=comment='+comment] )
        return wifi