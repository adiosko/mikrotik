from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallRaw:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRules(self):
        """
        Method will list all rules
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/raw/print'])
        if ipv6 == {}:
            print("No rule found,ssecure your router!!!")
        else:
            print("Action\tChain\tSrcAddress\tDstAddress\tProtocol\tSrcPort\tDstPort\tInInterface\tOutinterface")
            for i in ipv6:
                print(ipv6[i])
                #print(ipv6[i]['action']+"\t"+ipv6[i]['chain']+"\t"+ipv6[i]['src-address']+"\t"+ipv6[i]['dst-address']+"\t"+ipv6[i]['protocol']+ipv6[i]['src-port'+"\t"+ipv6[i]['dst-port']+"\t"+ipv6[i]['in-interface']+"\t"+ipv6[i]['out-interface']])
        return ipv6

    def addRule(self,chain="input"):
        """
        Method will add rule
        :param chain: input, forward,output
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/raw/add','=chain='+chain])
        return ipv6

    def removeRule(self,number):
        """
        Method will remove rule by rule number
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/raw/remove','=numbers='+number])
        return ipv6

    def enableRule(self,number):
        """
        Method will enable rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/enable', '=numbers=' + number] )
        return ipv6

    def disableRule(self,number):
        """
        Method will disable rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/disable', '=numbers=' + number] )
        return ipv6

    def commentRule(self,number,comment):
        """
        Method will comment rule
        :param number:
        :param comment:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv6

    def resetCounter(self,number):
        """
        Method will reset current counter
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/raw/reset-counters','=numbers='+number])
        return ipv6

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/raw/reset-counters-all'])
        return ipv6