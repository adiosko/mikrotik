from tikapy import TikapyClient
import pprint
#clock a api nie je podporavane

class SystemClock:
    def __init__(self,address, username, password):
            self.client = TikapyClient( address, 8728 )
            self.client.login( username, password )
    def showSystemClock(self):
        clock = self.client.talk(['/system/clock/manual/print'])
