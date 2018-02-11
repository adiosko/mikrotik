from tikapy import TikapyClient
from tikapy import TikapySslClient

class SnmpCommunity:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listCommunities(self):
        """
        Method will list communities
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/print'] )
        print( "Name\tAddress\tSecurity\tRead access\tWrite access" )
        for i in snmp:
            print( snmp[i]['name'] + "\t" + snmp[i]['addresses'] + "\t" + snmp[i]['security'] + "\t" + snmp[i][
                'read-access'] )
        return snmp

    def addCommunity(self, name, address):
        """
        Methdd will add community
        :param name:
        :param address:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/add', '=name=' + name, '=addresses=' + address] )
        return snmp

    def removeCommunity(self, name):
        """
        Method will remove community
        :param name:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/remove', '=numbers=' + name] )
        return snmp

    def setName(self, name, newName):
        """
        Method will set new name of community
        :param name:
        :param newName:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=name=' + newName] )
        return snmp

    def setAddresses(self, name, address):
        """
        Method will set addresses
        :param name:
        :param address:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=addresses=' + address] )
        return snmp

    def setSecuruty(self, name, sec="none"):
        """
        Method will set security
        :param name:
        :param sec: none, private, authorized
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=security=' + sec] )
        return snmp

    def readAccess(self, name):
        """
        Method will set read access
        :param name:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=read-access=yes'] )
        return snmp

    def writeAccess(self, name):
        """
        Method will set write access
        :param name:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=write-access=yes'] )
        return snmp

    def setAuthenticationProtocol(self, name, protocol="MD5"):
        """
        Method will set authentication protocol
        :param name:
        :param protocol: MD5, SHA1
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=authentication-protocol=' + protocol] )
        return snmp

    def setEncryptionProtocol(self, name, protocol="DES"):
        """
        Method will set encryption protocol
        :param name:
        :param protocol: AES, DES
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=encryption-protocol=' + protocol] )
        return snmp

    def setAuthenticationPassword(self, name, password):
        """
        Method will set authentication password
        :param name:
        :param password:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=authentication-password=' + password] )
        return snmp

    def setEncryptionPassword(self, name, password):
        """
        Method will set encrypton password
        :param name:
        :param password:
        :return:
        """
        snmp = self.client.talk( ['/snmp/community/set', '=numbers=' + name, '=encryption-password=' + password] )
        return snmp