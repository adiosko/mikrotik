from tikapy import TikapyClient
from tikapy import TikapySslClient

class AutoUpdate:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listKVM(self):
        """
        method will list all available KVMs on mikrotik
        :return:  list
        """
        kvm = self.client.talk(['/'])