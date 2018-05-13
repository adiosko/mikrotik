from tikapy import TikapyClient
from tikapy import TikapySslClient


class provisioning:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listProvisioning(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addProvisioning(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/add'])
        return wifi

    def removeProvisioning(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/provisioning/remove','=numbers='+number] )
        return wifi

    def enableProvisioning(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/provisioning/enable','=numbers='+number] )
        return wifi

    def disableProvisioning(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/provisioning/disable', '=numbers=' + number] )
        return wifi

    def commentProvisioning(self,number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/provisioning/comment', '=numbers=' + number,'=comment='+comment] )
        return wifi