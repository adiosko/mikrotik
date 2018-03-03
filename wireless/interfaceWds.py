from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWds:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listInterfaces(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addInterface(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/add'])
        return wifi

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/remove','=numbers='+name])
        return wifi

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/enable', '=numbers=' + name])
        return wifi

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/disable', '=numbers=' + name])
        return wifi

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/comment', '=numbers=' + name,'=comment='+comment])
        return wifi