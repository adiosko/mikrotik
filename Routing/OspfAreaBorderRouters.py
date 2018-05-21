from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfAreaBorderRouters:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRouters(self):
        """
        Method will list area ospf routres
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/area-border-router/print'])
        print(ospf)
        return ospf