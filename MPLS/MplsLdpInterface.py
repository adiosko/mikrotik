from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsLdpInterface:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list interfaces for ldp
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/interface/print'])
        if mpls == {}:
            print("No ldp interface found")
        else:
            print("Interface\tHello interval\thold time\ttransport address\taccept dynamic neighbors")
            for i in mpls:
                print(mpls[i]['interface']+"\t"+mpls[i]['hello-interval']+"\t"+mpls[i]['hold-time']+"\t"+mpls[i]['transport-address']+"\t"+mpls[i]['accept-dynamic-neighbors'])
        return mpls

    def addInterface(self,interface="ether1"):
        """
        Method will add interface
        :param interface: interface on ros
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/add','=interface='+interface])
        return mpls

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/remove', '=numbers=' + number] )
        return mpls

    def enableInterface(self,number):
        """
        Method will enable ldp interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/enable', '=numbers=' + number] )
        return mpls

    def disableInterface(self,number):
        """
        Method will disable ldp interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/disable', '=numbers=' + number] )
        return mpls

    def commentInterface(self,number,comment):
        """
        Method will comment interface
        :param number:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/comment', '=numbers=' + number,'=comment='+comment] )
        return mpls

    def setInterface(self,number,interface):
        """
        Method will set interface of ldp interface
        :param number:
        :param interface:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/set', '=numbers=' + number, '=interface=' + interface] )
        return mpls

    def setHelloInterval(self,number,interval="00:00:05"):
        """
        Method will set hello interval
        :param number:
        :param interval:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/set', '=numbers=' + number, '=hello-interval=' + interval] )
        return mpls

    def setHoldTime(self,number,hodltime="00:00:15"):
        """
        Method will set hold time interval
        :param number:
        :param hodltime:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/set', '=numbers=' + number, '=hold-time=' + hodltime] )
        return mpls

    def setTransportAddress(self,number,address="0.0.0.0"):
        """
        Method will set transport address (optional)
        :param number:
        :param address:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/set', '=numbers=' + number, '=transport-address=' + address] )
        return mpls

    def acceptDynamicNeighbors(self,number):
        """
        Method will accept dynamic neighbors
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/interface/set', '=numbers=' + number, '=accept-dynamic-neighbors=yes'] )
        return mpls