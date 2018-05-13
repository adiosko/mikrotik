from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallConnections:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)


    def listCOnnections(self):
        """
        Method will list all connections
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/connection/print'])
        if ipv6 == {}:
            print("No connection found")
        else:
            print("Protocol\tSrc address\tDst address\tTimeout\tSrc port\tDst port")
            for i in ipv6:
                print(ipv6[i]['protocol']+"\t"+ipv6[i]['src-address']+"\t"+ipv6[i]['dst-address']+"\t"+ipv6[i]['timeout']+"\t"+ipv6[i]['src-port']+"\t"+ipv6[i]['dst-port'])
        return ipv6