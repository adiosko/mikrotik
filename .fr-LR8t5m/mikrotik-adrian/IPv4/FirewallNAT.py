from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallNAT:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRules(self):
        """
        Method will list all rules
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/print'] )
        return ip

    def addMasquarade(self,interface):
        ip= self.client.talk(['/ip/firewall/nat/add','=chain=srcnat','=action=masquerade','=out-interface='+interface])
        return ip

    def addSrcNat(self,protocol,toAddress,srcPort=None,toPort=None,outInterface=None):
        ip = self.client.talk(['/ip/firewall/nat/add','=chain=srcnat','=action=src-nat','=protocol='+protocol,'=to-addresses='+toAddress,'=src-port='+srcPort,'=to-ports='+toPort,'=out-interface='+outInterface])
        return ip

    def addDstNat(self,protocol,toAddress,dstaddress,dstPort=None,toPort=None,interface=None):
        ip = self.client.talk(['/ip/firewall/nat/add','=chain=dstnat','=action=dst-nat','=protocol='+protocol,'=to-addresses='+toAddress,'=dst-address='+dstaddress,'=dst-port='+dstPort,'=to-ports='+toPort,'=in-interface='+interface])
        return ip

    def addSrcAccept(self,srcAddress,dstAddress=None,protocol=None,srcPort=None,dstPort=None):
        ip = self.client.talk( ['/ip/firewall/nat/add', '=chain=srcnat', '=action=accept', '=src-address=' + srcAddress,
                                '=dst-address=' + dstAddress, '=protocol=' + protocol, '=src-port=' + srcPort,
                                '=dst-port=' + dstPort] )
        return ip

    def addDstAccept(self,dstAddress,srcAddress=None,protocol=None,srcPort=None,dstPort=None):
        ip = self.client.talk( ['/ip/firewall/nat/add', '=chain=dstnat', '=action=accept', '=dst-address=' + srcAddress,
                                '=src-address=' + dstAddress, '=protocol=' + protocol, '=src-port=' + srcPort,
                                '=dst-port=' + dstPort] )

    def addRule(self, chain="srcnat"):
        """
        Method will add rule
        :param chain: srcnat,dstnat
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/add', '=chain=' + chain] )
        return ip

    def removeRule(self, number):
        """
        Method will remove rule by rule number
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/remove', '=numbers=' + number] )
        return ip

    def enableRule(self, number):
        """
        Method will enable rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/enable', '=numbers=' + number] )
        return ip

    def disableRule(self, number):
        """
        Method will disable rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/disable', '=numbers=' + number] )
        return ip

    def commentRule(self, number, comment):
        """
        Method will comment rule
        :param number:
        :param comment:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/comment', '=numbers=' + number, '=comment=' + comment] )
        return ip

    def resetCounter(self, number):
        """
        Method will reset current counter
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/reset-counters', '=numbers=' + number] )
        return ip

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/reset-counters-all'] )
        return ip