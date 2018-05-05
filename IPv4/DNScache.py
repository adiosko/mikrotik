from tikapy import TikapyClient
from tikapy import TikapySslClient

class DNScache:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listCache(self):
        """
        Method will list cache buffer
        :return:
        """
        dns = self.client.talk(['/ip/dns/cache/print'])
        if dns == {}:
            print("No object found")
        else:
            for i in dns:
                print(dns[i])
        return dns

    def flushDNS(self):
        """
        Method will flush dns cache
        :return:
        """
        dns = self.client.talk( ['/ip/dns/cache/flush'] )
        return dns