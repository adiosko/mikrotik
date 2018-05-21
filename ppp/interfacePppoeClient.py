from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppoeClient:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listIfaces(self):
        """
        Method will list pppoe client ifaces
        :return:
        """
        pppoe = self.client.talk(['/interface/pppoe-client/print'])
        for i in pppoe:
            print(pppoe[i])
        return pppoe

    def addInterface(self,interface):
        """
        Metho dwill add iface
        :param user:
        :return:
        """
        pppoe = self.client.talk(['/interface/pppoe-client/add','=interface='+interface])
        return pppoe

    def removeInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/remove','=numbers='+name] )
        return pppoe

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/enable', '=numbers=' + name] )
        return pppoe

    def disableInterface(self,name):
        """
        Method wil ldisable interface
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/disable', '=numbers=' + name] )
        return pppoe

    def commentInterface(self,name,comment):
        """
        Method will coment iface
        :param name:
        :param comment:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/comment', '=numbers=' + name,'=comment='+comment] )
        return pppoe