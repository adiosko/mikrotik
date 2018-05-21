from tikapy import TikapyClient
from tikapy import TikapySslClient


class vrrpScriptSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def setOnMasterScript(self,name,script):
        """

        :param name:
        :param script:
        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/set','=numbers='+name,'=on-master='+script])
        return vrrp

    def setOnBackupScript(self,name,script):
        """

        :param name:
        :param script:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=on-backup=' + script] )
        return vrrp