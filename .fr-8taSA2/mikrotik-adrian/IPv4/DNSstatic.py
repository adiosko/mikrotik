from tikapy import TikapyClient
from tikapy import TikapySslClient

class DNSstatic:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRecords(self):
        """
        Method will list all static records
        :return:
        """
        dns = self.client.talk(['/ip/dns/static/print'])
        return dns

    def addRecord(self,name,address):
        """
        Method will add record
        :param name:
        :param address:
        :return:
        """
        dns = self.client.talk(['/ip/dns/static/add','=name='+name,'=address='+address])
        return dns

    def removeRecord(self,name):
        """
        Method will remove record
        :param name:
        :return:
        """
        dns = self.client.talk(['/ip/dns/static/remove','=numbers='+name])
        return dns

    def enableRecord(self,name):
        """
        Method will enable record
        :param name:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/static/enable', '=numbers=' + name] )
        return dns

    def disableRecord(self,name):
        """
        Method will disable record
        :param name:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/static/disable', '=numbers=' + name] )
        return dns

    def commentRecord(self,name,comment):
        """
        Method will comment record
        :param name:
        :param comment:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/static/comment', '=numbers=' + name,'=comment='+comment] )
        return dns

    def setName(self,name,newName):
        """
        Method will rename name of server
        :param name:
        :param newName:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/static/set', '=numbers=' + name, '=name=' + newName] )
        return dns

    def setAddress(self,name,address):
        """
        Method will set address
        :param name:
        :param address:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/static/set', '=numbers=' + name, '=address=' + address] )
        return dns

    def setTtl(self,name,ttl="1d 00:00:00"):
        """
        Method will set ttl for dns
        :param name:
        :param ttl:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/static/set', '=numbers=' + name, '=ttl=' + ttl] )
        return dns