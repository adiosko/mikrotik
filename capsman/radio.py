from tikapy import TikapyClient
from tikapy import TikapySslClient

class radio:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def listRadios(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/radio/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def provisionRadio(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/radio/provision','=numbers='+number])
        return wifi