from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecRemotePeers:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listPeers(self):
        """
        Method will list remove peers
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/remote-peers/print'])
        for i in ipsec:
            print(ipsec[i])
        return ipsec

    def killConnections(self):
        """
        Method will kill connections
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/remote-peers/kill-connections'])
        return ipsec