from tikapy import TikapyClient
from tikapy import TikapySslClient


class interface:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listInterfaces(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addInterface(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/add'])
        return wifi

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/remove','=numbers='+name])
        return wifi

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/enable', '=numbers=' + name] )
        return wifi

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/disable', '=numbers=' + name] )
        return wifi

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/comment', '=numbers=' + name,'=comment='+comment] )
        return wifi