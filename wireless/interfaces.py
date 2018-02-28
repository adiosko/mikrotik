from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaces:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list interfaces
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addInterface(self,masterIface):
        """

        :param masterIface:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/add','=master-interface='+masterIface] )
        return wifi

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/remove', '=numbers=' + name] )
        return wifi

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/enable', '=numbers=' + name] )
        return wifi

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/disable', '=numbers=' + name] )
        return wifi

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/comment', '=numbers=' + name,'=comment='+comment] )
        return wifi