from tikapy import TikapyClient
from tikapy import TikapySslClient

class DhcpClient:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listCLients(self):
        """
        Method will list dhcp clients
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-client/print'])
        if ipv4 == {}:
            print("No client found")
        else:
            print("Interface\tUse peer dns\tAdd default route\tIP address\tExpires\tStatus")
            for i in ipv4:
                print(ipv4[i]['interface']+"\t"+ipv4[i]['use-peer-dns']+"\t"+ipv4[i]['add-default-route']+"\t"+ipv4[i]['address']+"\t"+ipv4[i]['expires-after']+"\t"+ipv4[i]['status'])
        return ipv4

    def releaseAddress(self,number):
        """
        Method will release dh client
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-client/release','=numbers='+number])
        return ipv4

    def renewAddress(self,number):
        """
        Method w
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/renew', '=numbers=' + number] )
        return ipv4

    def removeAddress(self,number):
        """
        Method will remove client
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/remove','=numbers='+number] )
        return ipv4

    def enableAddress(self,number):
        """
        Methodwill enable address
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/enable', '=numbers=' + number] )
        return ipv4

    def disableAddress(self,number):
        """
        Method will disable dhcp client
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/disable', '=numbers=' + number] )
        return ipv4

    def commentAddress(self,number,comment):
        """
        Method will comment address
        :param number:
        :param comment:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv4

    """
        Pridat sety a advanced sety
     """

    def setInterface(self,number,iface):
        """
        Method will set interface
        :param number:
        :param iface:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/set', '=numbers=' + number, '=interface=' + iface] )
        return ipv4

    def usePeerDns(self,number):
        """
        Methodwill set use peer dns
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/set', '=numbers=' + number, '=use-peer-dns=yes'] )
        return ipv4

    def usePeerNtp(self,number):
        """
        Method will use peer ntp
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/set', '=numbers=' + number, '=use-peer-ntp=yes'] )
        return ipv4

    def setDhcpOptions(self,number,option):
        """
        Method will set dhcp options
        :param number:
        :param option: clientid,hostname
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/set', '=numbers=' + number, '=dhcp-options='+option] )
        return ipv4

    def addDefaultRoute(self,number):
        """
        Method will add defalt route
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/set', '=numbers=' + number, '=add-default-route=yes'] )
        return ipv4

    def setDefaultROuteDistance(self,number,distance="0"):
        """
        Method will st distance
        :param number:
        :param distance:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/set', '=numbers=' + number, '=default-route-distance=' + distance] )
        return ipv4


    #options
    def listDhcpOptions(self):
        """
        Method will list all dhcp options
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-client/option/print'])
        if ipv4 == {}:
            print("No option found")
        else:
            print("Name\tCode\tValue")
            for i in ipv4:
                print(ipv4[i]['name']+"\t"+ipv4[i]['code']+"\t"+ipv4[i]['value'])
        return ipv4

    def addOption(self,name,code):
        """
        Method will add options
        :param name:
        :param code: code of f.e 121
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-client/option/add','=name='+name,'=code='+code])
        return ipv4

    def removeOption(self,name):
        """
        Method will remove option
        :param name:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-client/option/remove','=numbers='+name])
        return ipv4

    def setName(self,name,newName):
        """
        Method will rename option
        :param name:
        :param newName:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-client/option/set','=numbers='+name,'=name='+newName])
        return ipv4

    def setCode(self,name,code):
        """
        Method will set dhcp code
        :param name:
        :param code:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/option/set', '=numbers=' + name, '=code=' + code] )
        return ipv4

    def setValue(self,name,value):
        """
        Method will set value
        :param name:
        :param value: hexa value
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-client/option/set', '=numbers=' + name, '=value=' + value] )
        return ipv4