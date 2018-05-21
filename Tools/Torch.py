from tikapy import TikapyClient
from tikapy import TikapySslClient

class Torch:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setTorchInterface(self,interface,duration):
        """
        Method will set torch interface with time limit
        :param interface: interface to use
        :param duration: time limit
        :return:
        """
        torch = self.client.talk(['/tool/torch','=interface='+interface,'=duration='+duration])
        print(torch)
        return torch

    def setTorchFreezeTime(self,interface,time):
        """
        Method will set freeze time
        :param interface: interface to use
        :param time: timne to freeze
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=freeze-frame-time='+time] )
        return torch

    def setSourceIpv4Address(self,interface,address):
        """
        Method will set source address
        :param interface:
        :param address:
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=src-address=' + address] )
        return torch

    def setDestinationIpv4(self,interface,address):
        """
        Method will set dst address
        :param interface:
        :param address:
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=dst-address=' + address] )
        return torch


    def setSourceIpv6(self,interface,address):
        """
        Method will set source ipv6 address
        :param interface:
        :param address:
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=src-address6=' + address] )
        return torch

    def setIpv6Destination(self,interface,address):
        """
        Method will set Ipv6 dst address
        :param interface:
        :param address:
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=dst-address6=' + address] )
        return torch

    def setMacProtocol(self,interface,protocol):
        """
        Method will set mac protocol
        :param interface:
        :param protocol: all, arp, ip, ipv6,  ipx, loop, pppoe,pppoe-discovery, rarp, vlan
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=mac-protocol=' + protocol] )
        return torch

    def setProtocol(self,interface, protocol):
        """
        Method will set protocol
        :param interface:
        :param protocol: egp, ggp, icmp, igmp, ip-encap, ipsec,ospf, pup,tcp,udp
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=ip-protocol=' + protocol] )
        return torch

    def setDSCP(self,interface):
        """
        Method will set dscp field def any
        :param interface:
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=dscp=any'] )
        return torch

    def setPort(self,interface,port):
        """
        Method will set port to monitor
        :param interface:
        :param port: f.e auth, asia, bdp, etc
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=port=' + port] )
        return torch

    def setVlanId(self,interface,Vlan):
        """
        Method will set vlan id
        :param interface:
        :param Vlan:
        :return:
        """
        torch = self.client.talk( ['/tool/torch', '=interface=' + interface, '=vlan-id=' + Vlan] )
        return torch