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
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers=number','=chain='+chain])
        return ip

    def setChainMangle(self, number, chain="prerouting"):
        """
        Method will set chain
        :param number:
        :param chain: filter: forward,input,output,prerouting,postrouting
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=number', '=chain=' + chain] )
        return ip

    def setChainnat(self, number, chain="prerouting"):
        """
        Method will set chain
        :param number:
        :param chain: prerouting, output
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=number', '=chain=' + chain] )
        return ip

    def setSrcAddressFilter(self,number,src):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=src-address='+src])
        return ip

    def setSrcAddressMangle(self, number, src):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=src-address=' + src] )
        return ip

    def setSrcAddressnat(self, number, src):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=src-address=' + src] )
        return ip

    def setDstAddressFilter(self, number, dst):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ip

    def setDstAddressMangle(self, number, dst):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ip

    def setDstAddressnat(self, number, dst):
        """
        Method will setsrc address
        :param number:
        :param src:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ip

    def setProtocolFilter(self,number,protocol="tcp"):
        """
        Method will set protocol
        :param number:
        :param protocol: tcp udp to negate use !
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ip

    def setProtocolMangle(self, number, protocol="tcp"):
        """
        Method will set protocol to negate use !
        :param number:
        :param protocol: tcp udp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ip

    def setProtocolnat(self, number, protocol="tcp"):
        """
        Method will set protocol to negate use !
        :param number:
        :param protocol: tcp udp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ip

    def setSrcPortFIlter(self,number,port):
        """
        Method will set src port also !
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=src-port=' + port] )
        return ip

    def setSrcPortMangle(self, number, port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=src-port=' + port] )
        return ip

    def setSrcPortnat(self, number, port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=src-port=' + port] )
        return ip

    def setDstPortFilter(self,number,port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=dst-port=' + port] )
        return ip

    def setDstPortMangle(self, number, port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=dst-port=' + port] )
        return ip

    def setDstPortnat(self, number, port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=dst-port=' + port] )
        return ip

    def setAnyPortFilter(self,number,port):
        """
        Methodwill set any port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=port=' + port] )
        return ip

    def setAnyPortMangle(self, number, port):
        """
        Methodwill set any port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=port=' + port] )
        return ip

    def setAnyPortnat(self, number, port):
        """
        Methodwill set any port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=port=' + port] )
        return ip

    def setInInterfaceFilter(self,number,iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ip

    def setInInterfaceMangle(self, number, iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ip

    def setInInterfacenat(self, number, iface):
        """
        Method will set source iface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=in-interface=' + iface] )
        return ip

    def setOutInterfaceFilter(self,number,iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ip

    def setOutInterfaceMangle(self, number, iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ip

    def setOutInterfacenat(self, number, iface):
        """
        Methodw ill set out interface
        :param number:
        :param iface:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=out-interface=' + iface] )
        return ip

    def setP2PFilter(self,number,filter="all-p2p"):
        """
        Method will set p2p filter
        :param number:
        :param filter: all-p2p,bit-torrent,blubster,direct-connect,edonkey,fastrack,gnutella,soulseek,warez,winmx
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=p2p=' + filter] )
        return ip

    def setP2PMangle(self, number, filter="all-p2p"):
        """
        Method will set p2p filter
        :param number:
        :param filter: all-p2p,bit-torrent,blubster,direct-connect,edonkey,fastrack,gnutella,soulseek,warez,winmx
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=p2p=' + filter] )
        return ip

    def setPacketMarkFilter(self,number,filter="no-mark"):
        """
        Method will set packet amrk
        :param number:
        :param filter: 0x2 f.e.
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=packet-mark=' + filter] )
        return ip

    def setPacketMarkMangle(self, number, filter="no-mark"):
        """
        Method will set packet amrk
        :param number:
        :param filter: 0x2 f.e.
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=packet-mark=' + filter] )
        return ip

    def setConnectionMarkFilter(self,number,filter="no-mark"):
        """
        Method will set connection mark
        :param number:
        :param filter: 0x2
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=connection-mark=' + filter] )
        return ip

    def setConnectionMarkMangle(self, number, filter="no-mark"):
        """
        Method will set connection mark
        :param number:
        :param filter: 0x2
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-mark=' + filter] )
        return ip

    def setRoutingMarkFilter(self,number,filter="main"):
        """
        Method will set conenction amrk
        :param number:
        :param filter:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=routing-mark='+filter])
        return ip

    def setRoutingMarkMangle(self, number, filter="main"):
        """
        Method will set conenction amrk
        :param number:
        :param filter:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=routing-mark=' + filter] )
        return ip

    def setRoutingMarkNat(self, number, filter="main"):
        """
        Method will set conenction amrk
        :param number:
        :param filter:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=routing-mark=' + filter] )
        return ip

    def setRoutingTableFilter(self,number,table="main"):
        """
        Method will set routing table
        :param number:
        :param table:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=routing-table='+table])
        return ip

    def setRoutingTableMangle(self, number, table="main"):
        """
        Method will set routing table
        :param number:
        :param table:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=routing-table=' + table] )
        return ip

    def setRoutingTableNat(self, number, table="main"):
        """
        Method will set routing table
        :param number:
        :param table:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=routing-table=' + table] )
        return ip

    def setConnectionTypeFilter(self,number,conn="ftp"):
        """
        Method will set conenction tyoe
        :param number:
        :param conn: ftp,h323,irc,pptp,quake3,sip,tftp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=connection-type=' + conn] )
        return ip

    def setConnectionTypeMangle(self, number, conn="ftp"):
        """
        Method will set conenction tyoe
        :param number:
        :param conn: ftp,h323,irc,pptp,quake3,sip,tftp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-type=' + conn] )
        return ip

    def setConnectionTypeNat(self, number, conn="ftp"):
        """
        Method will set conenction tyoe
        :param number:
        :param conn: ftp,h323,irc,pptp,quake3,sip,tftp
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=connection-type=' + conn] )
        return ip

    def setConenctionStateFilter(self,number,state="established,related"):
        """
        Method will set conenction state
        :param number:
        :param state: !,invalid,established,related,new,untracked
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=connection-state=' + state] )
        return ip

    def setConenctionStateMangle(self, number, state="established,related"):
        """
        Method will set conenction state
        :param number:
        :param state: !,invalid,established,related,new,untracked
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-state=' + state] )
        return ip

    def setCOnnectionStateNAtFilter(self,number,filter="srcnat"):
        """
        Method wil lset conenction state for nat
        :param number:
        :param filter:!,srcnat,dstnat
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=connection-nat-state='+filter])
        return ip

    def setCOnnectionStateNAtMangle(self, number, filter="srcnat"):
        """
        Method wil lset conenction state for nat
        :param number:
        :param filter:!,srcnat,dstnat
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-nat-state=' + filter] )
        return ip
















