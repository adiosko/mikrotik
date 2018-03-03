from tikapy import TikapyClient
from tikapy import TikapySslClient

class accessList:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listAccessList(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/access-list/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addAccessList(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/access-list/add'])
        return wifi

    def removeAccessList(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/access-list/remove','=numbers='+number])
        return wifi

    def enableAccessList(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/enable', '=numbers=' + number] )
        return wifi

    def disableAccessList(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/disable', '=numbers=' + number] )
        return wifi

    def commentAccessList(self,number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/comment', '=numbers=' + number,'=comment='+comment] )
        return wifi