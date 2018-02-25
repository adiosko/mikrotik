from tikapy import TikapyClient
from tikapy import TikapySslClient

class registration:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRegistration(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/registration-table/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def removeConnection(self,name):
        """
        Method will kill connection
        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/registration-table/remove','=numbers='+name])
        return wifi

    def resetConnection(self,name):
        """
        Method will reset connection
        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/registration-table/reset','=numbers='+name])
        return wifi