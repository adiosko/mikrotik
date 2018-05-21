from tikapy import TikapyClient
from tikapy import TikapySslClient

class profileProtocols:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def useMpls(self,name,mpls="default"):
        """
        Method will set usage of mpls
        :param name:
        :param mpls: no,yes,requiered,default
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=use-mpls='+mpls])
        return ppp

    def useCOmpression(self,name,compress="default"):
        """
        Method will set compression usage
        :param name:
        :param compress: no,yes,default
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=use-compression=' + compress])
        return ppp

    def useEncryption(self,name,encrypt="default"):
        """
        Method will set usage of encryption
        :param name:
        :param encrypt: no,yes,requiered,default
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=use-encryption=' + encrypt])
        return ppp