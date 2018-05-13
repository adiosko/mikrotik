from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfAsBorderRouters:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRouters(self):
        """
        Method will list all border routers
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/as-border-router/print'])
        print(ospf)
        return ospf