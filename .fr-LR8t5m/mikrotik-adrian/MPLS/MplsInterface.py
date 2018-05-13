from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsInterface:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list interfaces
        :return:
        """
        mpls = self.client.talk(['/mpls/interface/print'])
        if mpls == {}:
            print("No interface found")
        else:
            print("Interface\tMTU")
            for i in mpls:
                print(mpls[i]['interface']+"\t"+mpls[i]['mpls-mtu'])
        return mpls

    def addInterface(self):
        """
        Method will add interface
        :return:
        """
        mpls = self.client.talk( ['/mpls/interface/add'] )
        return mpls

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/interface/remove','=numbers='+number] )
        return mpls

    def setInterface(self,number,interface="all"):
        """
        Method will set interface
        :param number:
        :param interface: all, or interface by choice
        :return:
        """
        mpls = self.client.talk( ['/mpls/interface/set','=numbers='+number,'=interface='+interface] )
        return mpls

    def setMtu(self,number,mtu="1508"):
        """
        Method will set mtu of interface
        :param number:
        :param mtu:
        :return:
        """
        mpls = self.client.talk( ['/mpls/interface/set', '=numbers=' + number, '=mpls-mtu=' + mtu] )
        return mpls
