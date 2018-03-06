from tikapy import TikapyClient
from tikapy import TikapySslClient

class DataPath:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listDataPath(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/datapath/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addDataPath(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/datapath/add','=name='+name])
        return wifi

    def removedatapath(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/remove', '=numbers=' + name] )
        return wifi

    def commentdatapath(self,name,comment):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/remove', '=numbers=' + name,'=comment='+comment] )
        return wifi