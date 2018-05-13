from tikapy import TikapyClient
from tikapy import TikapySslClient

class FilterActions:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setAction(self,number,action="passthrough"):
        """
        Method will set passthrough action
        :param number:
        :param action: accept,discard,jump,log,passthrough,reject,return
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=action=' + action] )
        return bgp

    def setJumpTarget(self,number,target="connected-in"):
        """
        Method will set tar\ger for action jumpt
        :param target: connected-in, dynamic-in
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=action=jump','=jump-target=' + target] )
        return bgp

    def setDistance(self,number,distance="255"):
        """
        Method will set distance
        :param number:
        :param distance:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=distance=' + distance] )
        return bgp

    def setScope(self, number, scope="255"):
        """
        Method will set distance
        :param number:
        :param distance:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=scope=' + scope] )
        return bgp

    def setTargetScope(self,number,scope="200"):
        """
        Method will set target scope
        :param number:
        :param scope:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=target-scope=' + scope] )
        return bgp

    def setPrefSource(self,number,source="0.0.0.0"):
        """
        Method wil lset prefer source address
        :param number:
        :param source:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-pref-src=' + source] )
        return bgp

    def setInNexthop(self,number,nhop):
        """
        Method will set next hop IP
        :param number:
        :param nhop:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop=' + nhop] )
        return bgp

    def setInNexthopDirection(self, number, nhop="ether1"):
        """
        Method will set next hop IP
        :param number:
        :param nhop:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop-direct=' + nhop] )
        return bgp

    def setOutNexthop(self,number,nhop="0.0.0.0"):
        """
        Method will set out nhop address
        :param number:
        :param nhop:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-out-nexthop=' + nhop] )
        return bgp

    def setRoutingMark(self,number,mark="main"):
        """
        Method will set routinh table
        :param number:
        :param mark:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-routing-mark=' + mark] )
        return bgp

    def setROuteComment(self,number,comment):
        """
        Method will set route comment
        :param number:
        :param comment:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-route-comment=' + comment] )
        return bgp

    def setCheckGateway(self,number,gw="ping"):
        """
        Method will set gw
        :param number:
        :param gw: ping, arp,none
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-check-gateway=' + gw] )
        return bgp

    def setDisabled(self,number,disable="no"):
        """
        Method will set filter disabled
        :param number:
        :param disable: no/yes
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-disabled=' + disable] )
        return bgp

    def setType(self,number,type="unicast"):
        """
        Method will set type
        :param number:
        :param type: unicast, blackhole,prohibit,unreachable
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-type=' + type] )
        return bgp

    def setRouteTag(self,number,tag="0"):
        """
        Method will set route tag
        :param number:
        :param tag:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-route-tag=' + tag] )
        return bgp
    def setUseTeNexthop(self,number,use="no"):
        """
        Method will set to use TE
        :param number:
        :param use:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-use-te-nexthop=' + use] )
        return bgp

    def setRouteTargets(self,number,target="0:0"):
        """
        Method will set target
        :param number:
        :param target:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-route-targets=' + target] )
        return bgp

    def setAppendRouteTargets(self,number,target="0:0"):
        """
        Method will set target
        :param number:
        :param target:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=append-route-targets=' + target] )
        return bgp

    def setSiteOrigin(self,number,origin="0:0"):
        """
        Method will set origin
        :param number:
        :param origin:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-site-of-origin=' + origin] )
        return bgp

    def setInIpv6Nexthop(self,number,IPv6):
        """
        Method will set in Ipv6 nexthop
        :param number:
        :param IPv6:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop-ipv6=' + IPv6] )
        return bgp

    def setInIpv6NexthopLinklocal(self,number,address,interface="ether1"):
        """
        Method will set interface and link local ipv6 address
        :param number:
        :param address:
        :param interface:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop-linklocal=' + address+"%"
                                 +interface] )
        return bgp

    def setOutIpv6Nexthop(self,number,IPv6):
        """
        Method will set Ipv6 out iface
        :param number:
        :param IPv6:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-out-nexthop-ipv6=' + IPv6] )
        return bgp

    def setOutNexthopIpv6LinkLocal(self,number,addres="::",interface="ether1"):
        """
        Method will set out ipv6 link local address
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-out-nexthop-linklocal=' + addres+"%"
                                 +interface] )
        return bgp