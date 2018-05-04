from tikapy import TikapyClient
from tikapy import TikapySslClient

class Identity:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setHostname(self,hostname):
        host = self.client.talk(['/system/identity/set','=name='+hostname])
        print(host)
        return host