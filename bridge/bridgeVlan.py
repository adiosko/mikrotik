from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeVlan:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listVlan(self):
        """

        :return:
        """
        vlan = self.client.talk(['/interface/bridge/vlan/print'])
        print("Bridge\tVLAN")
        for i in vlan:
            print(vlan[i]['bridge']+"\t"+vlan[i]['vlan-ids'])
        return vlan


    def addVlan(self,interface,vlanID):
        """
        Metho iwll set vlan
        :param interface:
        :param vlanID:
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/vlan/add','=bridge='+interface,'=vlan-ids='+vlanID])
        return vlan

    def removeVlan(self, number):
        """
    
        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/vlan/remove', '=numbers=' + number] )
        return vlan

    def enableVlan(self, number):
        """
    
        :param number:
        """
        vlan = self.client.talk( ['/interface/bridge/vlan/enable', '=numbers=' + number] )
        return vlan

    def disableVlan(self, number):
        """
    
        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/vlan/disable', '=numbers=' + number] )
        return vlan

    def commentVlan(self, number, comment):
        """
    
        :param number:
        :param comment:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/vlan/comment', '=numbers=' + number, '=comment=' + comment] )
        return vlan

    def setBridge(self,number,bridge):
        """
        Method will set bridge
        :param number:
        :param bridge:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/vlan/set', '=numbers=' + number, '=bridge=' + bridge] )
        return vlan

    def setVlanID(self, number, vlan):
        """
        Method will set bridge
        :param number:
        :param vlan:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/vlan/set', '=numbers=' + number, '=vlan-ids=' + vlan] )
        return vlan

    def setTag(self,number,tag):
        """

        :param number:
        :param tag:iface
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/vlan/set', '=numbers=' + number, '=tagged=' + tag] )
        return vlan

    def setUnTag(self, number, tag):
        """

        :param number:
        :param tag:iface
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/vlan/set', '=numbers=' + number, '=untagged=' + tag] )
        return vlan