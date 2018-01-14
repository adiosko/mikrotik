from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsSettings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setDynamicLabelRange(self,range="16-1048575"):
        """
        Method will set label range
        :param range:
        :return:
        """
        mpls = self.client.talk(['/mpls/set','=dynamic-label-range='+range])
        return mpls

    def setPropagateTtl(self):
        """
        Method will propagate tls
        :return:
        """
        mpls = self.client.talk( ['/mpls/set', '=propagate-ttl=yes'] )
        return mpls

    def unsetPropagateTtl(self):
        """
        Method will unset ttl propagation
        :return:
        """
        mpls = self.client.talk( ['/mpls/set', '=propagate-ttl=no'] )
        return mpls