from tikapy import TikapyClient
from tikapy import TikapySslClient

class Smb:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enable(self):
        """
        Method will enable smb
        :return:
        """
        smb = self.client.talk(['/ip/smb/set','=enabled=yes'])
        return smb

    def disable(self):
        """
        Method will disable smb
        :return:
        """
        smb = self.client.talk( ['/ip/smb/set', '=enabled=no'] )
        return smb

    def setDomain(self,domain):
        """
        Method will set domain
        :param domain:
        :return:
        """
        smb = self.client.talk(['/ip/smb/set','=domain='+domain])
        return smb

    def setComment(self,comment):
        """
        Method will set
        :param comment:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/set', '=comment='+comment] )
        return smb

    def AllowGuests(self):
        """
        Method will allow guests
        :return:
        """
        smb = self.client.talk( ['/ip/smb/set', '=allow-guests=yes'] )
        return smb

    def setInterface(self,iface="all"):
        """
        Method will se tinterface
        :param iface:
        :return:
        """
        smb = self.client.talk( ['/ip/smb/set', '=interfaces='+iface] )
        return smb