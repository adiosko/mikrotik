from tikapy import TikapyClient
from tikapy import TikapySslClient

class bondingSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setSlaves(self,name,slaveInterface):
        """

        :param name:
        :param slaveInterface:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set','=numbers='+name,'=slaves='+slaveInterface])
        return iface

    def setMode(self,name,mode="balance-rr"):
        """

        :param name:
        :param mode: 802.3ad,active-backup,balance-alb,balance-rr,balance-tlb,balance-xor,broadcast
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=mode=' + mode])
        return iface

    def setLinkMonitoring(self,name,link="mii"):
        """

        :param name:
        :param link:mii,arp,none
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=link-monitoring=' + link])
        return iface

    def setTransmitHashPolicy(self,name,policy="layer-2"):
        """

        :param name:
        :param policy: layer-2,layer-2-and-3,layer3-and-4
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=transmit-hash-policy=' + policy])
        return iface

    def setMinLinks(self,name,minimum="0"):
        """

        :param name:
        :param minimum:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=min-links=' + minimum])
        return iface

    def setDOwnDelay(self,name,delay="0"):
        """

        :param name:
        :param delay: in ms
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=down-delay=' + delay])
        return iface

    def setUpDelay(self,name,delay="0"):
        """

        :param name:
        :param delay:
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=up-delay=' + delay])
        return iface

    def setLacpRate(self,name,lacp="30s"):
        """

        :param name:
        :param lacp:30s,1s
        :return:
        """
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=lacp-rate=' + lacp])
        return iface

    def setMiiInterval(self,name,interval="100"):
        """

        :param name:
        :param interval:
        :return:
        """
        self.setMode(name,"mii")
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=mii-interval=' + interval])
        return iface

    def setArpInterval(self,name,inerval="100"):
        """

        :param name:
        :param inerval:
        :return:
        """
        self.setMode(name,"arp")
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=arp-interval=' + inerval])
        return iface

    def setArpTargets(self,name,targets):
        """

        :param name:
        :param targets: IPs
        :return:
        """
        self.setMode(name,"arp")
        iface = self.client.talk(['/interface/bonding/set', '=numbers=' + name, '=arp-ip-targets=' + targets])
        return iface