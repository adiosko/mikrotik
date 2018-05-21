from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficEngPathState:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPaths(self):
        """
        Method will list all paths
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/path-state/print'])
        if mpls == {}:
            print("No path found")
        else:
            for i in mpls:
                print(mpls[i])
        return mpls