from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeMSTI:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listMSTI(self):
        """
        Methdo will list all msti
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/msti/print'])
        print("Bridge\tIdentifier\tpriority(hex)")
        for i in vlan:
            print(vlan[i]['bridge']+"\t"+vlan[i]['identifier']+"\t"+vlan[i]['priority'])
        return vlan

    def addMsti(self,bridge,identifier,vlan):
        """
        
        :param bridge: 
        :param identifier: 
        :param vlan: 
        :return: 
        """
        vlan1 = self.client.talk(['/interface/bridge/msti/add','=bridge='+bridge,'=identifier='+identifier,'=vlan-mapping='+vlan])
        return vlan1

    def removeMst(self, number):
        """
    
        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/msti/remove', '=numbers=' + number] )
        return vlan

    def enableMst(self, number):
        """
    
        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/msti/enable', '=numbers=' + number] )
        return vlan

    def disableMst(self, number):
        """
    
        :param number:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/msti/disable', '=numbers=' + number] )
        return vlan

    def commentMst(self, number, comment):
        """
    
        :param number:
        :param comment:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/msti/comment', '=numbers=' + number, '=comment=' + comment] )
        return vlan

    def setBridge(self,number,bridge):
        """
        Method will set bridge
        :param number:
        :param bridge:
        :return:
        """
        vlan = self.client.talk(['/interface/bridge/msti/set', '=numbers=' + number, '=bridge=' + bridge] )
        return vlan

    def setIdentifier(self,number,iden="1"):
        """
        Method will set identifier
        :param number:
        :param iden:
        :return:
        """
        vlan = self.client.talk( ['/interface/bridge/msti/set', '=numbers=' + number, '=identifier=' + iden] )
        return vlan

    def setPriority(self, number, prio="80"):
        """

        :param number:
        :param prio:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/msti/set', '=numbers=' + number, '=priority=' + prio] )
        return vlan

    def setInternalPathCOst(self, number, cost="1"):
        """

        :param number:
        :param cost:
        :return:
        """
        vlan = self.client.talk(
            ['/interface/bridge/msti/set', '=numbers=' + number, '=vlan-mapping=' + cost] )
        return vlan
        