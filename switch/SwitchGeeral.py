from tikapy import TikapyClient
from tikapy import TikapySslClient

class SwitchGeneral:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSwitch(self):
        """
        Method will list switch
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/print'])
        print("Name\tType")
        for i in mswitch:
            print(mswitch[i]['name']+"\t"+mswitch[i]['type'])
        return mswitch

    def setName(self,name,newName):
        """
        Method will rename switch
        :param name:
        :param newName:
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/set','=numbers='+name,'=name='+newName])
        return mswitch

    def setMirrorSource(self,name,iface="ether1"):
        """
        Method will set mirror source
        :param name:
        :param iface:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/set', '=numbers=' + name, '=mirror-source=' + iface] )
        return mswitch

    def setMirrorTarget(self,name,tgt="ether1"):
        """
        Method will set mirror target
        :param name:
        :param tgt:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/set', '=numbers=' + name, '=mirror-target=' + tgt])
        return mswitch

    def switchAllPorts(self,name):
        """
        Method will switch all ports
        :param name:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/set', '=numbers=' + name, '=switch-all-ports=yes'] )
        return mswitch


