from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPv6Route:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listROutes(self):
        """
        Method will list routes
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/route/print'])
        if ipv6 == {}:
            print("No route found")
        else:
            print("Dst address\tGateway\tDisatnce")
            for i in ipv6:
                print(ipv6[i]['dst-address']+"\t"+ipv6[i]['gateway']+"\t"+ipv6[i]['distance'])
        return ipv6

    def addRoute(self,dst,gw):
        """
        Method will add routes
        :param dst: dst address subnet
        :param gw: gw address/interface
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/route/add','=dst-address='+dst,'=gateway='+gw])
        return ipv6

    def removeRoute(self,number):
        """
        Method will remove route
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/route/remove','=numbers='+number])
        return ipv6

    def enableRoute(self,number):
        """
        Method will enable route
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/enable', '=numbers=' + number] )
        return ipv6

    def disableROute(self,number):
        """
        Method will remove route
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/disable', '=numbers=' + number] )
        return ipv6

    def commentRoute(self,number,comment):
        """
        Method will comment rroute
        :param number:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv6

    #general
    def setDst(self,number,dst):
        """
        Method will set destination address
        :param number:
        :param dst:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/route/set','=numbers='+number,'=dst-address='+dst])
        return ipv6

    def setGateway(self,number,gw):
        """
        Method will set gw
        :param number:
        :param gw: interface or address
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=gateway=' + gw] )
        return ipv6

    def setCheckGateway(self,number,gw="ping"):
        """
        Method will check gateway
        :param number:
        :param gw: ping
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=check-gateway=' + gw] )
        return ipv6

    def setRouteType(self,number,type="unicast"):
        """
        Method will set route btype
        :param number:
        :param type: unicast/unreachable
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=type=' + type] )
        return ipv6

    def setDistance(self,number,distance="1"):
        """
        Method will set distance
        :param number:
        :param distance:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=distance=' + distance] )
        return ipv6

    def setScope(self,number,scope="30"):
        """
        Method will set scope
        :param number:
        :param scope:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=scope=' + scope] )
        return ipv6

    def setTargetScope(self,number,tgt="10"):
        """
        Method will set taget scope
        :param number:
        :param tgt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=target-scope=' + tgt] )
        return ipv6

    #Attributes
    def setBgpAsPath(self,number,aspath):
        """
        Method will set as path
        :param number:
        :param aspath: as path number
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=bgp-as-path=' + aspath] )
        return ipv6

    def setBgpLocPref(self,number,lpref="0"):
        """
        Method will set bgp local preference
        :param number:
        :param wight:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=bgp-local-pref=' +lpref ] )
        return ipv6

    def setBgpPrepend(self,number,prepend="0"):
        """
        Method will set prepend
        :param number:
        :param prepend:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=bgp-prepend=' + prepend] )
        return ipv6

    def setBgpMed(self,number,med="0"):
        """
        Method will set median
        :param number:
        :param med:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=bgp-med=' + med] )
        return ipv6

    def setAtomicAgregation(self,number,agreg="present"):
        """
        Method will set agregation
        :param number:
        :param agreg: present,absent
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=bgp-atomic-aggregate=' + agreg] )
        return ipv6

    def setBgpCOmmunities(self,number,comm="0:0"):
        """
        Method will set bgp communities
        :param number:
        :param comm:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=bgp-communities=' + comm] )
        return ipv6

    def setROuteTag(self,number,tag="0"):
        """
        Method will set route tag
        :param number:
        :param tag:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/route/set', '=numbers=' + number, '=route-tag=' + tag] )
        return ipv6