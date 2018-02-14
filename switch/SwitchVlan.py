from tikapy import TikapyClient
from tikapy import TikapySslClient

class SwitchVlan:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listVlans(self):
        """
        Method will list vlans
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/vlan/print'])
        print("Switch\tVlanID\tPorts")
        for i in mswitch:
            print(mswitch[i]['switch']+"\t"+mswitch[i]['vlan-id']+"\t"+mswitch[i]['ports'])
        return mswitch

    def addVlan(self,switch,vlan,port):
        """
        Method will set vlan
        :param switch:
        :param vlan:
        :param port:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/vlan/add','=switch='+switch,'=vlan-id='+vlan,'=ports='+port])
        return mswitch

    def removeVlan(self,number):
        """
        Method will remove vlan
        :param number:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/vlan/remove','=numbers='+number])
        return mswitch

    def enableVlan(self, number):
        """
        Method will enable vlan
        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/vlan/enable', '=numbers=' + number] )
        return mswitch

    def disableVlan(self, number):
        """
        Method will remove vlan
        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/vlan/disable', '=numbers=' + number] )
        return mswitch

    def setSwitch(self,number,switch):
        """
        Method will set switch
        :param number:
        :param switch:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/vlan/set','=numbers='+number,'=switch='+switch])
        return mswitch

    def setVlanId(self,number,ID):
        """
        Method will set vlan ID
        :param number:
        :param ID:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/vlan/set', '=numbers=' + number, '=vlan-id=' + ID] )
        return mswitch

    def setPorts(self,number,port):
        """
        Method will set ports
        :param number:
        :param port:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/vlan/set', '=numbers=' + number, '=ports=' + port] )
        return mswitch

    def independentLearning(self,number):
        """
        Method will set independent learning
        :param number:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/vlan/set', '=numbers=' + number, '=independent-learning=yes'] )
        return mswitch