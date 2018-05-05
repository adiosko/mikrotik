from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallFilter:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRules(self):
        """
        Method will list all rules
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/print'] )
        return ip

    def addRule(self, chain="input"):
        """
        Method will add rule
        :param chain: input, forward,output
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/add', '=chain=' + chain] )
        return ip

    def addinputaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/filter/add','=chain=input','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=in-interface='+interface])
        return ip

    def addinputreject(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/filter/add','=chain=input','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=in-interface='+interface])
        return ip

    def addinputdeny(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/filter/add','=chain=input','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=in-interface='+interface])
        return ip

    def addForwardaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/filter/add','=chain=forward','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addForwardreject(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/filter/add','=chain=input','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addForwarddeny(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/filter/add','=chain=input','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip


    def removeRule(self, number):
        """
        Method will remove rule by rule number
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/remove', '=numbers=' + number] )
        return ip

    def enableRule(self, number):
        """
        Method will enable rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/enable', '=numbers=' + number] )
        return ip

    def disableRule(self, number):
        """
        Method will disable rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/disable', '=numbers=' + number] )
        return ip

    def commentRule(self, number, comment):
        """
        Method will comment rule
        :param number:
        :param comment:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/comment', '=numbers=' + number, '=comment=' + comment] )
        return ip

    def resetCounter(self, number):
        """
        Method will reset current counter
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/reset-counters', '=numbers=' + number] )
        return ip

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/reset-counters-all'] )
        return ip