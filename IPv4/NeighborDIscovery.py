from tikapy import TikapyClient
from tikapy import TikapySslClient

class NeighborDiscovery:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enableInterface(self,name):
        """
        Method will enable discovery for interface
        :param name:
        :return:
        """
        neig = self.client.talk(['/ip/neighbor/discovery/set','=numbers='+name,'=discover=yes'])
        return neig

    def disableInterface(self, name):
        """
        Method will enable discovery for interface
        :param name:
        :return:
        """
        neig = self.client.talk( ['/ip/neighbor/discovery/set', '=numbers=' + name, '=discover=no'] )
        return neig