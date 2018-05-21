from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppServerSetDialIn:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setAuthentication(self,name,auth="mschap2,mschap1,chap,pap"):
        """
        Method will rename iface
        :param name:
        :param auth: mschap2,mschap1,pap,chap
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-server/set','=numbers='+name,'=authentication='+auth])
        return ppp

    def setProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile: default,default-encryption
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=profile=' + profile] )
        return ppp

    def setRingCount(self,name,count="1"):
        """

        :param name:
        :param count:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=ring-count=' + count] )
        return ppp