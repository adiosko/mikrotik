from tikapy import TikapyClient
from tikapy import TikapySslClient

class reselectChannel:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def reselectChannel(self,name):
        """
        Method will reselect channel of interface
        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/reselect-channel','=interface='+name])
        return wifi

