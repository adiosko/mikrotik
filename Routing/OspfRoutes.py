from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfRoutes:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listROutes(self):
        """
        Method will list all routes
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/route/print'])
        if ospf == {}:
            print("No route found")
        else:
            print("Instance\tArea\tDst address\tGateway\tInterface\tcost\tState")
            for i in ospf:
                print(ospf[i]['instance']+"\t"+ospf[i]['area']+"\t"+ospf[i]['dst-address']+"\t"+ospf[i]['gateway']+"\t"
                      +ospf[i]['interface']+"\t"+ospf[i]['cost']+"\t"+ospf[i]['state'])
        return ospf