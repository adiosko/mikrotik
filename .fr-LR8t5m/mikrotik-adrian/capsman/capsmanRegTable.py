from tikapy import TikapyClient
from tikapy import TikapySslClient

class capsmanRegTable:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listComponents(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/registration-table/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def removeComponent(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/registration-table/remove','=numbers='+number])
        return wifi