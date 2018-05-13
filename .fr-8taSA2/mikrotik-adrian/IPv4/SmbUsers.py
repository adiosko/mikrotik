from tikapy import TikapyClient
from tikapy import TikapySslClient

class SmbUsers:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

        # Users
    def listUsers(self):
        """
        Method will list users
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/print'] )
        print( "Name\tPassword\tReads only" )
        for i in smb:
            print( smb[i]['name'] + "\t" + smb[i]['password'] + "\t" + smb[i]['read-only'] )
        return smb

    def addUser(self, name, password):
        """
        Method will add user
        :param name:
        :param password:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/add', '=name=' + name, '=password=' + password] )
        return smb

    def removeUser(self, name):
        """
        Method will remove user
        :param name:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/remove', '=numbers=' + name] )
        return smb

    def enableUser(self, name):
        """
        Method will enable user
        :param name:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/enable', '=numbers=' + name] )
        return smb

    def disableUser(self, name):
        """
        Method will disable user
        :param name:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/disable', '=numbers=' + name] )
        return smb

    def setUser(self, name, newName):
        """
        Method will set username
        :param name:
        :param newName:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/set', '=numbers=' + name, '=name=' + newName] )
        return smb

    def setPassword(self, name, password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/set', '=numbers=' + name, '=password=' + password] )
        return smb

    def readOnlyUser(self, name):
        """
        Method will set user as read only user
        :param name:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/set', '=numbers=' + name, '=read-only=yes'] )
        return smb

    def writeUser(self, name):
        """
        Method will set user as write priviledges user
        :param name:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/users/set', '=numbers=' + name, '=read-only=no'] )
        return smb