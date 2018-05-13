from tikapy import TikapyClient
from tikapy import TikapySslClient

class SwitchHost:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listHosts(self):
        """
        Method will list hosts
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/host/print'])
        for i in mswitch:
            print(mswitch[i])
        return mswitch

    def addHost(self,Switch,MAC,Port):
        """
        Method will add host
        :param Switch:
        :param MAC:
        :param Port:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/host/add','=switch='+Switch,'=mac-address='+MAC,'=ports='+Port])
        return mswitch

    def removeHost(self,number):
        """
        Method will remove host
        :param number:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/host/remove','=numbers='+number])
        return mswitch

    def setSwitch(self,number,switch):
        """
        Method will set switch
        :param number:
        :param switch:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/host/set','=numbers='+number,'=switch='+switch])
        return mswitch

    def setMAC(self,number,MAC):
        """
        Methodwill set mac address
        :param number:
        :param MAC:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=mac-address=' + MAC] )
        return mswitch

    def setPorts(self,number,port):
        """
        Method will set ports
        :param port:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=ports=' + port] )
        return mswitch

    def copyToCpu(self,number):
        """

        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=copy-to-cpu=yes'] )
        return mswitch

    def redirectToCpu(self,number):
        """

        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=redirect-to-cpu=yes'] )
        return mswitch

    def drop(self,number):
        """

        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=drop=yes'] )
        return mswitch

    def mirror(self,number):
        """
        Method will mirror port
        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=mirror=yes'] )
        return mswitch

    def setVlanId(self,number,vlan="1"):
        """
        Method will set vlan id
        :param number:
        :param vlan:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/host/set', '=numbers=' + number, '=vlan-id='+vlan] )
        return mswitch

    def shareVlanLearned(self,number):
        """
        Method will share learned vlans
        :param number:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/host/set','=numbers='+number,'=share-vlan-learned=yes'] )
        return mswitch

