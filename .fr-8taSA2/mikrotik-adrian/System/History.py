from tikapy import TikapyClient
from tikapy import TikapySslClient

class History:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listHistory(self):
        hist = self.client.talk(['/system/history/print'])
        return hist