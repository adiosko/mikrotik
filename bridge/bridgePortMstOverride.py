from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeMstOverride:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listMst(self):
        """
        Method will list mst
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/port/mst-override/print'])
        for i in vlan:
            print(vlan[i])
        return vlan

    def addMst(self,identifier,iface):
        """
        Metho will add mst override
        :param identifier:
        :param iface:
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/port/mst-override/add','=interface='+iface,'=identifier='+identifier])
        return vlan

    def removeMst(self,number):
        """

        :param number:
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/port/mst-override/remove','=numbers='+number])
        return vlan

    def enableMst(self, number):
        """

        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/port/mst-override/enable', '=numbers=' + number] )
        return vlan

    def disableMst(self, number):
        """

        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/port/mst-override/disable', '=numbers=' + number] )
        return vlan

    def commentMst(self, number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/port/mst-override/comment', '=numbers=' + number,'=comment='+comment] )
        return vlan

    def setInterface(self,number,iface):
        """
        Method will set iface
        :param number:
        :param iface:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/port/mst-override/set', '=numbers=' + number, '=interface=' + iface] )
        return vlan

    def setIdentifier(self,number,iden="1"):
        """

        :param number:
        :param iden:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/port/mst-override/set', '=numbers=' + number, '=identifier=' + iden] )
        return vlan

    def setPriority(self,number,prio="80"):
        """

        :param number:
        :param prio:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/port/mst-override/set', '=numbers=' + number, '=priority=' + prio] )
        return vlan

    def setInternalPathCOst(self,number,cost="10"):
        """

        :param number:
        :param cost:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/port/mst-override/set', '=numbers=' + number, '=internal-path-cost=' + cost] )
        return vlan

