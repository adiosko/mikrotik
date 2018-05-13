from tikapy import TikapyClient
from tikapy import TikapySslClient

class Dhcpv6Client:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listCLients(self):
        """
        Method will list dhcpv6 clients
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-client/print'])
        if ipv6 == {}:
            print("No interface found")
        else:
            print("interface\tstatus\tRequest")
            for i in ipv6:
                print(ipv6[i]['interface']+"\t"+ipv6[i]['status']+"\t"+ipv6[i]['request'])
        return ipv6

    def addAddress(self,interface,rqst):
        """
        Method will add interface for ipv6 dhcp
        :param interface:
        :param rqst: addrees or prefix
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-client/add','=interface='+interface,'=request='+rqst])
        return ipv6

    def removeAddress(self,number):
        """
        method will remove client
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-client/remove','=numbers='+number])
        return ipv6

    def enableAddress(self,number):
        """
        Method will enable address
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/enable', '=numbers=' + number] )
        return ipv6

    def disableAddress(self,number):
        """
        Method will disable address
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/disable', '=numbers=' + number] )
        return ipv6

    def commentAddress(self,number,comment):
        """
        Method will comment adderess
        :param number:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv6

    def setInterface(self,number,iface):
        """
        Set client  iface
        :param number:
        :param iface:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number,'=interface='+iface] )
        return ipv6

    def setRequest(self,number,rqst="address"):
        """
        Method will set dhcp client requests
        :param number:
        :param rqst: address/prefix or both
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=request=' + rqst] )
        return ipv6

    def setPoolName(self,number,pool):
        """
        Method will set pool }use if u use if request is prefix
        :param number:
        :param pool:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=pool-name=' + pool] )
        return ipv6

    def setPoolLengthPrefix(self,number,prefix="64"):
        """
        Method will set prefix pool length
        :param number:
        :param prefix:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=pool-prefix-length=' + prefix] )
        return ipv6

    def setPrefixHint(self,number,hint="::/0"):
        """
        Method will set prefix hint
        :param number:
        :param hint: ipv6 subnet
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=prefix-hint=' + hint] )
        return ipv6

    def usePeerDns(self,number):
        """
        Method will use peer dns
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=use-peer-dns=yes'] )
        return ipv6

    def addDefaultRoute(self,number):
        """
        Method will use default route
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=use-default-route=yes'] )
        return ipv6

    #Advanced
    def setScript(self,number,script):
        """
        Method will setadvanced behaviour of dhcp client
        :param number:
        :param script:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/dhcp-client/set', '=numbers=' + number, '=script=' + script] )
        return ipv6

    def setRelease(self):
        """
        Method will release ipv6 addr for client
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-client/release'])
        return ipv6

    def setRenew(self):
        """
        Method will renew ipv6 address
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/dhcp-client/renew'])
        return ipv6
