from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallL7Protocols:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listProtocols(self):
        """
        Method will list protocols
        :return:
        """
        ip = self.client.talk(['/ip/firewall/layer7-protocol/print'])
        if ip == {}:
            print("No L7 found")
        else:
            print("Name\tRegexp")
            for i in ip:
                print(ip[i]['name']+"\t"+ip[i]['regexp'])
        return ip

    def addProtocol(self,name,regexp):
        """
        Method will add l7 protocol
        :param name:
        :param regexp: regular expresion script
        :return:
        """
        ip = self.client.talk(['/ip/firewall/layer7-protocol/add','=name='+name,'=regexp='+regexp])
        return ip

    def removeProtocol(self,name):
        """
        Method will remove protocol
        :param name:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/layer7-protocol/remove','=numbers='+name])
        return ip

    def commentProtocol(self,name,comment):
        """
        Method will comment protocol
        :param name:
        :param comment:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/layer7-protocol/comment','=numbers='+name,'=comment='+comment])
        return ip

    def setName(self,name,newNAme):
        """
        Method will renmae protocol
        :param name:
        :param newNAme:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/layer7-protocol/set','=numbers='+name,'=name='+newNAme])
        return ip

    def setRegexp(self,name,regexp):
        """
        Method will set regular expresion
        :param name:
        :param regexp:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/layer7-protocol/set','=numbers='+name,'=regexp='+regexp])
        return ip