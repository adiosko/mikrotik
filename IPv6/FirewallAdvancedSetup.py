from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallAdvancedSetup:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setSrcAddressListFilter(self,number,addr):
        """
        Method will set src address list
        :param number:
        :param addr: name of list
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set','=numbers='+number,'=src-address-list='+addr])
        return ipv6

    def setSrcAddressMangle(self, number, addr):
        """
        Method will set src address list
        :param number:
        :param addr: name of list
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=src-address-list=' + addr] )
        return ipv6

    def setSrcAddressListRaw(self, number, addr):
        """
        Method will set src address list
        :param number:
        :param addr: name of list
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=src-address-list=' + addr] )
        return ipv6

    def setDstAddressListFilter(self,number,addr):
        """
        method will set address list
        :param number:
        :param addr:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=dst-address-list=' + addr] )
        return ipv6

    def setDstAddressListMangle(self, number, addr):
        """
        method will set address list
        :param number:
        :param addr:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=dst-address-list=' + addr] )
        return ipv6

    def setContentFilter(self,number,cont="0"):
        """
        Method will set fw content
        :param number:
        :param cont:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=content=' + cont] )
        return ipv6

    def setContentMangle(self, number, cont="0"):
        """
        Method will set fw content
        :param number:
        :param cont:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=content=' + cont] )
        return ipv6

    def setContentRaw(self, number, cont="0"):
        """
        Method will set fw content
        :param number:
        :param cont:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=content=' + cont] )
        return ipv6

    def setCOnnectionByteFilter(self,number,bt="0"):
        """
        Method will set conenction byte
        :param number:
        :param bt: hexa value or decimal number
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-bytes=' + bt] )
        return ipv6

    def setCOnnectionByteMangle(self, number, bt="0"):
        """
        Method will set conenction byte
        :param number:
        :param bt: hexa value or decimal number
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=connection-bytes=' + bt] )
        return ipv6

    def setConnectionRatioFilter(self,number,ratio="0-4294967295"):
        """
        Method will set connectionr atio
        :param number:
        :param ratio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-rate=' + ratio] )
        return ipv6

    def setConnectionRatioMangle(self, number, ratio="0-4294967295"):
        """
        Method will set connectionr atio
        :param number:
        :param ratio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-rate=' + ratio] )
        return ipv6

    def setPerConnectionClassifierFilter(self,number,classif="src-address:1/0"):
        """
        Method will set classifier
        :param number:
        :param classif: both-addresses,both-adresses-and-ports,both-ports,dst-address,dst-address-and-port,dst-port,src-address,src-address-and-port,src-port:1/0
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=per-connection-classifier=' + classif] )
        return ipv6

    def setPerConnectionClassifierMangle(self, number, classif="src-address:1/0"):
        """
        Method will set classifier
        :param number:
        :param classif: both-addresses,both-adresses-and-ports,both-ports,dst-address,dst-address-and-port,dst-port,src-address,src-address-and-port,src-port:1/0
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=per-connection-classifier=' + classif] )
        return ipv6

    def setPerConnectionClassifierRaw(self, number, classif="src-address:1/0"):
        """
        Method will set classifier
        :param number:
        :param classif: both-addresses,both-adresses-and-ports,both-ports,dst-address,dst-address-and-port,dst-port,src-address,src-address-and-port,src-port:1/0
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/raw/set', '=numbers=' + number, '=per-connection-classifier=' + classif] )
        return ipv6

    def setSrcMacAddressFilter(self,number,mac):
        """
        Method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ipv6

    def setSrcMacAddressMangle(self, number, mac):
        """
        Method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ipv6

    def setSrcMacAddressRaw(self, number, mac):
        """
        Method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ipv6

    def setOutBrifgePortFilter(self,number,port="ether1"):
        """
        Method will set out bridge port
        :param number:
        :param port: all-ppp,all-vlan,all-wireless,ether1
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=out-bridge-port=' + port] )
        return ipv6

    def setOutBrifgePortMangle(self, number, port="ether1"):
        """
        Method will set out bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=out-bridge-port=' + port] )
        return ipv6

    def setInBridgePortFilter(self,number,port):
        """
        Method will set in bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1, all-ethernet
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=in-bridge-port=' + port] )
        return ipv6

    def setInBridgePortMangle(self, number, port):
        """
        Method will set in bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1, all-ethernet
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=in-bridge-port=' + port] )
        return ipv6

    def setInBridgePortListFilter(self,number,port="all"):
        """
        Method will set in bridge list
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=in-bridge-port-list=' + port] )
        return ipv6

    def setInBridgePortListMangle(self, number, port="all"):
        """
        Method will set in bridge list
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=in-bridge-port-list=' + port] )
        return ipv6

    def setOutInterfaceBridgeListFilter(self,number,port="all"):
        """
        Method will set out bridge list
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=out-bridge-port-list=' + port] )
        return ipv6

    def setOutInterfaceBridgeListMangle(self, number, port="all"):
        """
        Method will set out bridge list
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=out-bridge-port-list=' + port] )
        return ipv6

    def setIpsecPolicyFilter(self,number,policy="in:none"):
        """
        Method will set ipsec policy
        :param number:
        :param policy: in out : none, ipsec
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=ipsec-policy=' + policy] )
        return ipv6

    def setIpsecPolicyMangle(self, number, policy="in:none"):
        """
        Method will set ipsec policy
        :param number:
        :param policy: in out : none, ipsec
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=ipsec-policy=' + policy] )
        return ipv6

    def setIpsecPolicyRaw(self, number, policy="in:none"):
        """
        Method will set ipsec policy
        :param number:
        :param policy: in out : none, ipsec
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=ipsec-policy=' + policy] )
        return ipv6

    def setIngressPriorityFilter(self,number,prio="0"):
        """
        Method will set ingress priority
        :param number:
        :param prio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ipv6

    def setIngressPriorityMAngle(self, number, prio="0"):
        """
        Method will set ingress priority
        :param number:
        :param prio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ipv6

    def setIngressPriorityRaw(self, number, prio="0"):
        """
        Method will set ingress priority
        :param number:
        :param prio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ipv6

    def setPriorityFilter(self,number,prio):
        """
        Method will set priority of rule
        :param number:
        :param prio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=priority=' + prio] )
        return ipv6

    def setPriorityMangle(self, number, prio):
        """
        Method will set priority of rule
        :param number:
        :param prio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=priority=' + prio] )
        return ipv6

    def setPriorityRaw(self, number, prio):
        """
        Method will set priority of rule
        :param number:
        :param prio:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=priority=' + prio] )
        return ipv6

    def setDscpFilter(self,number,dscp="0"):
        """
        Method will set dscp value
        :param number:
        :param dscp:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=dscp=' + dscp] )
        return ipv6

    def setDscpMangle(self, number, dscp="0"):
        """
        Method will set dscp value
        :param number:
        :param dscp:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=dscp=' + dscp] )
        return ipv6

    def setDscpRaw(self, number, dscp="0"):
        """
        Method will set dscp value
        :param number:
        :param dscp:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=dscp=' + dscp] )
        return ipv6

    def setTcpMssFilter(self,number,mss="1460-65535"):
        """
        Method will set tcp mss, tcp flags must be enabled before that!
        :param number:
        :param mss:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=tcp-mss=' + mss] )
        return ipv6

    def setTcpMssMangle(self, number, mss="1460-65535"):
        """
        Method will set tcp mss
        :param number:
        :param mss:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=tcp-mss=' + mss] )
        return ipv6

    def setTcpMssRaw(self, number, mss="1460-65535"):
        """
        Method will set tcp mss
        :param number:
        :param mss:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=tcp-mss=' + mss] )
        return ipv6

    def setPacketSizeFilter(self,number,packet="0-65535"):
        """
        Method will set packet size
        :param number:
        :param packet:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=packet-size=' + packet] )
        return ipv6

    def setPacketSizeMangle(self, number, packet="0-65535"):
        """
        Method will set packet size
        :param number:
        :param packet:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=packet-size=' + packet] )
        return ipv6

    def setPacketSizeRaw(self, number, packet="0-65535"):
        """
        Method will set packet size
        :param number:
        :param packet:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=packet-size=' + packet] )
        return ipv6

    def setRandomFilter(self,number,filt="50"):
        """
        Methodwill set random value
        :param number:
        :param filt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=random=' + filt] )
        return ipv6

    def setRandomMangle(self, number, filt="50"):
        """
        Methodwill set random value
        :param number:
        :param filt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=random=' + filt] )
        return ipv6

    def setRandomRaw(self, number, filt="50"):
        """
        Methodwill set random value
        :param number:
        :param filt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=random=' + filt] )
        return ipv6

    def setTcpFlagsFilter(self,number,flag="ack"):
        """
        Method will set tcp flag
        :param number:
        :param flag: ack,syn,cwr,ece,fin,psh,rst,urg
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=tcp-flags=' + flag] )
        return ipv6

    def setTcpFlagsMangle(self, number, flag="ack"):
        """
        Method will set tcp flag
        :param number:
        :param flag: ack,syn,cwr,ece,fin,psh,rst,urg
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=tcp-flags=' + flag] )
        return ipv6

    def setTcpFlagsRaw(self, number, flag="ack"):
        """
        Method will set tcp flag
        :param number:
        :param flag: ack,syn,cwr,ece,fin,psh,rst,urg
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=tcp-flags=' + flag] )
        return ipv6

    def setInvertTcpFlagsFilter(self,number,flag):
        """
        Methodwill invert tcp flag
        :param number:
        :param flag:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=tcp-flags=!,' + flag] )
        return ipv6

    def setInvertTcpFlagsMangle(self, number, flag):
        """
        Methodwill invert tcp flag
        :param number:
        :param flag:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=tcp-flags=!,' + flag] )
        return ipv6

    def setInvertTcpFlagsRaw(self, number, flag):
        """
        Methodwill invert tcp flag
        :param number:
        :param flag:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=tcp-flags=!,' + flag] )
        return ipv6