from tikapy import TikapyClient
from tikapy import TikapySslClient

class RouteNexthops:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNexthops(self):
        """
        Method will list nexthops
        :param number:
        :return:
        """
        route = self.client.talk(['/ip/route/nexthop/print'])
        print("Address\tGateway Status\tScope")
        for i in route:
            print(route[i]['address']+"\t"+route[i]['gw-state']+"\t"+route[i]['scope'])
        return route