from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipNgInterfaces:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list ripng ifaces
        :return:
        """
        rip = self.client.talk(['/routing/ripng/interface/print'])
        if rip == {}:
            print("No interface found")
        else:
            print("Interface\tpassive iface\tin and out prefix list")
            for i in rip:
                print(rip[i]['interface']+"\t"+rip[i]['passive']+"\t"+rip[i]['in-prefix-list']+rip[i]['out-prefix-list'])
        return rip

    def addInterfaces(self):
        """
        Method will add rip iface
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/add'] )
        return rip

    def removeInterface(self, number):
        """
        Method will remove rip interface
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/remove', '=numbers=' + number] )
        return rip

    def enableInterface(self, number):
        """
        Method will enable iface
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/enable', '=numbers=' + number] )
        return rip

    def disableInterface(self, number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/disable', '=numbers=' + number] )
        return rip

    def setInterface(self, number, interface="all"):
        """
        Method will set rip interface
        :param number:
        :param interface: all or local interface
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/set', '=numbers=' + number, '=interface=' + interface] )
        return rip

    def setPassiveInterface(self, number):
        """
        Method will set iface passive
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/set', '=numbers=' + number, '=passive=yes'] )
        return rip

    def setInPrefixList(self, number, prefix):
        """
        Method will set input prefix list
        :param number:
        :param prefix:
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/set', '=numbers=' + number, '=in-prefix-list=' + prefix] )
        return rip

    def setOutPrefixList(self, number, prefix):
        """
        Method will set prefix output list
        :param number:
        :param prefix:
        :return:
        """
        rip = self.client.talk( ['/routing/ripng/interface/set', '=numbers=' + number, '=out-prefix-list=' + prefix] )
        return rip