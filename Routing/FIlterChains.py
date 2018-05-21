from tikapy import TikapyClient
from tikapy import TikapySslClient

class FilterChains:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setFilterChain(self, number, chain):
        """
        Method will set chain
        :param number:
        :param chain:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=chain=' + chain] )
        return filt

    def setPrefix(self, number, prefix):
        """
        Method will set prefix number
        :param number:
        :param prefix: IPNet/prefix
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=prefix=' + prefix] )
        return filt

    def setPrefixLength(self,number,prefixLength="0-32"):
        """
        Method will set prefix length
        :param number:
        :param prefixLength: 0-32
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=prefix-length=' + prefixLength] )
        return filt

    def setMatchChain(self,number,chain):
        """
        Method will match chain
        :param number:
        :param chain: connected-in, dynamic-in
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=match-chain=' + chain] )
        return filt

    def setProtocolCOnnect(self,number):
        """
        Method will set protocol
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=protocol=connect'] )
        return filt

    def setProtocolStatic(self, number):
        """
        Method will set protocol
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=protocol=static'] )
        return filt

    def setProtocolRIP(self, number):
        """
        Method will set protocol
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=protocol=rip'] )
        return filt

    def setProtocolOSPF(self, number):
        """
        Method will set protocol
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=protocol=ospf'] )
        return filt

    def setProtocolBGP(self, number):
        """
        Method will set protocol
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=protocol=bgp'] )
        return filt

    def setDistance(self,number,distance="0-255"):
        """
        Method will set distance for filter
        :param number:
        :param distance: 0-255
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=distance=' + distance] )
        return filt

    def setScope(self, number, scope="0-255"):
        """
        Method will set distance for filter
        :param number:
        :param scope: 0-255
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=scope=' + scope] )
        return filt

    def setTargetScope(self, number, target="0-255"):
        """
        Method will set distance for filter
        :param number:
        :param distance: 0-255
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=target-scope=' + target] )
        return filt

    def setPrefSource(self,number,src="0.0.0.0/0"):
        """
        Method will set src
        :param number:
        :param src: 0.0.0.0/0
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=pref-src=' + src] )
        return filt

    def setRoutingMark(self,number,mark="main"):
        """
        Method will set mark
        :param number:
        :param mark: main routing table
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=routing-mark=' + mark] )
        return filt

    def setRouteCOmment(self,number,comment):
        """
        Method will set route comment
        :param number:
        :param comment:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-comment=' + comment] )
        return filt

    def setRouteTag(self,number,tag="0"):
        """
        Method will set route tag
        :param number:
        :param tag:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-tag=' + tag] )
        return filt

    def setRouteTArgets(self,number,target="0:0"):
        """
        Method will add route targets
        :param number:
        :param target: 0:0
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=route-targets=' + target] )
        return filt

    def setSiteOfOrigin(self,number,origin="0:0"):
        """
        Method will set origin
        :param number:
        :param origin: 0:0
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=' + origin] )
        return filt

    def setIpAddressFamily(self,number):
        """
        Method will set address family
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=ip'] )
        return filt

    def setIpv6AddressFamily(self, number):
        """
        Method will set address family
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=ipv6'] )
        return filt

    def setL2VpnAddressFamily(self, number):
        """
        Method will set address family
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=l2vpn'] )
        return filt

    def setVpnv4AddressFamily(self, number):
        """
        Method will set address family
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=vpnv4'] )
        return filt

    def setCiscoVpnAddressFamily(self, number):
        """
        Method will set address family
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=site-of-origin=l2vpn-cisco'] )
        return filt

    def setOspfType(self,number,type="intra-area"):
        """
        Method will set ospf type
        :param number:
        :param type: intra-area,external-type-1,external-type-2,inter-area,nssa-external-type-1,nssa-external-type-2
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=ospf-type='+type] )
        return filt