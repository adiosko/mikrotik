from tikapy import TikapyClient
from tikapy import TikapySslClient
import pprint
#clock a api nie je podporavane

class SystemClock:
    def __init__(self,address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def showSystemClock(self):
        clock = self.client.talk(['/system/clock/manual/print'])
