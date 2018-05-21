from tikapy import TikapyClient
from tikapy import TikapySslClient

class Charts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listCharts(self):
        """
        Method will list all dude charts
        :return: list
        """
        pass

