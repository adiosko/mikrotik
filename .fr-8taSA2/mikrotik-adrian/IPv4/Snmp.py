from tikapy import TikapyClient
from tikapy import TikapySslClient

class Snmp:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enable(self):
        """
        Method will enable snmp
        :return:
        """
        snmp = self.client.talk(['/snmp/set','=enabled=yes'])
        return snmp

    def disable(self):
        """
        Method will disable snmp
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=enabled=no'] )
        return snmp

    def setContactInfo(self,contact):
        """
        Method will set contact
        :param contact:
        :return:
        """
        snmp = self.client.talk(['/snmp/set','=contact='+contact])
        return snmp

    def setLocation(self,location):
        """
        Method will set location
        :param location:
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=location=' + location] )
        return snmp

    def setEngineId(self,engine):
        """
        Method will set engine id
        :param engine:
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=engine-id=' + engine] )
        return snmp

    def setTrapTgt(self,trap):
        """
        Method will set trap target
        :param trap:
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=trap-target=' + trap] )
        return snmp

    def setTrapCommunity(self,community="public"):
        """
        Method will set community
        :param community: public or custom
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=trap-community=' + community] )
        return snmp

    def setTrapVersion(self,version="1"):
        """
        Method will set trap version
        :param version: 1,2,3
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=trap-version=' + version] )
        return snmp

    def setTrapGenerator(self,gen="intrerfaces"):
        """
        Method will set rrap generator
        :param gen: interfaces, start-trap
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=trap-generators=' + gen] )
        return snmp

    def setTrapInterface(self,interface="all"):
        """
        Method will set trap iface
        :param interface:
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=trap-interfaces=' + interface] )
        return snmp

    def setSrcAddress(self,src="::"):
        """
        Method will set src address
        :param src:
        :return:
        """
        snmp = self.client.talk( ['/snmp/set', '=src-address=' + src] )
        return snmp