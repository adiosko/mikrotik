from tikapy import TikapyClient
from tikapy import TikapySslClient

class detectInternetState:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def listStatuses(self):
        """

        :return:
        """
        iface = self.client.talk(['/interface/detect-internet/state/print'])
        for i in iface:
            print(iface[i])
        return iface
    