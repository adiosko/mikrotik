from tikapy import TikapyClient
from tikapy import TikapySslClient

class RouteGeneral:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)


    def listRoutes(self):
        """
        Method will list routes
        :return:
        """
        route = self.client.talk(['/ip/route/print'])
        print("Dst address\tGateway\tDistance\tPref source")
        for i in route:
            print(route[i]['dst-address']+"\t"+route[i]['gateway']+"\t"+route[i]['distance']+"\t"+route[i]['pref-src'])
        return route


    def addRoute(self,dst,gw):
        """
        Method will add route
        :param dst:
        :param gw:
        :return:
        """
        route = self.client.talk(['/ip/route/add','=dst-address='+dst,'=gateway='+gw])
        return route

    def removeRoute(self,number):
        """
        Method will remove route
        :param number:
        :return:
        """
        route = self.client.talk(['/ip/route/remove','=numbers='+number])
        return route

    def enableRoute(self,number):
        """
        Method will enable route
        :param number:
        :return:
        """
        route = self.client.talk( ['/ip/route/enable', '=numbers=' + number] )
        return route

    def disableRoute(self,number):
        """
        Method will disable route
        :param number:
        :return:
        """
        route = self.client.talk( ['/ip/route/disable', '=numbers=' + number] )
        return route

    def commentRoute(self,number,comment):
        """
        Method will comment route
        :param number:
        :param comment:
        :return:
        """
        route = self.client.talk( ['/ip/route/comment', '=numbers=' + number,'=comment='+comment] )
        return route

    #General
    def setDstAddress(self,number,dst):
        """
        Method will set dst address
        :param number:
        :param dst:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=dst-address=' + dst] )
        return route

    def setGateway(self,number,gw):
        """
        Method will set gateway of the route
        :param number:
        :param gw:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=gateway=' + gw] )
        return route

    def checkGateway(self,number,check="ping"):
        """
        Method will set method to check gateway
        :param number:
        :param check: ping, arp
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=check-gateway=' + check] )
        return route

    def setType(self,number,route="unicast"):
        """
        Method will set route type
        :param number:
        :param route: unicast, blackhole, prohibit, unreachable
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=type=' + route] )
        return route

    def setDistance(self,number,distance="1"):
        """
        Method will set distance
        :param number:
        :param distance:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=distance=' + distance] )
        return route

    def setScope(self,number,scope="30"):
        """
        Method will set scope
        :param number:
        :param scope:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=scope=' + scope] )
        return route

    def setTargetScope(self,number,scope="100"):
        """
        Method will set tgt scope
        :param number:
        :param scope:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=target-scope=' + scope] )
        return route

    def setRoutingMark(self,number,mark="main"):
        """
        Method will set routing mark == table
        :param number:
        :param mark:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=routing-mark=' + mark] )
        return route

    def setPrefSoure(self,number,src):
        """
        Method will set pref source
        :param number:
        :param src:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=pref-src=' + src] )
        return route

    #Attributes
    def setBgpAsPath(self,number,AS="1"):
        """
        Method will set bgp as path
        :param number:
        :param AS:
        :return:
        """
        route = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-as-path=' + AS] )
        return route

    def setBgpLocPref(self, number, lpref="0"):
        """
        Method will set bgp local preference
        :param number:
        :param wight:
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-local-pref=' + lpref] )
        return ip

    def setBgpPrepend(self, number, prepend="0"):
        """
        Method will set prepend
        :param number:
        :param prepend:
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-prepend=' + prepend] )
        return ip

    def setBgpMed(self, number, med="0"):
        """
        Method will set median
        :param number:
        :param med:
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-med=' + med] )
        return ip

    def setAtomicAgregation(self, number, agreg="present"):
        """
        Method will set agregation
        :param number:
        :param agreg: present,absent
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-atomic-aggregate=' + agreg] )
        return ip

    def setBgpOrigin(self, number, orig="igp"):
        """
        Method will set agregation
        :param number:
        :param orig: igp, egp, incomplete
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-origin=' + orig] )
        return ip

    def setBgpCOmmunities(self, number, comm="0:0"):
        """
        Method will set bgp communities
        :param number:
        :param comm:
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=bgp-communities=' + comm] )
        return ip

    def setROuteTag(self, number, tag="0"):
        """
        Method will set route tag
        :param number:
        :param tag:
        :return:
        """
        ip = self.client.talk( ['/ip/route/set', '=numbers=' + number, '=route-tag=' + tag] )
        return ip