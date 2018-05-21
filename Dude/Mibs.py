from tikapy import TikapyClient
from tikapy import TikapySslClient

class Mibs:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listMibs(self):
        """
        Not aplicable via api
        :return: list
        """
        pass