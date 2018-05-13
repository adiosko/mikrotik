from tikapy import TikapyClient
from tikapy import TikapySslClient

class RoutingFilterBgp:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setBgpAsPath(self,number,AS="20"):
        """
        Method will set as path ibgp
        :param number:
        :param AS:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path=' + AS] )
        return filt

    def negateBgpAsPath(self,number,AS):
        """
        Method will negate as path
        :param number:
        :param AS:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path=!' + AS] )
        return filt

    def setBgpAsPathLength(self,number,leng="500"):
        """
        Method will set bgp as path
        :param number:
        :param leng:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path-length=' + leng] )
        return filt

    def negateBgpAsPathLength(self,number,leng="500"):
        """

        :param number:
        :param leng:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path-length=!' + leng] )
        return filt

    def setBgpWeight(self,number,weight="2000000"):
        """
        Method will set bgp weight
        :param number:
        :param weight:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-weight=' + weight] )
        return filt

    def negateBgpWeight(self,number,weight="!2000000"):
        """

        :param number:
        :param weight:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-weight=!' + weight] )
        return filt

    def setBgpLocalPref(self,number,lpref="2000000"):
        """
        Method will set local pref
        :param number:
        :param lpref:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-local-pref=' + lpref] )
        return filt

    def negateLocalPref(self,number,lpref="!2000000"):
        """
        Method will negate lpref
        :param number:
        :param lpref:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-local-pref=!' + lpref] )
        return filt

    def setBgpMed(self,number,med="3000000"):
        """
        Method will set med parameter
        :param number:
        :param med:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-med=' + med] )
        return filt

    def negateBgpMed(self,number,med):
        """
        Method will negate med
        :param number:
        :param med:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-med=!' + med] )
        return filt

    def setBgpAtomicAgregate(self,number,agreg="absent"):
        """
        Method will set agregate status
        :param number:
        :param agreg: absent, present
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-atomic-aggregate=' + agreg] )
        return filt

    def setBgpOrigin(self,number,origin="igp"):
        """
        Method will set bgp origin
        :param number:
        :param origin: igp,egp,incomplete
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-origin=' + origin] )
        return filt

    def setLocalyOriginatedBgp(self,number):
        """
        Method will set distribution of origin
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=locally-originated-bgp=yes'] )
        return filt

    def unsetLOcalyOriginBgp(self,number):
        """
        Method will unset origin bgp
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=locally-originated-bgp=no'] )
        return filt

    def setBgpCommunities(self,number,community="0:0"):
        """
        Method will set bgp community
        :param number:
        :param community: i.e 1:1
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-communities='+community] )
        return filt

    def uninvertMatch(self, number):
        """
        Method will reinvert match
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=invert-match=no'] )
        return filt


