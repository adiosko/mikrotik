from tikapy import TikapyClient
from tikapy import TikapySslClient

class rates:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listRates(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/rates/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addRates(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/rares/add','=name='+name])
        return wifi

    def removeRate(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/rares/remove', '=numbers=' + name] )
        return wifi

    def commentRate(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/rares/comment', '=numbers=' + name,'=comment='+comment] )
        return wifi