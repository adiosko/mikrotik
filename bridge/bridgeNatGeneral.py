from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeNatGeneral:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setChain(self,number,chain="srcnat"):
        """
        Method will set chain
        :param number:
        :param chain: srcnat,dstnat
        :return:
        """
        nat = self.client.talk(['/interface/bridge/nat/set','=numbers='+number,'=chain='+chain])
        return nat

    def setInInterfaceFilter(self, number, iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ip

    def setOutInterface(self, number, iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ip

    def setInInterfaceList(self,number,ifaceList="all"):
        """
        Method will set in interface list
        :param number:
        :param ifaceList: all, none, dynamic
        :return:
        """
        ip = self.client.talk(['/interface/bridge/nat/set','=numbers='+number,'=in-interface-list='+ifaceList])
        return ip

    def setOutInterfaceList(self, number, ifaceList="all"):
        """
        Method will set in interface list
        :param number:
        :param ifaceList: all, none, dynamic
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=out-interface-list=' + ifaceList] )
        return ip

    def setInBridge(self, number, bridge):
        """
        Method will set in interface list
        :param number:
        :param bridge: all, none, dynamic
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=in-bridge=' + bridge] )
        return ip

    def setOutBridge(self, number, bridge):
        """
        Method will set in interface list
        :param number:
        :param bridge: all, none, dynamic
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=out-bridge=' + bridge] )
        return ip

    def setInBridgeList(self, number, bridgeList="all"):
        """
        Method will set in interface list
        :param number:
        :param bridge: all, none, dynamic,!
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=in-bridge-list=' + bridgeList] )
        return ip

    def setSrcMacAddress(self,number,mac):
        """
        method will set src mac address
        :param number:
        :param mac:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=src-mac-address=' + mac] )
        return ip

    def setDstMac(self,number,mac):
        """
        Method will set mac mask
        :param number:
        :param mask:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=dst-mac-address=' + mac] )
        return ip

    def setMacProtocol(self,number,protocol="ip"):
        """
        Method iwll set mac protocol
        :param number:
        :param protocol: 802.2,arp,homeplug,-av,ip,ipv6,ipx,length,lldp,loop-protect,mpls-multicats,mpls-unicats,packing-compr,packing-simple,pppoe,pppoe-discovery,rarp,service-vlan,vlan
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=mac-protocol=' + protocol] )
        return ip

    def setSrcAddress(self,number,src):
        """
        Method will set src address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=src-address=' + src] )
        return ip

    def setSrcPort(self,number,port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=src-port=' + port] )
        return ip

    def setDstAddress(self,number,dst):
        """
        Method will set dst address
        :param number:
        :param dst:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ip

    def setDstPort(self,number,port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=dst-port=' + port] )
        return ip

    def setProtocol(self,number,protocol="tcp"):
        """
        Method wil lset protocol
        :param number:
        :param protocol: dccp,ddp.egp,encap,etherip,ggp,gre,hmp,...
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=ip-protocol=' + protocol] )
        return ip

    def setTlsHost(self,number,host="4"):
        """
        Method will set tls field
        :param number:
        :param host:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=tls-host=' + host] )
        return ip

    def setPacketMark(self,number,packet):
        """
        Method will set packet mark
        :param number:
        :param packet:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=packet-mark=' + packet] )
        return ip

    def setIngressPriority(self,number,prio="0"):
        """
        Method will set inmgress priority
        :param number:
        :param prio:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=ingress-priority=' + prio] )
        return ip