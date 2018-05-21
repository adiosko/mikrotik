from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallAdvancedSetup:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setSrcAddressListFilter(self,number,addr):
        """
        Method will set src address list
        :param number:
        :param addr: name of list
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=src-address-list='+addr])
        return ip

    def setSrcAddressMangle(self, number, addr):
        """
        Method will set src address list
        :param number:
        :param addr: name of list
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=src-address-list=' + addr] )
        return ip

    def setSrcAddressListnat(self, number, addr):
        """
        Method will set src address list
        :param number:
        :param addr: name of list
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=src-address-list=' + addr] )
        return ip

    def setDstAddressListFilter(self,number,addr):
        """
        method will set address list
        :param number:
        :param addr:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=dst-address-list=' + addr] )
        return ip

    def setDstAddressListNat(self, number, addr):
        """
        method will set address list
        :param number:
        :param addr:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=dst-address-list=' + addr] )
        return ip

    def setDstAddressListMangle(self, number, addr):
        """
        method will set address list
        :param number:
        :param addr:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=dst-address-list=' + addr] )
        return ip

    def setL7ProtocolFilter(self,number,protoc):
        """
        Method will set l7 protocol
        :param number:
        :param protoc: ccreated in l7 protocols class
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=layer7-protocol='+protoc])
        return ip

    def setL7ProtocolMangle(self, number, protoc):
        """
        Method will set l7 protocol
        :param number:
        :param protoc: ccreated in l7 protocols class
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=layer7-protocol=' + protoc] )
        return ip

    def setL7ProtocolNat(self, number, protoc):
        """
        Method will set l7 protocol
        :param number:
        :param protoc: ccreated in l7 protocols class
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=layer7-protocol=' + protoc] )
        return ip

    def setContentFilter(self,number,cont="0"):
        """
        Method will set fw content
        :param number:
        :param cont:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=content=' + cont] )
        return ip

    def setContentMangle(self, number, cont="0"):
        """
        Method will set fw content
        :param number:
        :param cont:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=content=' + cont] )
        return ip

    def setContentnat(self, number, cont="0"):
        """
        Method will set fw content
        :param number:
        :param cont:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=content=' + cont] )
        return ip

    def setCOnnectionByteFilter(self,number,bt="0"):
        """
        Method will set conenction byte
        :param number:
        :param bt: hexa value or decimal number
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=connection-bytes=' + bt] )
        return ip

    def setCOnnectionByteMangle(self, number, bt="0"):
        """
        Method will set conenction byte
        :param number:
        :param bt: hexa value or decimal number
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-bytes=' + bt] )
        return ip

    def setCOnnectionByteNat(self, number, bt="0"):
        """
        Method will set conenction byte
        :param number:
        :param bt: hexa value or decimal number
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=connection-bytes=' + bt] )
        return ip

    def setConnectionRatioFilter(self,number,ratio="0-4294967295"):
        """
        Method will set connectionr atio
        :param number:
        :param ratio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=connection-rate=' + ratio] )
        return ip

    def setConnectionRatioMangle(self, number, ratio="0-4294967295"):
        """
        Method will set connectionr atio
        :param number:
        :param ratio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-rate=' + ratio] )
        return ip

    def setConnectionRatioNat(self, number, ratio="0-4294967295"):
        """
        Method will set connectionr atio
        :param number:
        :param ratio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=connection-rate=' + ratio] )
        return ip

    def setPerConnectionClassifierFilter(self,number,classif="src-address:1/0"):
        """
        Method will set classifier
        :param number:
        :param classif: both-addresses,both-adresses-and-ports,both-ports,dst-address,dst-address-and-port,dst-port,src-address,src-address-and-port,src-port:1/0
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=per-connection-classifier=' + classif] )
        return ip

    def setPerConnectionClassifierMangle(self, number, classif="src-address:1/0"):
        """
        Method will set classifier
        :param number:
        :param classif: both-addresses,both-adresses-and-ports,both-ports,dst-address,dst-address-and-port,dst-port,src-address,src-address-and-port,src-port:1/0
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=per-connection-classifier=' + classif] )
        return ip

    def setPerConnectionClassifiernat(self, number, classif="src-address:1/0"):
        """
        Method will set classifier
        :param number:
        :param classif: both-addresses,both-adresses-and-ports,both-ports,dst-address,dst-address-and-port,dst-port,src-address,src-address-and-port,src-port:1/0
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set', '=numbers=' + number, '=per-connection-classifier=' + classif] )
        return ip

    def setSrcMacAddressFilter(self,number,mac):
        """
        Method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ip

    def setSrcMacAddressMangle(self, number, mac):
        """
        Method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ip

    def setSrcMacAddressnat(self, number, mac):
        """
        Method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ip

    def setOutBrifgePortFilter(self,number,port="ether1"):
        """
        Method will set out bridge port
        :param number:
        :param port: all-ppp,all-vlan,all-wireless,ether1
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=out-bridge-port=' + port] )
        return ip

    def setOutBrifgePortMangle(self, number, port="ether1"):
        """
        Method will set out bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=out-bridge-port=' + port] )
        return ip

    def setOutBrifgePortNat(self, number, port="ether1"):
        """
        Method will set out bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=out-bridge-port=' + port] )
        return ip

    def setInBridgePortFilter(self,number,port):
        """
        Method will set in bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1, all-ethernet
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=in-bridge-port=' + port] )
        return ip

    def setInBridgePortMangle(self, number, port):
        """
        Method will set in bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1, all-ethernet
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=in-bridge-port=' + port] )
        return ip

    def setInBridgePortNat(self, number, port):
        """
        Method will set in bridge port
        :param number:
        :param port:all-ppp,all-vlan,all-wireless,ether1, all-ethernet
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=in-bridge-port=' + port] )
        return ip

    def setIPsecPolicyFilter(self,number,policy="in:ipsec"):
        """
        Method will set ipsec policy
        :param number:
        :param policy: in,out ,none,ipsec
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=ipsec-policy='+policy])
        return ip

    def setIPsecPolicyMangle(self, number, policy="in:ipsec"):
        """
        Method will set ipsec policy
        :param number:
        :param policy: in,out ,none,ipsec
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=ipsec-policy=' + policy] )
        return ip

    def setIPsecPolicyNat(self, number, policy="in:ipsec"):
        """
        Method will set ipsec policy
        :param number:
        :param policy: in,out ,none,ipsec
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=ipsec-policy=' + policy] )
        return ip

    def setIngressPriorityFilter(self,number,prio="0"):
        """
        Method will set ingress priority
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ip

    def setIngressPriorityMAngle(self, number, prio="0"):
        """
        Method will set ingress priority
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ip

    def setIngressPrioritynat(self, number, prio="0"):
        """
        Method will set ingress priority
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ip

    def setPriorityFilter(self,number,prio):
        """
        Method will set priority of rule
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=priority=' + prio] )
        return ip

    def setPriorityMangle(self, number, prio):
        """
        Method will set priority of rule
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=priority=' + prio] )
        return ip

    def setPrioritynat(self, number, prio):
        """
        Method will set priority of rule
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=priority=' + prio] )
        return ip

    def setDscpFilter(self,number,dscp="0"):
        """
        Method will set dscp value
        :param number:
        :param dscp:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=dscp=' + dscp] )
        return ip

    def setDscpMangle(self, number, dscp="0"):
        """
        Method will set dscp value
        :param number:
        :param dscp:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=dscp=' + dscp] )
        return ip

    def setDscpnat(self, number, dscp="0"):
        """
        Method will set dscp value
        :param number:
        :param dscp:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=dscp=' + dscp] )
        return ip

    def setTcpMssFilter(self,number,mss="1460-65535"):
        """
        Method will set tcp mss, tcp flags must be enabled before that!
        :param number:
        :param mss:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=tcp-mss=' + mss] )
        return ip

    def setTcpMssMangle(self, number, mss="1460-65535"):
        """
        Method will set tcp mss
        :param number:
        :param mss:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=tcp-mss=' + mss] )
        return ip

    def setTcpMssnat(self, number, mss="1460-65535"):
        """
        Method will set tcp mss
        :param number:
        :param mss:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=tcp-mss=' + mss] )
        return ip

    def setPacketSizeFilter(self,number,packet="0-65535"):
        """
        Method will set packet size
        :param number:
        :param packet:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=packet-size=' + packet] )
        return ip

    def setPacketSizeMangle(self, number, packet="0-65535"):
        """
        Method will set packet size
        :param number:
        :param packet:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=packet-size=' + packet] )
        return ip

    def setPacketSizenat(self, number, packet="0-65535"):
        """
        Method will set packet size
        :param number:
        :param packet:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=packet-size=' + packet] )
        return ip

    def setRandomFilter(self,number,filt="50"):
        """
        Methodwill set random value
        :param number:
        :param filt:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=random=' + filt] )
        return ip

    def setRandomMangle(self, number, filt="50"):
        """
        Methodwill set random value
        :param number:
        :param filt:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=random=' + filt] )
        return ip

    def setRandomnat(self, number, filt="50"):
        """
        Methodwill set random value
        :param number:
        :param filt:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=random=' + filt] )
        return ip

    def setTcpFlagsFilter(self,number,flag="ack"):
        """
        Method will set tcp flag
        :param number:
        :param flag: ack,syn,cwr,ece,fin,psh,rst,urg
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=tcp-flags=' + flag] )
        return ip

    def setTcpFlagsMangle(self, number, flag="ack"):
        """
        Method will set tcp flag
        :param number:
        :param flag: ack,syn,cwr,ece,fin,psh,rst,urg
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=tcp-flags=' + flag] )
        return ip

    def setTcpFlagsnat(self, number, flag="ack"):
        """
        Method will set tcp flag
        :param number:
        :param flag: ack,syn,cwr,ece,fin,psh,rst,urg
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=tcp-flags=' + flag] )
        return ip

    def setInvertTcpFlagsFilter(self,number,flag):
        """
        Methodwill invert tcp flag
        :param number:
        :param flag:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=tcp-flags=!,' + flag] )
        return ip

    def setInvertTcpFlagsMangle(self, number, flag):
        """
        Methodwill invert tcp flag
        :param number:
        :param flag:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=tcp-flags=!,' + flag] )
        return ip

    def setInvertTcpFlagsnat(self, number, flag):
        """
        Methodwill invert tcp flag
        :param number:
        :param flag:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=tcp-flags=!,' + flag] )
        return ip

    def setIcmpOptionsFilter(self,number,icmp="any"):
        """
        Method will set icmp options
        :param number:
        :param icmp: any,loose-source-routing,no-record-route,no-router-alert,no-source-routing,no-timestamp,none,record-route,router-alert,strict-source-routing,timestamp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=ipv4-options=' + icmp] )
        return ip

    def setIcmpOptionsNat(self, number, icmp="any"):
        """
        Method will set icmp options
        :param number:
        :param icmp: any,loose-source-routing,no-record-route,no-router-alert,no-source-routing,no-timestamp,none,record-route,router-alert,strict-source-routing,timestamp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=ipv4-options=' + icmp] )
        return ip

    def setIcmpOptionsMangle(self, number, icmp="any"):
        """
        Method will set icmp options
        :param number:
        :param icmp: any,loose-source-routing,no-record-route,no-router-alert,no-source-routing,no-timestamp,none,record-route,router-alert,strict-source-routing,timestamp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=ipv4-options=' + icmp] )
        return ip

    def setIcmpTtlFilter(self,number,ttl="equal:0"):
        """
        Method will se tttl for icmp
        :param number:
        :param ttl: equal,greater-than,less-than,not-equal:number
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=ttl=' + ttl] )
        return ip

    def setIcmpTtlNat(self, number, ttl="equal:0"):
        """
        Method will se tttl for icmp
        :param number:
        :param ttl: equal,greater-than,less-than,not-equal:number
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=ttl=' + ttl] )
        return ip

    def setIcmpTtlMangle(self, number, ttl="equal:0"):
        """
        Method will se tttl for icmp
        :param number:
        :param ttl: equal,greater-than,less-than,not-equal:number
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=ttl=' + ttl] )
        return ip





