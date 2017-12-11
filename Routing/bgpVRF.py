from tikapy import TikapyClient
from tikapy import TikapySslClient

class bgpVRF:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listVrf(self):
        """
        Method will list vrf instances
        :return:
        """
        vrf = self.client.talk(['/routing/bgp/instance/vrf/print'])
        if vrf == {}:
            print("No vrf set")
        else:
            print("Instance\tRouting mark\tin filter \t out filter")
            for i in vrf:
                #print(vrf)
                print(vrf[i]['instance']+"\t"+vrf[i]['routing-mark']+"\t"+vrf[i]['in-filter']+"\t"+vrf[i]['out-filter'])
        return vrf

    def addVrf(self,routingMark):
        """
        Method will add new vrf instance
        :param routingMark: routing table except from main
        :return:
        """
        vrf = self.client.talk(['/routing/bgp/instance/vrf/add','=routing-mark='+routingMark])
        return vrf

    def removeVrf(self,number):
        """
        Method will remove brf instance
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/remove', '=numbers=' + number] )
        return vrf

    def disableVrf(self,number):
        """
        Method will disable instance
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/disable', '=numbers=' + number] )
        return vrf

    def enableVrf(self,number):
        """
        Method will enable vrf instance
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/enable', '=numbers=' + number] )
        return vrf

    def commentVrfInstance(self,number,comment):
        """
        Method will comment vrf
        :param number:
        :param comment:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/comment', '=numbers=' + number,'=comment='+comment] )
        return vrf

    def setVrfInstance(self,number,instance):
        """
        Method will set instance vrf
        :param number:
        :param instance: default or created name f.e bgp
        :return:
        """
        vrf = self.client.talk(['/routing/bgp/instance/vrf/set','=numbers='+number,'=instance='+instance])
        return vrf

    def setRoutingMArk(self,number,mark):
        """
        Method will set routing mark
        :param number:
        :param mark: bgp or default or custom
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=routing-mark=' + mark] )
        return vrf

    def setRedistributeConnected(self,number):
        """
        Method will enable connected nwks
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=redistribute-connected=yes'] )
        return vrf

    def setRedistributeStatic(self, number):
        """
        Method will enable connected nwks
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=redistribute-static=yes'] )
        return vrf

    def setRedistributeRIP(self, number):
        """
        Method will enable connected nwks
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=redistribute-rip=yes'] )
        return vrf

    def setRedistributeOSPF(self, number):
        """
        Method will enable connected nwks
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=redistribute-ospf=yes'] )
        return vrf

    def setRedistributeBGP(self, number):
        """
        Method will enable connected nwks
        :param number:
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=redistribute-other-bgp=yes'] )
        return vrf

    def setInFilter(self,number,filter):
        """
        Method will set input filter
        :param number:
        :param filter: connected-in,dynamic-in,rip-in,rip-out
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=in-filter='+filter] )
        return vrf

    def setOutputFilter(self,number,filter):
        """
        Method will set output filter
        :param number:
        :param filter: filter: connected-in,dynamic-in,rip-in,rip-out
        :return:
        """
        vrf = self.client.talk( ['/routing/bgp/instance/vrf/set', '=numbers=' + number, '=out-filter='+filter] )
        return vrf