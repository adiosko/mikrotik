from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppclient:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listIfaces(self):
        """
        Method will list ppp client ifaces
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-client/print'])
        for i in ppp:
            print(ppp[i])
        return ppp

    def addInterface(self):
        """
        Metho dwill add iface
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-client/add'])
        return ppp

    def removeInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/remove','=numbers='+name] )
        return ppp

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/enable', '=numbers=' + name] )
        return ppp

    def disableInterface(self,name):
        """
        Method wil ldisable interface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/disable', '=numbers=' + name] )
        return ppp

    def commentInterface(self,name,comment):
        """
        Method will coment iface
        :param name:
        :param comment:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/comment', '=numbers=' + name,'=comment='+comment] )
        return ppp