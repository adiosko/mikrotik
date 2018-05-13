from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPv6NeighborDiscovery:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list interfaces
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/nd/print'])
        if ipv6 == {}:
            print("No interface found")
        else:
            print("Interface\tRA interface\tRA Delay\tRA Lifetime\tadvertise MAC\tAdvertise DNS")
            for i in ipv6:
                #print(ipv6[i])
                print(ipv6[i]['interface']+"\t"+ipv6[i]['ra-interval']+"\t"+ipv6[i]['ra-lifetime']+"\t"+ipv6[i]['advertise-mac-address']+"\t"+ipv6[i]['advertise-dns'])
        return ipv6

    def addInterface(self):
        """
        Method will add interface
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/add'] )
        return ipv6

    def removeInterface(self,number):
        """
        Method wil lremove interface
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/remove','=numbers='+number] )
        return ipv6

    def enableInterface(self,number):
        """
        Method will enable interface
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/enable','=numbers='+number] )
        return ipv6

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/disable','=numbers='+number] )
        return ipv6

    def setInterface(self,number,interface="all"):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number,'=interface='+interface] )
        return ipv6

    def setRaInterval(self,number,interval="200-600"):
        """
        Method will set ra interval in seconds
        :param number:
        :param interval:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number,'=ra-interval='+interval] )
        return ipv6

    def setRaDelay(self,number,delay="3"):
        """
        Method will set delay in secs
        :param number:
        :param delay:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=ra-delay=' + delay] )
        return ipv6

    def setMtu(self,number,mtu="1500"):
        """
        Method will set mtu
        :param number:
        :param mtu:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=mtu=' + mtu] )
        return ipv6

    def setRachableTime(self,number,timeout="0"):
        """
        Method will set timeout
        :param number:
        :param timeout:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=reachable-time=' + timeout] )
        return ipv6

    def  setRetransmitInterval(self,number,interval="0"):
        """
        Method will set retransmit interval
        :param number:
        :param interval:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=retransmit-interval=' + interval] )
        return ipv6

    def setRaLifetime(self,number,life="1800"):
        """
        Method will set ra lifetime in secs
        :param number:
        :param life:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=ra-lifetime=' + life] )
        return ipv6

    def setHopLimit(self,number,limit="64"):
        """
        Method will set hop limit in secs
        :param number:
        :param limit:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=hop-limit=' + limit] )
        return ipv6

    def setAdvertiseMacAddress(self,number):
        """
        Method will advertise mac
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=advertise-mac-address=yes'] )
        return ipv6

    def setAdvertiseDns(self,number):
        """
        Method will advertise dns
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=advertise-dns=yes'] )
        return ipv6

    def setManagedAddressConfiguration(self,number):
        """
        Method will set managed address config
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=managed-address-configuration=yes'] )
        return ipv6

    def setOtherConfiguration(self,number):
        """
        Method will set other configuration
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/set', '=numbers=' + number, '=other-configuration=yes'] )
        return ipv6
    #Prefixes
    def setDefaultAutonomous(self):
        """
        Method will set autinomous nd
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/nd/prefix/default/set','=autonomous=yes'])
        return ipv6

    def setValidLifetime(self,lifetime="30d 00:00:00"):
        """
        Method will set valid lifetime
        :param number:
        :param lifetime:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/default/set', '=valid-lifetime='+lifetime] )
        return ipv6

    def setPrefferedLifetime(self,lifetime="7d 00:00:00"):
        """
        Method will set preff lifetime
        :param lifetime:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/default/set', '=preferred-lifetime='+lifetime] )
        return ipv6

    #prefixes all
    def listPrefixes(self):
        """
        Method will list prefixes
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/print'] )
        if ipv6 == {}:
            print("No prefix found")
        else:
            print("Prefix\tInterface")
            for i in ipv6:
                print(ipv6[i]['prefix']+"\t"+ipv6[i]['interface'])
        return ipv6

    def addPrefix(self,interface="ether1"):
        """
        Method will add prefix baed on source interface
        :param interface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/add', '=interface='+interface] )
        return ipv6

    def removePrefix(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/remove', '=numbers='+number] )
        return ipv6

    def enablePrefix(self,number):
        """
        Method wil
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/enable', '=numbers='+number] )
        return ipv6

    def disablePrefix(self,number):
        """
        Method will disable rpefix
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/disable', '=numbers='+number] )
        return ipv6

    def setPrefix(self,number,prefix="::/0"):
        """
        Method will set prefix
        :param number:
        :param prefix:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/nd/prefix/set','=numbers='+number,'=prefix='+prefix])
        return ipv6

    def set6to4Interface(self,number,interface="ether1"):
        """
        Method will set 6to4 iface
        :param number:
        :param interface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/set', '=numbers=' + number, '=6to4-interface=' + interface] )
        return ipv6

    def setPrefixInterface(self,number,interface="ether1"):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/set', '=numbers=' + number, '=interface=' + interface] )
        return ipv6

    def setOnLink(self,number):
        """
        Method will set interface on-link
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/set', '=numbers=' + number, '=on-link=yes'] )
        return ipv6

    def setAutonomous(self,number):
        """
        Method will set prefix autonomous
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/set', '=numbers=' + number, '=autonomous=yes'] )
        return ipv6

    def setCustomValidLifetime(self,number,life="30d 00:00:00"):
        """
        M
        :param number:
        :param life:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/default/set','=numbers='+number, '=valid-lifetime=' + life] )
        return ipv6

    def setCustomPrefferedLifetime(self,number,life="7d 00:00:00"):
        """
        Method will set preff lifetime
        :param number:
        :param life:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/nd/prefix/default/set', '=numbers=' + number, '=preferred-lifetime=' + life] )
        return ipv6