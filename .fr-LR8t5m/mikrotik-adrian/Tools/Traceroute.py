from tikapy import TikapyClient
from tikapy import TikapySslClient

class Traceroute:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setTraceroute(self,address):
        """
        Method will set traceroute on mikrotik
        :param address: address to trace
        :return:
        """
        trc = self.client.talk(['/tool/traceroute','=address='+address])
        return trc

    def setPacketSize(self,address,packet):
        """
        Method will trace with specific  packet size
        :param address: address
        :param packet: packet size default 56 B
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address,'=size='+packet] )
        return trc

    def setTimeout(self,address,timeout):
        """
        Method will set traceroute timeout
        :param address:
        :param timeout: default 1000 ms
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=timeout=' +  timeout] )
        return trc

    def setProtcol(self,address, protocol):
        """
        Method will set protocol to send
        :param address:
        :param protocol:
        :return: icmp/udp
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=protocol=' + protocol] )
        return trc

    def useDNS(self,address):
        """
        Method will use dns in traceroute
        :param address: address to trace with dns enabled
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=use-dns=yes'] )
        return trc

    def dontUseDNS(self, address):
        """
        Method will not use dns in traceroute
        :param address: address to trace with dns enabled
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=use-dns=no'] )
        return trc

    def setPacketCount(self,address,count):
        """
        Method will set count of packets to send
        :param address:
        :param count: number of count
        :return:
        """

    def useDNS(self, address):
        """
        Method will use dns in traceroute
        :param address: address to trace with dns enabled
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=use-dns=no'] )
        return trc
    def setMaxHops(self,address,hops):
        """
        Method will set max hops on route
        :param address:
        :param hops:
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=max-hops=' + hops] )
        return trc

    def setSourceAddress(self,address,src):
        """
        Method will set source address in trc
        :param address:
        :param src: ip src address
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=src-address=' + src] )
        return trc

    def setTracertInterface(self,address,interface):
        """
        Method will set tracert interface
        :param address:
        :param interface:
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=interface=' + interface] )
        return trc

    def setDSCP(self,address,dscp):
        """
        Method will set dscp field
        :param address:
        :param dscp:
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=dscp=' + dscp] )
        return trc

    def setRoutingTable(self,address):
        """
        Method will set routing table on tracetrt dafault is main
        :param address:
        :return:
        """
        trc = self.client.talk( ['/tool/traceroute', '=address=' + address, '=routing-table=main'] )
        return trc