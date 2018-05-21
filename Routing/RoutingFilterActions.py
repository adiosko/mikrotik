from tikapy import TikapyClient
from tikapy import TikapySslClient
#import main

class RoutingFilterActions:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setAction(self,number,action="jump"):
        """
        Method will set action
        :param number:
        :param action: accept, discard,jump,log,passthrough,reject,return
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=action=' + action] )
        return filt

    def setJumpTarget(self,number,tgt="dynamic-in"):
        """
        Method will set target
        :param number:
        :param tgt: connected-in,dynamic-in,mme-in,ospf-in,ospf-out
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=jump-target=' + tgt] )
        return filt

    def setDistance(self,number,distance):
        """
        Method will set distance
        :param number:
        :param distance:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=distance=' + distance] )
        return filt

    def setScope(self,number,scope):
        """
        Method will set scope to 255
        :param number:
        :param scope:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=scope=' + scope] )
        return filt

    def setTargetScope(self,number,scope="200"):
        """
        Method will set target scope to 255
        :param number:
        :param scope:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=target-scope=' + scope] )
        return filt

    def setPrefSource(self,number,source="172.16.53.2"):
        """
        Method will set pref source
        :param number:
        :param source:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-pref-src=' + source] )
        return filt

    def setNextHop(self,number,nhop):
        """
        Method will set next hop
        :param number:
        :param nhop:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop=' + nhop] )
        return filt

    def setInNxtHopDirect(self,number,iface="ether1"):
        """
        Method will set next hop direction
        :param number:
        :param iface:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop-direct='+iface] )
        return filt

    def setOutNextHop(self,number,nhop="172.16.53.2"):
        """
        Method will set nhop iface
        :param number:
        :param nhop:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-out-nexthop=' + nhop] )
        return filt

    def setRoutingMark(self,number,mark="main"):
        """
        Method will set  routing mark
        :param number:
        :param mark: main
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-routing-mark=' + mark] )
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

    def setCheckGw(self,number,gw="arp"):
        """
        Method will set gw protocol
        :param number:
        :param gw: arp, ping, none
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-check-gateway=' + gw] )
        return filt

    def setDisabled(self,number):
        """
        Method will set action to be disabled
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-disabled=yes'] )
        return filt

    def unsetDIsabled(self,number):
        """
        Method will unset disable status of action
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-disabled=no'] )
        return filt

    def setType(self,number,type="prohibit"):
        """
        Method will set type
        :param number:
        :param type: blackhole,prohibit,unicast,unreachable
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-type='+type] )
        return filt

    def setRouteTag(self,number,tag="10"):
        """
        Method will set route tag
        :param number:
        :param tag:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-route-tag='+tag] )
        return filt

    def setUseTeNextHop(self,number):
        """
        Method will use te nhop
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-use-te-nexthop=yes'] )
        return filt

    def unsetUseTeNextHop(self, number):
        """
        Method will use te nhop
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-use-te-nexthop=no'] )
        return filt

    def setRouteTargets(self,number,tgts="1:10"):
        """
        Method will s
        :param number:
        :param tgts:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-route-targets='+tgts] )
        return filt

    def setAppendRouteTargets(self,number,tgts="1:10"):
        """
        Method will append route targets
        :param number:
        :param tgts:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=append-route-targets=' + tgts] )
        return filt

    def setSIteOfOrigin(self,number,orig="1:10"):
        """
        Methodwill set site of origin
        :param number:
        :param orig:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-site-of-origin=' + orig] )
        return filt

    def setInNextHopIpv6(self,number,ipv6):
        """
        Method will set ipv6 nhop
        :param number:
        :param ipv6:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop-ipv6=' + ipv6] )
        return filt

    def setInNextHopIpv6LinkLocal(self,number,ipv6,iface="ether1"):
        """
        Method will set ipv6 link local
        :param number:
        :param ipv6:
        :param iface
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-in-nexthop-linklocal='+ipv6+"%"+iface] )
        return filt

    def setOutNextHopIpv6(self,number,nhop):
        """
        Method will set nhop ipv6
        :param number:
        :param nhop:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-out-nexthop-ipv6=' + nhop] )
        return filt

    def setOutNextHopLinkLOcal(self,number,ipv6):
        """
        Method wil set nhop ipv6
        :param number:
        :param ipv6:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=set-out-nexthop-linklocal=' + ipv6] )
        return filt