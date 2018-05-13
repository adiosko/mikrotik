from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsVpls:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listIntrefaces(self):
        """
        Method will lis tvpls interfaces
        :return:
        """
        vpls = self.client.talk(['/interface/vpls/print'])
        if vpls == {}:
            print("No interface found")
        else:
            print("Name\tMtu\tl2mtu")
            for i in vpls:
                print(vpls[i]['name']+"\t"+vpls[i]['mtu']+"\t"+vpls[i]['l2mtu'])
        return vpls

    def addInterface(self,remotePeer,vID):
        """
        Method will add interface
        :param remotePeer: IP
        :param vID: 1:0 etc.
        :return:
        """
        vpls = self.client.talk(['/interface/vpls/add','=remote-peer='+remotePeer,'=vpls-id='+vID,'=disabled=no'])
        return vpls

    def removeInterface(self,name):
        """
        Method will remove interface
        :param name:
        :return:
        """
        vpls = self.client.talk(['/interface/vpls/remove','=numbers='+name])
        return vpls

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/enable', '=numbers=' + name] )
        return vpls

    def disableInterface(self,name):
        """
        Method will disable interface
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/disable', '=numbers=' + name] )
        return vpls

    def commentInterface(self,name,comment):
        """
        Method will comment interface
        :param name:
        :param comment:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/comment', '=numbers=' + name,'=comment='+comment] )
        return vpls

    def setName(self,name,newName):
        """
        Method will rename interface
        :param name:
        :param newName:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=name=' + newName] )
        return vpls

    def setMtu(self,name,mtu="1500"):
        """
        Method will set mtu
        :param name:
        :param mtu:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=mtu=' + mtu] )
        return vpls

    def setMacAddress(self,name,mac):
        """
        Method will set amc address
        :param name:
        :param mac:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=mac-address=' + mac] )
        return vpls

    def setArp(self,name,arp="enabled"):
        """
        Method will se t arp mode
        :param name:
        :param arp: disabled,enabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=arp=' + arp] )
        return vpls

    def setRemotePeer(self,name,peer):
        """
        Method will set remote peer
        :param name:
        :param peer:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=remote-peer=' + peer] )
        return vpls

    def setVplsId(self,name,Id):
        """
        Method will set vpls id
        :param name:
        :param id: 2-2
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=vpls-id=' + Id] )
        return vpls

    def setArpTimeout(self,name,tout="00:00:00"):
        """
        Method will set timeout for arp
        :param name:
        :param tout:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=arp-timeout=' + tout] )
        return vpls

    def setCiscoStyle(self,name):
        """
        Method will set cisco style
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=cisco-style=yes'] )
        return vpls

    def unsetCiscoStyle(self,name):
        """
        Method will unset cisco style
        :param name:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=cisco-style=no'] )
        return vpls

    def setCiscoStyleId(self,name,Id="0"):
        """
        Method will set cisco style id
        :param name:
        :param id:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=cisco-style-id=' + Id] )
        return vpls

    def setAdvertizedMtu(self,name,mtu="1500"):
        """
        Method will set advertized mtu
        :param name:
        :param mtu:
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=advertized-l2mtu=' + mtu] )
        return vpls

    def setPwType(self,name,typ="raw-ethernet"):
        """
        Method will set pw type
        :param name:
        :param typ: raw-ethernet,tagged-ethernet
        :return:
        """
        vpls = self.client.talk( ['/interface/vpls/set', '=numbers=' + name, '=pw-type=' + typ] )
        return vpls