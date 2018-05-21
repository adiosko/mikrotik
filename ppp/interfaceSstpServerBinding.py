from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceSstpServerBinding:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listIfaces(self):
        """
        Method will list ppp client ifaces
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/print'])
        for i in ppp:
            print(ppp[i])
        return ppp

    def addInterface(self,user):
        """
        Metho dwill add iface
        :param user:
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/add','=user='+user])
        return ppp

    def removeInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/sstp-server/remove','=numbers='+name] )
        return ppp

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/sstp-server/enable', '=numbers=' + name] )
        return ppp

    def disableInterface(self,name):
        """
        Method wil ldisable interface
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/sstp-server/disable', '=numbers=' + name] )
        return ppp

    def commentInterface(self,name,comment):
        """
        Method will coment iface
        :param name:
        :param comment:
        :return:
        """
        ppp = self.client.talk( ['/interface/sstp-server/comment', '=numbers=' + name,'=comment='+comment] )
        return ppp