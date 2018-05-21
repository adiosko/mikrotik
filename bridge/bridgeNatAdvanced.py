from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeNatAdvanced:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setVlanId(self,number,vlan="1"):
        """
        Method will set vlan id
        :param number:
        :param vlan:
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/nat/set','=numbers='+number,'=vlan-id='+vlan])
        return vlan

    def setVlanId(self, number, vlan="1"):
        """
        Method will set vlan id
        :param number:
        :param vlan:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=vlan-id=' + vlan] )
        return vlan

    def setVlanPriority(self, number, vlan="1"):
        """
        Method will set vlan id
        :param number:
        :param vlan:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=vlan-priority=' + vlan] )
        return vlan

    def setVlanEncap(self, number, vlan="ip"):
        """
        Method will set vlan id
        :param number:
        :param vlan: 802.2,arp,homeplug,-av,ip,ipv6,ipx,length,lldp,loop-protect,mpls-multicats,mpls-unicats,packing-compr,packing-simple,pppoe,pppoe-discovery,rarp,service-vlan,vlan
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=vlan-encap=' + vlan] )
        return vlan

    def set8023Sap(self,number,vlan="0"):
        """

        :param number:
        :param vlan:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=802.3-sap=' + vlan] )
        return vlan

    def set8023Type(self, number, vlan="0"):
        """

        :param number:
        :param vlan:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=802.3-type=' + vlan] )
        return vlan

    def setPacketType(self,number,packet="host"):
        """

        :param number:
        :param packet: host, unicast, broadcast,multicast
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=packet-type=' + packet] )
        return vlan

    def setLimitRateFilter(self, number, rate="1/se", burst="5"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec or
        :return:
        """
        ip = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=limit=' + rate + "," + burst] )
        return ip

    def setTimeFilter(self, number, fromDate="00:00:00", toDate="1d 00:00:00", day="mon,tue"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ip = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, "=time=" + fromDate + "," + toDate + "," + day] )
        return ip

    

