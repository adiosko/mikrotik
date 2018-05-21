from tikapy import TikapyClient
from tikapy import TikapySslClient

class SpecialLogin:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listSPecialLogins(self):
        """
        Method will list all special logins
        :return: list
        """
        usr = self.client.talk(['/special-login/print'])
        for i in usr:
            print(usr)
        return usr

    def addSpecialUser(self,username,port,disbled):
        """
        Method will add special username
        :param username: special username created in user mgmt
        :param port: serial0
        :param disbled: no/yes
        :return: list
        """
        usr = self.client.talk(['/special-login/add','=user='+username,'=port='+port,'=disabled='+disbled])
        return usr

    def setSPecialUser(self,username,port,disabled):
        """
        Method will setup existing user
        :param username: username to edit
        :param port: port
        :param disabled: disable yes/no
        :return: list
        """
        usr = self.client.talk(['/special-login/set','=numbers='+username,'=port='+port,'=disabled='+disabled])
        return usr

    def removeSPecialUser(self,username):
        """
        Method will remove special login
        :param username: username
        :return: list
        """
        usr = self.client.talk(['/special-login/remove','=numbers='+username])
        return usr

    def enableSpecialUser(self,username):
        """
        Method will enable special user
        :param username: username to enable
        :return: list
        """
        usr = self.client.talk(['/special-login/enable','=numbers='+username])
        return usr

    def disableSpecialUser(self,username):
        """
        Method will disable special username
        :param username: username to disable
        :return: list
        """
        usr = self.client.talk(['/special-login/disable','=numbers='+username])
        return usr