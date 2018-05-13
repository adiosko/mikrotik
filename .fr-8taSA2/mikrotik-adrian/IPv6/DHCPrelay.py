from tikapy import TikapyClient
from tikapy import TikapySslClient

class Dhcpv6Relay:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRelays(self):
        """
        Method will list all relays
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-relay/print'])
        if ipv6 == {}:
            print("No relay defined")
        else:
            print("Name\tInterface")
            for i in ipv6:
                print(ipv6[i]['name']+"\t"+ipv6[i]['interface'])
        return ipv6

    def addRelay(self,name,interface,server):
        """
        Method will add interface
        :param interface:
        :param name:
        :param server:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-relay/add','=name='+name,'=interface='+interface,'=dhcp-server='+server])
        return ipv6

    def removeRelay(self,name):
        """

        :param name:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp/relay/remove','=numbers='+name])
        return ipv6

    def enableRelay(self, name):
        """

        :param name:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp/relay/enable', '=numbers=' + name] )
        return ipv6

    def disableRelay(self, name):
        """

        :param name:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp/relay/disable', '=numbers=' + name] )
        return ipv6

    def commentRelay(self,name,comment):
        """
        Method wil lcomment rule
        :param name:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp/relay/comment', '=numbers=' + name,'=comment='+comment] )
        return ipv6

    def resetCounters(self):
        """
        Method will rese tcounters
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-relay/reset-counters'])
        return ipv6

    def setName(self,name,newName):
        """
        Method will set new name
        :param name:
        :param newName:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-relay/set','=numbers='+name,'=name='+newName])
        return ipv6

    def setInterface(self,name,interface):
        """
        Method will set interface
        :param name:
        :param interface:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-relay/set','=numbers='+name,'=interface='+interface])
        return ipv6

    def setDhcpServer(self,name,server,interface=None):
        """
        Method will set dhcp server for relay
        :param name:
        :param server: IPv6%interface
        :return:
        """
        if interface == None:
            ipv6 = self.client.talk(['/ipv6/dhcp-relay/set','=numbers='+name,'=dhcp-server='+server])
        else:
            ipv6 = self.client.talk(['/ipv6/dhcp-relay/set','=numbers='+name,'=dhcp-server='+server+"%"+interface])
        return ipv6

    def setLinkAddress(self,name,address="::"):
        """
        Method will set link address of dhcp relay
        :param name:
        :param address:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-relay/set','=numbers='+name,'=link-address='+address])
        return ipv6

    def setDelayThreshold(self,name,hold="00:00:00"):
        """
        Method will set threshold
        :param name:
        :param hold:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-relay/set', '=numbers=' + name,'=delay-threshold='+hold] )
        return ipv6