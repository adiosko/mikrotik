from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipRoutes:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRoutes(self):
        """
        Method will list all routes
        :return:
        """
        rip = self.client.talk(['/routing/rip/route/print'])
        if rip == {}:
            print("No route found")
        else:
            print("Dst address\tFrom")
            for i in rip:
                #print(rip[i])
                print(rip[i]['dst-address']+"\t"+rip[i]['metric'])
        return rip