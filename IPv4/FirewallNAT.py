from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallNAT:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRules(self):
        """
        Method will list all rules
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/print'] )
        if ip == {}:
            print( "No rule found,ssecure your router!!!" )
        else:
            print( "Action\tChain\tSrcAddress\tDstAddress\tProtocol\tSrcPort\tDstPort\tInInterface\tOutinterface" )
            for i in ip:
                print( ip[i] )
                # print(ipv6[i]['action']+"\t"+ipv6[i]['chain']+"\t"+ipv6[i]['src-address']+"\t"+ipv6[i]['dst-address']+"\t"+ipv6[i]['protocol']+ipv6[i]['src-port'+"\t"+ipv6[i]['dst-port']+"\t"+ipv6[i]['in-interface']+"\t"+ipv6[i]['out-interface']])
        return ip

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