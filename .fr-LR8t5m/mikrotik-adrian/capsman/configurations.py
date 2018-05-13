from tikapy import TikapyClient
from tikapy import TikapySslClient

class channels:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listConfigs(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/configuration/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addConfig(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/configuration/add','=name='+name])
        return wifi

    def removeConfiguration(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/remove', '=numbers=' + name] )
        return wifi

    def commentConfiguration(self,name,comment):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/remove', '=numbers=' + name,'=comment='+comment] )
        return wifi