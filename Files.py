from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class Files:
    def __init__(self,address):
        self.client = TikapyClient( address, 8728 )
        self.client.login( 'admin', 'admin' )
    def listFiles(self):
        pass

    def backuprouter(self,filename):
        pass

    def restorerouter(self,filename):
        pass

