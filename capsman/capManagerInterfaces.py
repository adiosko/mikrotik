from tikapy import TikapyClient
from tikapy import TikapySslClient

class capManagerInterfaces:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def listInterfaces(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addInterface(self,interface="all"):
        """

        :param interface:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/add','=interface='+interface])
        return wifi

    def removeInterface(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/remove','=numbers='+number])
        return wifi

    def enableInterface(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/enable', '=numbers=' + number])
        return wifi

    def disableInterface(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/disable', '=numbers=' + number])
        return wifi

    def commentInterface(self,number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/comment', '=numbers=' + number,'=comment='+comment])
        return wifi

    def setInterface(self,number,interface="all"):
        """

        :param number:
        :param interface:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/set', '=numbers=' + number,'=interface='+interface])
        return wifi

    def forbidInterface(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/set', '=numbers=' + number,'=forbid=yes'])
        return wifi

    def notForbidInterface(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/interface/set', '=numbers=' + number,'=forbid=no'])
        return wifi