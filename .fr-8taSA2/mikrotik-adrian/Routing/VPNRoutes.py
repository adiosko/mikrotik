from tikapy import TikapyClient
from tikapy import TikapySslClient

class VPNRoutes:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRoutes(self):
        """
        Method will list all VPN methods
        :return:
        """
        vpn = self.client.talk(['/routing/bgp/vpnv4-route/print'])
        if vpn == {}:
            print("no vpn route found")
        else:
            print(vpn)
        return vpn