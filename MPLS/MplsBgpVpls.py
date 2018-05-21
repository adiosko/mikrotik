from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsBgpVpls:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list interfaces
        :return:
        """
        vpls = self.client.talk(['/interface/vpls/bgp-vpls/print'])
        if vpls == {}:
            print("No interface found")
        else:
            print("Name\tBridge")
            for i in vpls:
                print(vpls[i]['name']+"\t"+vpls[i]['bridge'])
        return vpls

    def addInterface(self):
        """
        Method will add interface
        :return:
        """
        vpls = self.client.talk(['/interface/vpls/bgp-vpls/add'])
        return vpls

    def removeInterface(self,name):
        """
        Method will remove interface
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/remove','=numbers='+name] )
        return vpls

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/enable', '=numbers=' + name] )
        return vpls

    def disableInterface(self,name):
        """
        Method will disable interface
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/disable', '=numbers=' + name] )
        return vpls

    def setName(self,name,newName):
        """
        Method will rename interface
        :param name:
        :param newName:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name,'=name='+newName] )
        return vpls

    def setRouteDistinquisher(self,name,dist="0:0"):
        """
        Method will set route distinquisher
        :param name:
        :param dist: 0:0 etc
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name,'=route-distinguisher='+dist] )
        return vpls

    def setImportRouteTarget(self,name,trg="0:0"):
        """
        Method will set route target
        :param name:
        :param trg:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=import-route-targets=' + trg] )
        return vpls

    def setExportRouteTargets(self,name,trg="0:0"):
        """
        Method will set exporting of route targets
        :param name:
        :param trg:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=export-route-targets=' + trg] )
        return vpls

    def setSideId(self,name,Id="1"):
        """
        Method will set side id
        :param name:
        :param Id:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=side-id=' + Id] )
        return vpls

    def setBridge(self,name,bridge="none"):
        """
        Method will set route bridge
        :param name:
        :param bridge: none or existing bridge
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=bridge=' + bridge] )
        return vpls

    def setBridgeCost(self,name,cost="50"):
        """
        Method will set bridge cost
        :param name:
        :param cost:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=bridge-cost=' + cost] )
        return vpls

    def setBridgeHorizon(self,name,horiz="0"):
        """
        Method will set horizon
        :param name:
        :param horiz:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=bridge-horizon=' + horiz] )
        return vpls

    def useControlWord(self,name):
        """
        Method will set control word
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=use-control-word=yes'] )
        return vpls

    def doNotUseControlWord(self,name):
        """
        Method will not use control word
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=use-control-word=no'] )
        return vpls

    def setPwMtu(self,name,mtu="1500"):
        """
        Method will set mtu
        :param name:
        :param mtu:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=pw-mtu=' + mtu] )
        return vpls

    def setPwType(self,name,typ="vpls"):
        """
        Method will set pw type
        :param name:
        :param typ: vpls, raw-ethernet, tagged-ethernet
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/bgp-vpls/set', '=numbers=' + name, '=pw-type=' + typ] )
        return vpls