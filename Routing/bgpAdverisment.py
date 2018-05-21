from tikapy import TikapyClient
from tikapy import TikapySslClient

class bgpAdvertisment:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listAdvertisments(self):
        """
        Method will list advertisments
        :return:
        """
        adv = self.client.talk(['/routing/bgp/advertisements/print'])
        if adv == {}:
            print("No advertisment")
        else:
            print(adv)
        return adv