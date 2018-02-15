from tikapy import TikapyClient
from tikapy import TikapySslClient

class BridgeGeneral:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listBridge(self):
        """
        Method will list bridge
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/print'])
        print("Name\tL2 MTU\tMAC\tProtocol")
        for i in bridge:
            print(bridge[i]['name']+"\t"+bridge[i]['l2mtu']+"\t"+bridge[i]['mac-address']+"\t"+bridge[i]['protcol-mode'])
        return bridge

    def addBridge(self,name):
        """
        Method wil ladd bridge
        :param name:
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/add','=name='+name])
        return bridge

    def removeBridge(self,name):
        """
        Method will remove bridge
        :param name:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/remove', '=numbers=' + name] )
        return bridge

    def enableBridge(self,name):
        """
        Method will enable bridge
        :param name:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/enable', '=numbers=' + name] )
        return bridge

    def disableBridge(self,name):
        """
        Method will disable bridge
        :param name:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/disable', '=numbers=' + name] )
        return bridge

    def commentBridge(self,name,comment):
        """
        Method will comment bridge
        :param name:
        :param comment:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/comment', '=numbers=' + name,'=comment='+comment] )
        return bridge

    #General
    def setName(self,name,newName):
        """
        Method will set new name
        :param name:
        :param newName:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=name=' + newName] )
        return bridge

    def setMtu(self,name,mtu="64"):
        """
        Method will set mtu
        :param name:
        :param mtu: 64k
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=mtu=' + mtu] )
        return bridge

    def setArp(self,name,arp="enabled"):
        """
        Method will enable arp
        :param name:
        :param arp: enabled,disabled,local-proxy-arp,proxy-arp,local-only
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=arp=' + arp] )
        return bridge

    def setArpTimeout(self,name,time="00:00:00"):
        """
        Method will set arp timeout
        :param name:
        :param time:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=arp-timeout=' + time] )
        return bridge

    def setAdminMacAddress(self,name,mac):
        """
        Method will set admin mac
        :param name:
        :param mac:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=admin-mac=' + mac] )
        return bridge

    def setIgmpSnooping(self,name):
        """
        Method will enable igmp snooping
        :param name:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=igmp-snooping=yes'] )
        return bridge

    def fastForward(self,name):
        """
        Method will enable fast forward
        :param name:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=fast-forward=yes'] )
        return bridge

    #STP
    def setProtocolMode(self,name,protocol="rstp"):
        """
        Method will set rstp
        :param name:
        :param protocol: none,stp,rstp,mstp
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=protocol-mode=' + protocol] )
        return bridge

    def setPriority(self,name,priority="8000"):
        """
        Method will set priority
        :param name:
        :param priority:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=priority=' + priority] )
        return bridge

    def setRegionName(self,name,region):
        """
        Method will set region anme,mstp must be enabled
        :param name:
        :param region:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=protocol-type=mstp','=region-name=' + region] )
        return bridge

    def setRegionRevisionNumber(self,name,number="0"):
        """
        Method will set mstp region revision number
        :param name:
        :param number:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name,'=protocol-type=mstp', '=region-revision=' + number] )
        return bridge

    def setMaxMessageAge(self,name,message="00:00:20"):
        """
        Method wil lset max message exchange
        :param name:
        :param message:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=max-message-age=' + message] )
        return bridge

    def forwardDelay(self,name,fw="00:00:15"):
        """
        Method will set forward delay
        :param name:
        :param fw:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=forward-delay=' + fw] )
        return bridge

    def setTransmitHoldCount(self,name,count="6"):
        """
        method will set tr hold count
        :param name:
        :param count:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=transmit-hold-count=' + count] )
        return bridge

    def setAgeingTime(self,name,age="00:05:00"):
        """

        :param name:
        :param age:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=ageing-time=' + age] )
        return bridge

    def setMaxHops(self,name,hops="20"):
        """
        method will set Max hops
        :param name:
        :param hops:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=max-hops=' + hops] )
        return bridge

    #VLAN
    def setVlanFiltering(self,name):
        """
        Method will enbale vlan filteirng
        :param name:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=vlan-filtering=yes'] )
        return bridge

    def setPVid(self,name,vlan="1"):
        """
        method will set vlan id
        :param name:
        :param vlan:
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/set', '=numbers=' + name, '=pvid=' + vlan] )
        return bridge
