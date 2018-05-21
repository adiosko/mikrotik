from tikapy import TikapyClient
from tikapy import TikapySslClient

class DhcpServer:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listServers(self):
        """
        Method will list servers
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/print'])
        if ipv6 == {}:
            print("No server found")
        else:
            print("Name\tInterface\tLeaseTime")
            for i in ipv6:
                print(ipv6[i]['name']+"\t"+ipv6[i]['interface']+"\t"+ipv6[i]['lease-time'])
        return ipv6

    def addServer(self,interface,name,pool):
        """
        Method will add dhcp server bases on pool
        :param interface:
        :param name:
        :param pool:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/add','=interface='+interface,'=name='+name,'=address-pool='+pool])
        return ipv6

    def removeServer(self,name):
        """
        Method will remove server
        :param name:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/remove','=numbers='+name])
        return ipv6

    def enableServer(self,name):
        """
        Method will enable dhcp server
        :param name:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/enable','=numbers='+name])
        return ipv6

    def disableServer(self,name):
        """
        Method will disable server
        :param name:
        :return:
        """
        ipv6 = self.client.talk(["/ipv6/dhcp-server/disable",'=numbers='+name])
        return ipv6

    def commentServer(self,name,comment):
        """
        Method will comment rule
        :param name:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/comment','=numbers='+name,'=comment='+comment])
        return ipv6
    #Global
    def setName(self,name,newName):
        """
        Method will rename server
        :param name:
        :param newName:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/set','=numbers='+name,'=name='+newName])
        return ipv6

    def setInterface(self,name,iface):
        """
        Method will set dhcp server interface
        :param name:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/set','=numbers='+name,'=interface='+iface])
        return ipv6

    def setPool(self,name,pool):
        """
        Method will set pool
        :param name:
        :param pool: created pool
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/set','=numbers='+name,'=address-pool='+pool])
        return ipv6

    def setLeaseTime(self,name,lease):
        """
        Method will set lease time
        :param name:
        :param lease: 00:00:00 or 1d 00:00:00
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/set','=numbers='+name,'=lease-time='+lease])
        return ipv6

    #Binding
    def listDuid(self):
        """
        Method will list duid needed for binding
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/print','detail'])
        print("Name\tDuid")
        for i in ipv6:
            print(ipv6[i]['name']+"\t"+ipv6[i]['duid'])
        #print(ipv6)
        return ipv6


    def listBindings(self):
        """
        Method will list bindings
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/print'])
        if ipv6 == {}:
            print("No binding found")
        else:
            for i in ipv6:
                print(ipv6[i])
        return ipv6

    def addInterface(self,duid,iaid,server):
        """
        Method will add binding
        :param duid: from detail print of server
        :param iaid: identifier of client station 0..4294967295
        :param server: ipv6 addr
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/add','=server='+server,'=duid='+duid,'=iaid='+iaid])
        return ipv6

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/remove','=numbers='+number])
        return ipv6

    def enableInterface(self,number):
        """
        Method will enable iface
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-server/binding/enable', '=numbers=' + number] )
        return ipv6

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-server/binding/disable', '=numbers=' + number] )
        return ipv6

    def commentInterface(self,number,comment):
        """
        Method will comment iface
        :param number:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-server/binding/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv6

    def setAddress(self,number,address):
        """
        Method will set binding address
        :param number:
        :param address:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/set','=numbers='+number,'=address='+address])
        return ipv6

    def setDuid(self,number,duid):
        """
        Method will set duid on mikrotik (from dhcp server value)
        :param number:
        :param duid:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/set','=numbers='+number,'=duid='+duid])
        return ipv6

    def setIaid(self,number,ids):
        """
        Method will set id of client
        :param number:
        :param ids:integer [0..4294967295]; Default: )
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/set','=numbers='+number,'iaid='+ids])
        return ipv6

    def setServer(self,number,server="all"):
        """
        Method will set server
        :param number:
        :param server: interface all or specific one
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/set','=numbers='+number,'=server='+server])
        return ipv6

    def setLifeTime(self,number,life="3d 00:00:00"):
        """
        Method will set life time
        :param number:
        :param life:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/set','=numbers='+number,'=life-time='+life])
        return ipv6

    def setPrefixPool(self,number,pool="none"):
        """
        Method will set prefix pool
        :param number:
        :param pool:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-server/binding/set','=prefix-pool='+pool])
        return ipv6
