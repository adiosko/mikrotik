from tikapy import TikapyClient
from tikapy import TikapySslClient

class DhcpRelay:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRelay(self):
        """
        Method will list relay
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-relay/print'])
        return ipv4

    def addRelay(self,name,interface,server):
        """
        Method will add relay
        :param interface:
        :param server: dhcp server
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-relay/add','=name='+name,'=interface='+interface,'=dhcp-server='+server])
        return ipv4

    def removeRelay(self,name):
        """
        Method will remove relay
        :param name:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-relay/remove','=numbers='+name])
        return ipv4

    def enableRelay(self,name):
        """
        Method will enable relay
        :param name:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-relay/enable', '=numbers=' + name] )
        return ipv4

    def disableRelay(self, name):
        """
        Method will enable relay
        :param name:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-relay/disable', '=numbers=' + name] )
        return ipv4

    def resetCounters(self):
        """
        Method will reset counters
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-relay/reset-counters'])
        return ipv4

    def setName(self,name,newName):
        """
        Methodwill rename relay
        :param name:
        :param newName:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-relay/set','=numbers='+name,'=name='+newName])
        return ipv4

    def setInterface(self,name,iface):
        """
        Methodwill set interface
        :param name:
        :param iface:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-relay/set', '=numbers=' + name, '=interface=' + iface] )
        return ipv4

    def setDhcpServer(self,name,server):
        """
        Method will set relay dhcp server
        :param name:
        :param server:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-relay/set', '=numbers=' + name, '=dhcp-server=' + server] )
        return ipv4

    def setThreshold(self,name,threshold="00:00:00"):
        """
        Method will set threshold
        :param name:
        :param threshold:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-relay/set', '=numbers=' + name, '=delay-threshold=' + threshold] )
        return ipv4

    def setLocalAddress(self,name,address="0.0.0.0"):
        """
        Method will sert local address
        :param name:
        :param address:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-relay/set', '=numbers=' + name, '=local-address=' + address] )
        return ipv4
