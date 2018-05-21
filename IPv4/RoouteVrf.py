from tikapy import TikapyClient
from tikapy import TikapySslClient

class RouteVrf:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listVrf(self):
        """
        Method will list vrf
        :return:
        """
        vrf = self.client.talk(['/ip/route/vrf/print'])
        print("Routing mark\tInterfaces\troute distinguisher")
        for i in vrf:
            print(vrf[i]['routing-mark']+"\t"+vrf[i]['interfaces']+"\t"+vrf[i]['route-distinguisher'])
        return vrf

    def addVrf(self,mark,interface):
        """
        Method will add vrf
        :param mark: routing mark
        :param interface:
        :return:
        """
        vrf = self.client.talk(['/ip/route/vrf/add','=routing-mark='+mark,'=interfaces='+interface])
        return vrf

    def removeVrf(self,number):
        """
        Method will remove vrf
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/remove','=numbers='+number] )
        return vrf

    def enableVrf(self,number):
        """
        Method will enable vrf
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/enable', '=numbers=' + number] )
        return vrf

    def disableVrf(self, number):
        """
        Method will disable vrf
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/disable', '=numbers=' + number] )
        return vrf

    def commentVrf(self,number,comment):
        """
        Method will comment vrf
        :param number:
        :param comment:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/comment', '=numbers=' + number,'=comment='+comment] )
        return vrf

    def setRoutingMark(self,number,mark):
        """
        Method will set routing mark
        :param number:
        :param mark: routing mark
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/set', '=numbers=' + number, '=routing-mark=' + mark] )
        return vrf

    def setInterfaces(self,number,interfaces):
        """
        Method will set interfaces
        :param number:
        :param interfaces:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/set', '=numbers=' + number, '=interfaces=' + interfaces] )
        return vrf

    def setRouteDistinguisher(self,number,dist="0:0"):
        """
        Method will set route distinguisher
        :param number:
        :param dist:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/set', '=numbers=' + number, '=route-distinguisher=' + dist] )
        return vrf

    def setImportRouteTarget(self,number,tgt="0:0"):
        """
        Method will set route target import
        :param number:
        :param tgt:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/set', '=numbers=' + number, '=import-route-targets=' + tgt] )
        return vrf

    def setExxportRouteTarget(self, number, tgt="0:0"):
        """
        Method will set route target import
        :param number:
        :param tgt:
        :return:
        """
        vrf = self.client.talk( ['/ip/route/vrf/set', '=numbers=' + number, '=export-route-targets=' + tgt] )
        return vrf