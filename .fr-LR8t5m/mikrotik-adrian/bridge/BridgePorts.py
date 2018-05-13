from tikapy import TikapyClient
from tikapy import TikapySslClient

class BridgePorts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    #opravit!!!!!!!
    def listPort(self):
        """
        Method will list ports
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/port/print'])
        return bridge

    def addPort(self,interface,bridge):
        """
        Method will add port
        :param interface:
        :param bridge:
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/port/add','=interface='+interface,'=bridge='+bridge])
        return bridge

    def removePort(self,number):
        """
        Metjhod will remove port
        :param number:
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/port/remove','=numbers='+number])
        return bridge

    def enablePort(self,number):
        """
        Method will enable port
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/enable', '=numbers=' + number] )
        return bridge

    def disablePort(self,number):
        """
        Method will disable port
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/disable', '=numbers=' + number] )
        return bridge

    def commentPort(self,number,comment):
        """
        bridge = self.client.talk(['/interface/bridge/port/remove','=numbers='+number])
        return bridge
        :param number:
        :param comment:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/comment', '=numbers=' + number,'=comment='+comment] )
        return bridge

    #General
    def setInterface(self,number,iface):
        """
        Method will set iface
        :param number:
        :param iface:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=interface=' + iface] )
        return bridge

    def setBridge(self,number,bridge):
        """
        Method will set bridge
        :param number:
        :param bridge:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=bridge=' + bridge] )
        return bridge

    def setHorizon(self,number,horizon="0"):
        """
        Method will set horizon
        :param number:
        :param horizon:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=horizon=' + horizon] )
        return bridge

    def setExternalFdb(self,number,fdb="auto"):
        """

        :param number:
        :param fdb: auto,no,yes
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=external-fdb=' + fdb] )
        return bridge

    def hardwareOffload(self,number):
        """

        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=hw=yes'] )
        return bridge

    #STP
    def setPriority(self,number,priority="80"):
        """
        Method will set priority
        :param number:
        :param priority:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=priority=' + priority] )
        return bridge

    def setPAthCost(self,number,cost="10"):
        """
        Method will set path cost
        :param number:
        :param cost:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=path-cost=' + cost] )
        return bridge

    def setInternalPathCOst(self,number,path="10"):
        """
        Method will set internal path cost
        :param number:
        :param path:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=internal-path-cost=' + path] )
        return bridge

    def setEdge(self,number,edge="auto"):
        """
        Methdo wil let edge emthod
        :param number:
        :param edge: auto,no,no-discover,yes,yes-discover
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=edge=' + edge] )
        return bridge

    def setP2P(self,number,p2p="auto"):
        """
        Method ill swt p2p method
        :param number:
        :param p2p: auto,no,yes
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=point-to-point=' + p2p] )
        return bridge

    def autoIsolate(self,number):
        """
        Method will auto isolate
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=auto-isolate=yes'] )
        return bridge

    def restrictedRole(self,number):
        """
        Method will enable restricted role
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=restricted-role=yes'] )
        return bridge

    def restrictedTcn(self,number):
        """
        Method will set restricted tcn
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=restricted-tcn=yes'] )
        return bridge

    #vlan
    def setVlanId(self,number,vlan="1"):
        """
        method will set vlan id
        :param number:
        :param vlan:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=pvid=' + vlan] )
        return bridge

    def setFrameType(self,number,frame="admit-all"):
        """
        method will set  frame type
        :param number:
        :param frame: admit-all,admit-only-untagged-and-priority-tagged,admin-only-vlan-tagged
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=frame-types=' + frame] )
        return bridge

    def ingressFiltering(self,number):
        """
        Method will ingress filtering
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/port/set', '=numbers=' + number, '=ingress-filtering=yes'] )
        return bridge