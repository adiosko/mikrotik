from tikapy import TikapyClient
from tikapy import TikapySslClient

class RoutingFilterBgpActions:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setBgpWeight(self,number,weight="50"):
        """
        Method will set bgp weight
        :param number:
        :param weight:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-weight='+weight] )
        return filt

    def setBgpLocPref(self,number,lpref="100"):
        """
        Method will set lpref
        :param number:
        :param lpref:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-local-pref=' + lpref] )
        return filt

    def setBgpPrepend(self,number,prepend="10"):
        """
        Method will set prepend
        :param number:
        :param prepend:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-prepend=' + prepend] )
        return filt

    def setBgpPrependPath(self,number,path="0"):
        """
        Met
        :param number:
        :param path:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-prepend-path=' + path] )
        return filt

    def setBgpMed(self,number,med="1"):
        """
        Method will set med value
        :param number:
        :param med:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-med=' + med] )
        return filt

    def setBgpCommunities(self,number,comm="1:1"):
        """
        Method will set bgp communities
        :param number:
        :param comm:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-bgp-communities=' + comm] )
        return filt

    def appendBgpCommunities(self,number,comm="0:0"):
        """
        Method will append communities for bgp
        :param number:
        :param comm:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=append-bgp-communities=' + comm] )
        return filt