from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotServicePorts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPorts(self):
        """
        Method will list service ports
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/service-port/print'])
        print("Name\tport")
        for i in hotspot:
            print(hotspot[i]['name']+"\t"+hotspot[i]['ports'])
        return hotspot

    def enablePorts(self,name):
        """
        Method will enable port
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/service-port/enable','=numbers='+name] )
        return hotspot

    def disablePorts(self,name):
        """
        Method will disable ports
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/service-port/disable', '=numbers=' + name] )
        return hotspot

    def setPorts(self,name,port):
        """
        Method will set port
        :param name:
        :param port:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/service-port/set', '=numbers=' + name,'=ports='+port] )
        return hotspot