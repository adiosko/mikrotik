from tikapy import TikapyClient
from tikapy import TikapySslClient

class security:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def listSecurity(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/security/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addSecurity(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/caps-man/security/add','=name='+name])
        return wifi

    def removeSecurity(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/remove', '=numbers=' + name] )
        return wifi

    def commentSecurity(self,name,comment):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/remove', '=numbers=' + name,'=comment='+comment] )
        return wifi