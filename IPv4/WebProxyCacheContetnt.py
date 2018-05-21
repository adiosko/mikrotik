from tikapy import TikapyClient
from tikapy import TikapySslClient

class WebProxyCacheContent:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listContents(self):
        """
        Method will list connections
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/cache-contents/print'])
        for i in proxy:
            print(proxy[i])
        return proxy