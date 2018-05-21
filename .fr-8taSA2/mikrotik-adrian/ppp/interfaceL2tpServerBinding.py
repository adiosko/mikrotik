from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceL2tpServerBinding:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listIfaces(self):
        """
        Method will list ppp client ifaces
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/print'])
        for i in ppp:
            print(ppp[i])
        return ppp

    def addInterface(self,user):
        """
        Metho dwill add iface
        :param user:
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/add','=user='+user])
        return ppp

    def removeInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/l2tp-server/remove','=numbers='+name] )
        return ppp

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/l2tp-server/enable', '=numbers=' + name] )
        return ppp

    def disableInterface(self,name):
        """
        Method wil ldisable interface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/l2tp-server/disable', '=numbers=' + name] )
        return ppp

    def commentInterface(self,name,comment):
        """
        Method will coment iface
        :param name:
        :param comment:
        :return:
        """
        ppp = self.client.talk( ['/interface/l2tp-server/comment', '=numbers=' + name,'=comment='+comment] )
        return ppp