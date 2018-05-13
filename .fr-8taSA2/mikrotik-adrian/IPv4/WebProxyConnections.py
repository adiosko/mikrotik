from tikapy import TikapyClient
from tikapy import TikapySslClient

class WebProxyConnections:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listConnections(self):
        """
        Method will list connections
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/connections/print'])
        for i in proxy:
            print(proxy[i])
        return proxy