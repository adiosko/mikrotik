from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceVirtualWdsSLave:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setMode(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=mode=wds-slave'] )
        return wifi

    def setSsid(self, name, ssid):
        """

        :param name:
        :param ssid:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=ssid=' + ssid] )
        return wifi

    def setMasterInterface(self, name, iface):
        """

        :param name:
        :param iface:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=master-interface=' + iface] )
        return wifi

    def setArea(self,name,area):
        """

        :param name:
        :param area:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name,'=area='+area] )
        return wifi

    def setSecurityProfile(self, name, profile="default"):
        """

        :param name:
        :param profile:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=security-profile=' + profile] )
        return wifi

    def setWpsMode(self,name,mode="disabled"):
        """

        :param name:
        :param mode: disabled,push-button,virtual-push-button-only
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wps-mode=' + mode] )
        return wifi

    def setMaxStationCOunt(self,name,count="2007"):
        """

        :param name:
        :param count:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=max-station-count=' + count] )
        return wifi

    def setWmmSuport(self,name,support="disabled"):
        """

        :param name:
        :param support: disabled,enabled,required
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wmm-support=' + support] )
        return wifi

    def setVlanMode(self,name,tag="no-tag"):
        """

        :param name:
        :param tag:no-tag,use-service-tag,use-tag
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=vlan-mode=' + tag] )
        return wifi

    def setVlanId(self,name,vlan="1"):
        """

        :param name:
        :param vlan:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=vlan-id=' + vlan] )
        return wifi

    def setDefaultApTxRate(self,name,tx):
        """

        :param name:
        :param tx: bps
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-ap-tx-limit=' + tx] )
        return wifi

    def setDefaultClientTxRate(self,name,tx):
        """

        :param name:
        :param tx: bps
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-client-tx-limit=' + tx] )
        return wifi

    def setMulticastHelper(self,name,helper="default"):
        """

        :param name:
        :param helper:  default, disabled, full
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=multicast-helper=' + helper] )
        return wifi

    def enableMulticastBuffering(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=multicast-buffering=yes'] )
        return wifi

    def disableMulticastBuffering(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=multicast-buffering=no'] )
        return wifi

    def enableKeepAliveFramers(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=keepalive-frames=yes'] )
        return wifi

    def disableKeepAliveFramers(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=keepalive-frames=no'] )
        return wifi

    def enableDefaultAuthenticate(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-authentication=yes'] )
        return wifi

    def disableDefaultAuthenticate(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-authentication=no'] )
        return wifi

    def enableDefaultForward(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-forwarding=yes'] )
        return wifi

    def disableDefaultForward(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-forwarding=no'] )
        return wifi

    def hideSsid(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' +name,'hide-ssid=yes'] )
        return wifi

    def unhideSsid(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' +name,'hide-ssid=no'] )
        return wifi