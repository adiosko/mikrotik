from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallGeneralSetup:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setChainFilter(self,number,chain="input"):
        """
        Method will set chain
        :param number:
        :param chain: filter: input, output, forward
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set','=numbers=number','=chain='+chain])
        return ipv6

    def setChainMangle(self, number, chain="prerouting"):
        """
        Method will set chain
        :param number:
        :param chain: filter: forward,input,output,prerouting,postrouting
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=number', '=chain=' + chain] )
        return ipv6

    def setChainRaw(self, number, chain="prerouting"):
        """
        Method will set chain
        :param number:
        :param chain: prerouting, output
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=number', '=chain=' + chain] )
        return ipv6

    def setSrcAddressFilter(self,number,src):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set','=numbers='+number,'=src-address='+src])
        return ipv6

    def setSrcAddressMangle(self, number, src):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=src-address=' + src] )
        return ipv6

    def setSrcAddressRaw(self, number, src):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=src-address=' + src] )
        return ipv6

    def setDstAddressFilter(self, number, dst):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ipv6

    def setDstAddressMangle(self, number, dst):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ipv6

    def setDstAddressRaw(self, number, dst):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ipv6

    def setProtocolFilter(self,number,protocol="tcp"):
        """
        Method will set protocol
        :param number:
        :param protocol: tcp udp to negate use !
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ipv6

    def setProtocolMangle(self, number, protocol="tcp"):
        """
        Method will set protocol to negate use !
        :param number:
        :param protocol: tcp udp
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ipv6

    def setProtocolRaw(self, number, protocol="tcp"):
        """
        Method will set protocol to negate use !
        :param number:
        :param protocol: tcp udp
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ipv6

    def setSrcPortFIlter(self,number,port):
        """
        Method will set src port also !
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=src-port=' + port] )
        return ipv6

    def setSrcPortMangle(self, number, port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=src-port=' + port] )
        return ipv6

    def setSrcPortRaw(self, number, port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=src-port=' + port] )
        return ipv6

    def setDstPortFilter(self,number,port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=dst-port=' + port] )
        return ipv6

    def setDstPortMangle(self, number, port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=dst-port=' + port] )
        return ipv6

    def setDstPortRaw(self, number, port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=dst-port=' + port] )
        return ipv6

    def setAnyPortFilter(self,number,port):
        """
        Methodwill set any port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=port=' + port] )
        return ipv6

    def setAnyPortMangle(self, number, port):
        """
        Methodwill set any port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=port=' + port] )
        return ipv6

    def setAnyPortRaw(self, number, port):
        """
        Methodwill set any port
        :param number:
        :param port:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=port=' + port] )
        return ipv6

    def setInInterfaceFilter(self,number,iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ipv6

    def setInInterfaceMangle(self, number, iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ipv6

    def setInInterfaceRaw(self, number, iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ipv6

    def setOutInterfaceFilter(self,number,iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ipv6

    def setOutInterfaceMangle(self, number, iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ipv6

    def setOutInterfaceRaw(self, number, iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ipv6

    def setInInterfaceListFilter(self,number,ilist="all"):
        """
        Method will set in interface list all or custom
        :param number:
        :param ilist:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=in-interface-list=' + ilist] )
        return ipv6

    def setInInterfaceListMangle(self, number, ilist="all"):
        """
        Method will set in interface list all or custom
        :param number:
        :param ilist:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=in-interface-list=' + ilist] )
        return ipv6

    def setInInterfaceListRaw(self, number, ilist="all"):
        """
        Method will set in interface list all or custom
        :param number:
        :param ilist:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=in-interface-list=' + ilist] )
        return ipv6

    def setOutInterfaceListFilter(self,number,olist="all"):
        """
        Method will set out interface list
        :param number:
        :param olist:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=out-interface-list=' + olist] )
        return ipv6

    def setOutInterfaceListMangle(self, number, olist="all"):
        """
        Method will set out interface list
        :param number:
        :param olist:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=out-interface-list=' + olist] )
        return ipv6

    def setOutInterfaceListRaw(self, number, olist="all"):
        """
        Method will set out interface list
        :param number:
        :param olist:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=out-interface-list=' + olist] )
        return ipv6

    def setPacketMarkFilter(self,number,filter="no-mark"):
        """
        Method will set packet amrk
        :param number:
        :param filter: 0x2 f.e.
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=packet-mark=' + filter] )
        return ipv6

    def setPacketMarkMangle(self, number, filter="no-mark"):
        """
        Method will set packet amrk
        :param number:
        :param filter: 0x2 f.e.
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=packet-mark=' + filter] )
        return ipv6

    def setConnectionMarkFilter(self,number,filter="no-mark"):
        """
        Method will set connection mark
        :param number:
        :param filter: 0x2
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-mark=' + filter] )
        return ipv6

    def setConnectionMarkMangle(self, number, filter="no-mark"):
        """
        Method will set connection mark
        :param number:
        :param filter: 0x2
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=connection-mark=' + filter] )
        return ipv6

    def setConnectionTypeFilter(self,number,conn="ftp"):
        """
        Method will set conenction tyoe
        :param number:
        :param conn: ftp,h323,irc,pptp,quake3,sip,tftp
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-type=' + conn] )
        return ipv6

    def setConnectionTypeMangle(self, number, conn="ftp"):
        """
        Method will set conenction tyoe
        :param number:
        :param conn: ftp,h323,irc,pptp,quake3,sip,tftp
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=connection-type=' + conn] )
        return ipv6

    def setConenctionStateFilter(self,number,state="established,related"):
        """
        Method will set conenction state
        :param number:
        :param state: !,invalid,established,related,new,untracked
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-state=' + state] )
        return ipv6

    def setConenctionStateMangle(self, number, state="established,related"):
        """
        Method will set conenction state
        :param number:
        :param state: !,invalid,established,related,new,untracked
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=connection-state=' + state] )
        return ipv6













