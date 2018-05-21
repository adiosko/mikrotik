from tikapy import TikapyClient
from tikapy import TikapySslClient

class WebProxyInserts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listInserts(self):
        """
        Method will list lookups
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/inserts/print'])
        for i in proxy:
            print(proxy)
        return proxy