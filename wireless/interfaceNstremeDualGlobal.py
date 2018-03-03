from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceNstreamDualGlobal:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNstream(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/nstreme-dual/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addInterface(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/nstreme-dual/add'])
        return wifi

    def removeInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/remove','=numbers='+name] )
        return wifi

    def enableInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/enable','=numbers='+name] )
        return wifi

    def disableInterface(self,name):
        """
        Method will remove iface
        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/disable','=numbers='+name] )
        return wifi

    def commentInterface(self,name,comment):
        """
        Method will remove iface
        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/comment','=numbers='+name,'=comment='+comment] )
        return wifi