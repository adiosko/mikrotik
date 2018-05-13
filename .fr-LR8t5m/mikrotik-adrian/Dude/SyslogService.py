from tikapy import TikapyClient
from tikapy import TikapySslClient

class SyslogService:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

