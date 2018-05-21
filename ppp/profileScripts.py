from tikapy import TikapyClient
from tikapy import TikapySslClient

class profileScripts:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setOnUpScript(self,name,script):
        """
        Method will set on up script
        :param name:
        :param script:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=on-up='+script])
        return ppp

    def setOnDownScript(self,name,script):
        """
        Method will set on down script
        :param name:
        :param script:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=on-down='+script])
        return ppp