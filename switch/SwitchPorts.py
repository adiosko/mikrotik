from tikapy import TikapyClient
from tikapy import TikapySslClient

class SwitchPorts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPorts(self):
        """
        Method will list ports
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/port/print'])
        print("Name\tinterface\tVlan mode\tDefault Vlan ID")
        for i in mswitch:
            print(mswitch[i]['name']+"\t"+mswitch[i]['switch']+"\t"+mswitch[i]['vlan-mode']+"\t"+mswitch[i]['default-vlan-id'])
        return mswitch


    def setVlanMode(self,name,mode="disabled"):
        """
        Method will set vlan mode for port
        :param name:
        :param mode: check, disabled,fallback,secure
        :return:
        """
        mswitch = self.client.talk(['/interface/ethernet/switch/port/set','=numbers='+name,'=vlan-mode='+mode])
        return mswitch

    def setVlanHeader(self,name,header="leave-as-is"):
        """
        Method will set vlan header
        :param name:
        :param header: add-if-missing,always-strip,leave-as-is
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/port/set', '=numbers=' + name, '=vlan-header=' + header] )
        return mswitch

    def setVlanId(self,name,ID="1"):
        """
        Method will set default vlan ID
        :param number:
        :param ID:
        :return:
        """
        mswitch = self.client.talk( ['/interface/ethernet/switch/port/set', '=numbers=' + name, '=default-vlan-id=' + ID] )
        return mswitch