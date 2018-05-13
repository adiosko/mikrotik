from tikapy import TikapyClient
from tikapy import TikapySslClient

class SwitchRule:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    #match
    def listRules(self):
        """
        Method will lis rules
        :return:
        """
        switch = self.client.talk(['/interface/ethernet/switch/rule/print'])
        for i in switch:
            print(switch[i])
        return switch

    def addRule(self,switch,port):
        """
        Method will add action
        :param switch:
        :param port:
        :return:
        """
        rule = self.client.talk(['/interface/ethernet/switch/rule/add','=switch='+switch,'=ports='+port])
        return rule

    def removeRule(self,number):
        """
        Method will remove rule
        :param number:
        :return:
        """
        rule = self.client.talk(['/interface/ethernet/switch/rule/remove','=numbers='+number])
        return rule

    def enableRule(self, number):
        """
        Method will remove rule
        :param number:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/enable', '=numbers=' + number] )
        return rule

    def disableRule(self, number):
        """
        Method will remove rule
        :param number:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/disable', '=numbers=' + number] )
        return rule

    #Match
    def setSwitch(self,number,switch="switch1"):
        """
        Method will set switch
        :param number:
        :param switch:
        :return:
        """
        rule = self.client.talk(['/interface/ethernet/switch/rule/set','=numbers='+number,'=switch='+switch])
        return rule

    def setPorts(self,number,port="switch1-cpu"):
        """

        :param number:
        :param port: ports,switch1-cpu
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=ports=' + port] )
        return rule

    def srcMacAddress(self,number,mac):
        """
        Method will sets src mac address
        :param number:
        :param mac:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return rule

    def setDstMacAddress(self,number,mac):
        """
        Method will set dst mac address
        :param number:
        :param mac:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=dst-mac-address=' + mac] )
        return rule

    def setProtocol(self,number,protocol="ip"):
        """
        Method will set protocol
        :param number:
        :param protocol: 802.2,arp,homeplug-av,ip,ipv6,ipx,lldp,loop-protect,mpls-multicast,mpls-unicast,packing-compr,
        packing-simple,pppoe,ppoe-discovery,rarp,service-vlan,vlan
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=mac-protocol=' + protocol] )
        return rule

    def setVlanHeader(self,number,vlan="not-present"):
        """
        Method will set vlan ehader
        :param number:
        :param vlan: present,not-present
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=vlan-header=' + vlan] )
        return rule

    def setVlanId(self,number,ID="1"):
        """
        method will set vlan id
        :param number:
        :param ID:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=vlan-id=' + ID] )
        return rule

    def setVlanPriority(self,number,priority="1"):
        """
        Method will set vlan priority
        :param number:
        :param priority:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=vlan-priority=' + priority] )
        return rule

    def setSrcAddress(self,number,src):
        """
        Method will set src address
        :param number:
        :param src:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=src-address=' + src] )
        return rule

    def serDstAddress(self,number,dst):
        """
        method will set dst  address
        :param number:
        :param dst:
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=dst-address=' + dst] )
        return rule

    def setIpProtocol(self,number,protocol="tcp"):
        """
        Method w
        :param number:
        :param protocol:  dccp,ddp,egp,encap,etherip,ggp,gre,gmp,icmp,icmpv6,idpr-cmtp,igmp,ipencap,ipip,ipsec-ah,ipsec-esp,
        ipv6,ipv6-frag,ipv6-nonxt,ipv6-opts,ipv6-route,iso-tp4,l2tp,ospf,pim,pup,rdp,rspf,rsvp,sctp,st,tcp,udp,udp-lite,
        vmtp,vrrp,xns-idp,xtp
        :return:
        """
        rule = self.client.talk( ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=protocol=' + protocol] )
        return rule

    def setSrcPort(self,number,port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=src-port=' + port] )
        return rule

    def setDstPort(self,number,port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=dst-port=' + port] )
        return rule

    def setDscp(self,number,dscp="0"):
        """
        Method will set dscp
        :param number:
        :param dscp:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=dscp=' + dscp] )
        return rule

    def setIpv6SrcAddress(self,number,src="::/0"):
        """
        Method wil lset src ipv6 address
        :param number:
        :param src:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=src-address6=' + src] )
        return rule

    def setDstIpv6Address(self,number,dst):
        """
        Method will set dst address
        :param number:
        :param dst:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=dst-address6=' + dst] )
        return rule

    def setTrafficClass(self,number,tclass="0"):
        """
        Method will set traffic class
        :param number:
        :param tclass:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=traffic-class=' + tclass] )
        return rule

    def setFlowLabel(self,number,label="0"):
        """
        Method will set flow label
        :param number:
        :param label:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=flow-label=' + label] )
        return rule

    #Action
    def copyToCpu(self,number):
        """
        Method will set copt to cpu action
        :param number:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=copy-to-cpu=yes'] )
        return rule

    def redirectToCpu(self,number):
        """

        :param number:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=redirect-to=cpu=yes'] )
        return rule

    def mirror(self,number):
        """

        :param number:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=mirror=yes'] )
        return rule

    def setNewDstPorts(self,number,port):
        """
        Method will set new dst ports
        :param number:
        :param port:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=new-dst-ports=' + port] )
        return rule

    def setNewVlanId(self,number,vlan="1"):
        """
        Method wil lset new vlan ID
        :param number:
        :param vlan: ID of vlan
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=new-vlan-id=' + vlan] )
        return rule

    def setNewVlanPriority(self,number,priority):
        """
        Method will set vlan priority
        :param number:
        :param priority:
        :return:
        """
        rule = self.client.talk(
            ['/interface/ethernet/switch/rule/set', '=numbers=' + number, '=new-vlan-priority=' + priority] )
        return rule