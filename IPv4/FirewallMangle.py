from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallMangle:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRules(self):
        """
        Method will list all rules
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/print'] )
        if ip == {}:
            print( "No rule found,ssecure your router!!!" )
        else:
            print( "Action\tChain\tSrcAddress\tDstAddress\tProtocol\tSrcPort\tDstPort\tInInterface\tOutinterface" )
            for i in ip:
                print( ip[i] )
                # print(ip[i]['action']+"\t"+ip[i]['chain']+"\t"+ip[i]['src-address']+"\t"+ip[i]['dst-address']+"\t"+ip[i]['protocol']+ip[i]['src-port'+"\t"+ip[i]['dst-port']+"\t"+ip[i]['in-interface']+"\t"+ip[i]['out-interface']])
        return ip

    def addRule(self, chain="input"):
        """
        Method will add rule
        :param chain: input, forward,output
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/add', '=chain=' + chain] )
        return ip

    def removeRule(self, number):
        """
        Method will remove rule by rule number
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/remove', '=numbers=' + number] )
        return ip

    def enableRule(self, number):
        """
        Method will enable rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/enable', '=numbers=' + number] )
        return ip

    def disableRule(self, number):
        """
        Method will disable rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/disable', '=numbers=' + number] )
        return ip

    def commentRule(self, number, comment):
        """
        Method will comment rule
        :param number:
        :param comment:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/comment', '=numbers=' + number, '=comment=' + comment] )
        return ip

    def resetCounter(self, number):
        """
        Method will reset current counter
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/reset-counters', '=numbers=' + number] )
        return ip

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/reset-counters-all'] )
        return ip