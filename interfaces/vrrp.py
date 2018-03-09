from tikapy import TikapyClient
from tikapy import TikapySslClient


class vrrp:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listInterfaces(self):
        """

        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/print'])
        for i in vrrp:
            print(vrrp)
        return vrrp

    def addInterface(self,name,interface):
        """

        :param name:
        :param interface:
        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/add','=name='+name,'=interface='+interface])
        return vrrp

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/remove','=numbers='+name])
        return vrrp

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/enable','=numbers='+name])
        return vrrp

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/disable', '=numbers=' + name] )
        return vrrp

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/comment', '=numbers=' + name,'=comment='+comment] )
        return vrrp