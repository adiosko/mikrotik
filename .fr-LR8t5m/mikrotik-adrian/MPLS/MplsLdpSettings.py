from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsLdpSettings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enableLdp(self):
        """
        Method will enable ldp
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/set','=enabled=yes'])
        return mpls

    def disableLdp(self):
        """
        Method will disable ldp
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=enabled=no'])
        return mpls

    def setLsrId(self,id="0.0.0.0"):
        """
        Method will set lsr id
        :param id: ip address
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/set', '=lsr-id='+id])
        return mpls

    def setTransparentAddress(self,address="0.0.0.0"):
        """
        Method will set transparent address
        :param address: IP
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=transport-address=' + address] )
        return mpls

    def setPathVectorLimit(self,limit="255"):
        """
        Method will set path vector limit
        :param limit: max 255
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=path-vector-limit=' + limit] )
        return mpls

    def setHopLimit(self,limit="255"):
        """
        Method will set hop limit max 255
        :param limit:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=hop-limit=' + limit] )
        return mpls

    def enableLoopDetect(self):
        """
        Method will enable loop detection
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=loop-detect=yes'] )
        return mpls

    def useExplicitNull(self):
        """
        Methodwill use explicit null
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=use-explicit-null=yes'] )
        return mpls

    def distributeForDefaultRoute(self):
        """
        Method will distribute default route
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/set', '=distribute-for-default-route=yes'] )
        return mpls