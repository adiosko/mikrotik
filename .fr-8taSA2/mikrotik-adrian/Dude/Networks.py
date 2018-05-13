from tikapy import TikapyClient
from tikapy import TikapySslClient

class Networks:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNetworks(self):
        """
        Not aplicable via API
        :return: list
        """
        pass