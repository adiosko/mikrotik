from tikapy import TikapyClient
from tikapy import TikapySslClient

class remoteCap:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listCaps(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/remote-cap/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def removeCap(self,numbers):
        """

        :param numbers:
        :return:
        """
        wifi = self.client.talk(['/caps-man/remote-cap/remove','=numbers='+numbers])
        return wifi

    def provisionCap(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/remote-cap/provision', '=numbers=' + number] )
        return wifi

    def upgradeCap(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/remote-cap/upgrade', '=numbers=' + number] )
        return wifi

    def setIdentity(self,number,identity):
        """

        :param number:
        :param identity:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/remote-cap/set-identity', '=numbers=' + number,'=identity='+identity] )
        return wifi