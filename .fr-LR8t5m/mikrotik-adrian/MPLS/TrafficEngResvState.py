from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficEngResvState:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listStates(self):
        """
        Method will list all states
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/resv-state/print'])
        if mpls == {}:
            print("No state found")
        else:
            for i in mpls:
                print(mpls[i])
        return mpls