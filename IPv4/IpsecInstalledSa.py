from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecInstalledSa:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listSas(self):
        """
        Method wlist all tunnels between poublic IPs
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/installed-sa/print'])
        for i in ipsec:
            print(ipsec[i])
        return ipsec

    def flushSa(self):
        """
        Method will flush sa's
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/installed-sa/flush'])
        return ipsec
