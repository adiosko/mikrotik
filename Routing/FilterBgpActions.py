from tikapy import TikapyClient
from tikapy import TikapySslClient

class FilterBgpActions:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setBgpWeight(self,number,weight="0"):
        """
        Method will set bgp eight
        :param number:
        :param weight:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-weight=' + weight] )
        return bgp

    def setBgpLocalPref(self,number,lpref="0"):
        """
        Method will set lpref for bgp
        :param number:
        :param lpref:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-local-pref=' + lpref] )
        return bgp

    def setBgpPrepend(self,number,prepend="0"):
        """
        Method will set prepend for bgp
        :param number:
        :param prepend:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-prepend=' + prepend] )
        return bgp

    def setBgpMed(self,number,med="0"):
        """
        Method will set med value
        :param number:
        :param med:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-med=' + med] )
        return bgp

    def setBgpCommunities(self,number,community="0:0"):
        """
        Method will set bgp community
        :param number:
        :param community:no-export,no-advertise,local-as
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-communities=' + community] )
        return bgp

    def setAppenfBgpCommunities(self,number,community="0:0"):
        """
        Method wil lset bgp sommunity and will apend it
        :param number:
        :param community: no-export, no-advertise,local-as
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=append-bgp-communities=' + community] )
        return bgp
