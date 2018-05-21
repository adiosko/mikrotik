from tikapy import TikapyClient
from tikapy import TikapySslClient

class PacketSniffer:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSniffer(self):
        """
        Method will list sniffer stats
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/print'])
        if sniff == {}:
            print("No sniffer is running")
        else:
            for i in sniff:
                print(sniff)
        return sniff

    def startSniffer(self):
        """
        Method will start sniffer
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/start'])
        return sniff

    def stopSniffer(self):
        """
        Method will stop sniffer
        :return:
        """
        sniff = self.client.talk( ['/tool/sniffer/stop'] )
        return sniff

    def setSniffer(self,memoryLimit,onlyHeaders,memoryScroll,fileLimit,file=None):
        """
        opravit
        Method will set sniffer
        :param memoryLimit: 100 kb  default
        :param onlyHeaders: yes/no def no
        :param memoryScroll: def yes yes/no
        :param fileLimit: 1000 kb default
        :return:
        """
        if file == None:
            sniff = self.client.talk(['/tool/sniffer/set','=memory-limit='+memoryLimit,'=only-headers='+onlyHeaders,
                                      '=memory-scroll='+memoryScroll,'=file-limit'+fileLimit])
        else:
            sniff = self.client.talk(['/tool/sniffer/set', '=memory-limit=' + memoryLimit,
                                      '=only-headers='+onlyHeaders,'=memory-scroll='+memoryScroll,
                                      '=file-limit' + fileLimit,'=file-name='+file] )
        return sniff

    def showPackets(self):
        """
        Method will list all packets in interval
        :param interval: interval of packet usage
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/packet/print'])
        print(sniff)
        return sniff

    def showConnections(self):
        """
        Method will show all connection on sniffer
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/connection/print'])
        if sniff == {}:
            print("No connection established or server is not running")
        else:
            print("src address \t dst address \t bytes \t resends \t mss")
            for i in sniff:
                print(sniff[i]['src-address']+"\t"+sniff[i]['dst-address']+"\t"+sniff[i]['bytes']+"\t"
                      +sniff[i]['resends']+"\t"+sniff[i]['mss'])
        return sniff

    def showHosts(self):
        """
        Method will list all connected hosts
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/host/print'])
        if sniff == {}:
            print("No hosts found")
        else:
            print("address\trate\tpeekrate\ttotal")
            for i in sniff:
                print(sniff[i]['address']+"\t"+sniff[i]['rate']+"\t"+sniff[i]['peek-rate']+"\t"+sniff[i]['total'])
        return sniff

    def showProtocols(self,interval):
        """
        Method will list all protocols in session
        :param interval: interval on run
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/protocol/print','=interval='+interval])
        print(sniff)
        return sniff

    def enableStream(self,server,filter):
        """
        Method will enable stream
        :param server: server IP
        :param filter: yes/no def no
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=streaming-enabled=yes','=streaming-server='+server])
        return sniff

    def filterInterface(self,interface):
        """
        Method will filtersniffer interface
        :param interface: interface to filter
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-interface='+interface])
        return sniff

    def filterMacAddress(self,MAC):
        """
        Method will filter trafiic on mac address
        :param MAC: mac address to filter
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-mac-address='+MAC])
        return sniff

    def filterMacProtocol(self, MAC):
        """
        Method will filter trafiic on mac protocol
        :param MAC: mac protocol: 802.2,ip,lldp,mpls-unicast,pppoe,service-vlan,arp,ipv6,loop-protect,packing-compr,
        pppoe-discovery,vlan,homeplug-av,ipx,mpls-multicast,packing-simple,rarp
        :return:
        """
        sniff = self.client.talk( ['/tool/sniffer/set', '=filter-mac-protocol=' + MAC] )
        return sniff

    def filterIpaddress(self,IP):
        """
        Methd will filter traffic on IP address
        :param IP: IP to filter
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-ip-address='+IP])
        return sniff

    def filterIpv6Address(self,IPv6):
        """
        Method will filter Ipv6 address
        :param IPv6: Ipv6 address to filter
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-ipv6-address='+IPv6])
        return sniff

    def filterIpProtocol(self,protocol):
        """
        Method to set filer on IP protocol
        :param protocol: icmp, igmp, ggp, ip-encap, tcp,egp, pup, udp, ipsec, ospf
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-ip-protocol='+protocol])
        return sniff

    def filterPort(self,port):
        """
        Method will filter protocol all protocol f.e ssh,
        :param port: netstat, ssh, telnet, ftp, smtp, etc.
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-port='+port])
        return sniff

    def filterCPU(self,CPU):
        """
        Method will filter CPU
        :param CPU: standardly cpu0
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-cpu='+CPU])
        return sniff

    def filterDirection(self,direction):
        """
        Method will filter direction
        :param direction: any, rx,tx
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-direction='+direction])
        return sniff

    def filterOperation(self,operation):
        """
        Method will filter opeartion of filter
        :param operation:  and or or
        :return:
        """
        sniff = self.client.talk(['/tool/sniffer/set','=filter-operator-between-entries='+operation])
        return sniff