from tikapy import TikapyClient
from tikapy import TikapySslClient

class SmbShare:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

        # Shared
        def listShares(self):
            """
            Method will list shares
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/print'] )
            print( "Name\tDirectory\tMax sessions" )
            for i in smb:
                print( smb[i]['name'] + "\t" + smb[i]['directory'] + "\t" + smb[i]['max-sessions'] )
            return smb

        def addShare(self, name, dir):
            """
            Method will remove share
            :param name:
            :param dir:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/add', '=name=' + name, '=directory=' + dir] )
            return smb

        def removeShare(self, name):
            """
            Method will remove share
            :param name:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/remove', '=numbers=' + name] )
            return smb

        def enableShare(self, name):
            """
            Method will enable share
            :param name:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/enable', '=numbers=' + name] )
            return smb

        def disableShare(self, name):
            """
            Method will disable share
            :param name:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/disable', '=numbers=' + name] )
            return smb

        def commentShare(self, name, comment):
            """
            Method will comment share
            :param name:
            :param comment:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/comment', '=numbers=' + name, '=comment=' + comment] )
            return smb

        def setName(self, name, newName):
            """
            Method will rename share
            :param name:
            :param newName:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/set', '=numbers=' + name, '=name=' + newName] )
            return smb

        def setDirectory(self, name, directory):
            """
            Method will set dir
            :param name:
            :param directory:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/set', '=numbers=' + name, '=directory=' + directory] )
            return smb

        def setMaxSessions(self, name, session):
            """
            Method will set max sessions
            :param name:
            :param session:
            :return:
            """
            smb = self.client.talk( ['/ip/smb/shares/set', '=numbers=' + name, '=max-sessions=' + session] )
            return smb