from tikapy import TikapyClient
from tikapy import TikapySslClient

class RouteNexthops:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNexthops(self):
        """
        Method will list nexthops
        :param number:
        :return:
        """
        route = self.client.talk(['/ip/route/nexthop/print'])
        return route