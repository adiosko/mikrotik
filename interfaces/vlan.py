from tikapy import TikapyClient
from tikapy import TikapySslClient


class vlan:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listVlan(self):
        """

        :return:
        """
        vlan = self.client.talk(['/interface/vlan/print'])
        return vlan

    def addVlan(self,name,vlanId,interface):
        """

        :param vlanId:
        :param interface:
        :return:
        """
        vlan = self.client.talk(['/interface/vlan/add','=name='+name,'=interface='+interface,'=vlan-id='+vlanId])
        return vlan

    def removeVlan(self,name):
        """

        :param name:
        :return:
        """
        vlan = self.client.talk(['/interface/vlan/remove','=numbers='+name])
        return vlan

    def enableVlan(self,name):
        """

        :param name:
        :return:
        """
        vlan = self.client.talk( ['/interface/vlan/enable', '=numbers=' + name] )
        return vlan

    def disableVlan(self,name):
        """

        :param name:
        :return:
        """
        vlan = self.client.talk( ['/interface/vlan/disable', '=numbers=' + name] )
        return vlan

    def commentVlan(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        vlan = self.client.talk( ['/interface/vlan/comment', '=numbers=' + name,'=comment='+comment] )
        return vlan