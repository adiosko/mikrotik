from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallMangle:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
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

    def addinputaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=input','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=in-interface='+interface])
        return ip

    def addinputreject(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=input','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=in-interface='+interface])
        return ip

    def addinputdeny(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=input','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=in-interface='+interface])
        return ip

    def addForwardaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=forward','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addForwardreject(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=forward','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addForwarddeny(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=forward','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addOutputaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=output','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addOutputreject(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=output','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addOutputdeny(self,dst=None,src=None,protocol=None,sport=None,dport=None,interface=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=output','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport,'=out-interface='+interface])
        return ip

    def addPostroutingaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=postrouting','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport])
        return ip

    def addPostroutingreject(self,dst=None,src=None,protocol=None,sport=None,dport=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=postrouting','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport])
        return ip

    def addPostroutingdeny(self,dst=None,src=None,protocol=None,sport=None,dport=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=postrouting','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport])
        return ip

    def addPreroutingaccept(self,dst=None,src=None,protocol=None,sport=None,dport=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=prerouting','=action=accept','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport])
        return ip

    def addPreroutingreject(self,dst=None,src=None,protocol=None,sport=None,dport=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=prerouting','=action=reject','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport])
        return ip

    def addPreroutingdeny(self,dst=None,src=None,protocol=None,sport=None,dport=None):
        ip = self.client.talk(['/ip/firewall/mangle/add','=chain=prerouting','=action=drop','=src-address='+src,'=dst-address='+dst,'=protocol='+protocol,'=src-port='+sport,'=dst-port='+dport])
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