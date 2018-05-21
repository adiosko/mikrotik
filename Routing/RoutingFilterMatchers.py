from tikapy import TikapyClient
from tikapy import TikapySslClient

class RoutingFiltersMatchers:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)


    def setChain(self,number,chain):
        """
        Method will set chain
        :param number: order no
        :param chain: connected-in,dynamic-in,mme-in,ospf-in,ospf-out
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set','=numbers='+number,'=chain=' + chain] )
        return filt

    def setPrefix(self,number,prefix):
        """
        Method will set prefix
        :param number:
        :param prefix:  subnet/n
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=prefix=' + prefix] )
        return filt

    def negatePrefix(self,number,prefix):
        """
        Method will negate prefix
        :param number:
        :param prefix: subnet/n
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=prefix=!' + prefix] )
        return filt

    def setPrefixLength(self,number,leng):
        """
        Method will set prefix length
        :param number:
        :param len:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=prefix-length=' +leng] )
        return filt

    def negatePrefixLength(self,number,leng):
        """

        :param number:
        :param leng: 0-32
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=prefix-length=!' + leng] )
        return filt

    def setMatchChain(self,number,chain):
        """
        method will set chain to match
        :param number:
        :param chain: connected-in,dynamic-in,mme-in,ospf-in,ospf-out
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=match-chain=' + chain] )
        return filt

    def negateMatchChain(self,number,chain):
        """
        Method will negate chain input
        :param number:
        :param chain:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=match-chain=!' + chain] )
        return filt

    def enableProtocol(self,number,protocol):
        """
        Method will enable protocol
        :param number:
        :param protocol: bgp, connect, ospf, rip, static
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=protocol=' + protocol] )
        return filt

    def setDistance(self,number,distance="192"):
        """
        Method will set distance
        :param number:
        :param distance:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=distance=' + distance] )
        return filt

    def negateDistance(self,numbers,distance="192"):
        """
        Method will negate distance
        :param numbers:
        :param distance:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + numbers, '=distance=!' + distance] )
        return filt

    def setScope(self,number,scope="200"):
        """
        Method will set scope
        :param number:
        :param scope: max 255
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=scope=' + scope] )
        return filt

    def negateScope(self,number,scope):
        """

        :param number:
        :param scope:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=scope=!' + scope] )
        return filt

    def setTargetScope(self,number,tscope="150"):
        """

        :param number:
        :param tscope: max 255
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=target-scope=' + tscope] )
        return filt

    def negateTargetScope(self,number,tscope):
        """

        :param number:
        :param tscope:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=target-scope=!' + tscope] )
        return filt

    def setPrefSource(self,number,source="1.1.1.0/24"):
        """
        Method will set pref source
        :param number:
        :param source:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=pref-src=' + source] )
        return filt

    def negatePrefSource(self,number,source):
        """

        :param number:
        :param source:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=pref-src=!' + source] )
        return filt

    def setRoutingMark(self,number,mark="main"):
        """
        Method will set routing table
        :param number:
        :param mark:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=routing-mark=' + mark] )
        return filt

    def negateRoutingMark(self,number,mark):
        """

        :param number:
        :param mark:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=routing-mark=!' + mark] )
        return filt

    def setRouteCOmment(self,number,comment):
        """
        Method will set comment for routing
        :param number:
        :param comment:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-comment=' + comment] )
        return filt

    def negateRouteCOmment(self,number,comment):
        """
        Method will negate comment for routing
        :param number:
        :param comment:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-comment=!' + comment] )
        return filt

    def setRouteTag(self,number,tag="5"):
        """
        Method will set route tag
        :param number:
        :param tag:  N
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-tag=' + tag] )
        return filt

    def negateRouteTag(self,number,tag):
        """
        Method will negate route tag
        :param number:
        :param tag:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-tag=!' + tag] )
        return filt

    def setRouteTarget(self,number,taget="10:0"):
        """
        Method will set route target
        :param number:
        :param taget:0:n or n:0
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-targets=' + taget] )
        return filt

    def negateRouteTarget(self,number,target):
        """
        Method will negate target
        :param number:
        :param target:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-targets=!' + target] )
        return filt

    def setSiteOfOrigin(self,number,site="10:0"):
        """
        Method will set site of orgin
        :param number:
        :param site:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=' + site] )
        return filt

    def negateSiteOrigin(self,number,site="!10:0"):
        """

        :param number:
        :param site:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=!' + site] )
        return filt

    def setAddressFamily(self,number,family):
        """
        Method will set address family
        :param number:
        :param family: ip,ipv6,l2vpn,l2vpn-cisco,vpnv4
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=address-family=' + family] )
        return filt

    def setOspfType(self,number,type="external-type-1"):
        """

        :param number:
        :param type: external-type-1,external-type-2,inter-area,intra-area,nssa-external-type-1,nssa-external-type-2
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=ospf-type=' + type] )
        return filt

    def invertMatch(self,number):
        """
        Method will invert match
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=invert-match=yes'] )
        return filt

    def uninvertMatch(self,number):
        """
        Method will reinvert match
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=invert-match=no'] )
        return filt






