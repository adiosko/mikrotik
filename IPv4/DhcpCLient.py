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
