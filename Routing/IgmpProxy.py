from tikapy import TikapyClient
from tikapy import TikapySslClient

class IgmpProxy:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listIgmpProxySettings(self):
        """
        Method will list proxy settings
        :return:
        """
        proxy = self.client.talk(['/routing/igmp-proxy/print'])
        if proxy == {}:
            print("no proxy enabled")
        else:
            print(proxy)
        return proxy

    def setQuickLeave(self):
        """
        Method will set quick leave
        :return:
        """
        proxy = self.client.talk(['/routing/igmp-proxy/set','=quick-leave=yes'])
        return proxy

    def unsetQuickLeave(self):
        """
        Method will set quick leave
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/set', '=quick-leave=no'] )
        return proxy

    def setQueryInterval(self,interval="00:02:05"):
        """
        Method will set query interval
        :param interval:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/set', '=query-interval='+interval] )
        return proxy

    def setQueryResponseInterval(self,interval="00:00:10"):
        """
        Method will set quewry interval
        :param interval:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/set', '=query-response-interval='+interval] )
        return proxy

    def listIgmpInterfaces(self):
        """
        Method will list interfaces of proxy
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/print'] )
        if proxy == {}:
            print("No proxy interface enabled")
        else:
            print("Interface\tThreshold\tAlternative subnets\tupstream")
            for i in proxy:
                #print(proxy)
                print(proxy[i]['interface']+"\t"+proxy[i]['threshold']+"\t"+proxy[i]['alternative-subnets']+"\t"+proxy[i]['upstream'])
        return proxy

    def removeProxyInterface(self,number):
        """
        Method will remove proxy
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/remove', '=numbers='+number] )
        return proxy

    def disableInterface(self,number):
        """
        Method will disable iface
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/disable', '=numbers='+number] )
        return proxy

    def enableInterface(self,number):
        """
        Method will enable interface
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/enable', '=numbers='+number] )
        return proxy

    def commentProxy(self,number,comment):
        """
        Method will comment proxy
        :param number:
        :param comment:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/set', '=numbers='+number,'=comment='+comment] )
        return proxy

    def setInterface(self,number,interface="all"):
        """
        Method will set proxy interface
        :param number:
        :param interface:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/set', '=numbers='+number,'=interface='+interface] )
        return proxy

    def setInterfaceThreshold(self,number,thres="1"):
        """
        Method will set threshold value
        :param number:
        :param thres:
        :return:
        """
        proxy = self.client.talk(['/routing/igmp-proxy/interface/set', '=numbers=' + number, '=threshold=' + thres] )
        return proxy

    def setAlternativeSubnet(self,number,subnet="0.0.0.0/0"):
        """
        Method will set alternative subnet
        :param number:
        :param subnet:
        :return:
        """
        proxy = self.client.talk(['/routing/igmp-proxy/interface/set', '=numbers=' + number, '=alternative-subnets='
                                  +subnet] )
        return proxy

    def setUpstream(self,number):
        """
        Method will enable upstream, there must be upstream interface to set it
        :param number:
        :return:
        """
        proxy = self.client.talk(['/routing/igmp-proxy/interface/set', '=numbers=' + number, '=upstream=yes'] )
        return proxy

    def unsetUpstream(self, number):
        """
        Method will enable upstream, there must be upstream interface to set it
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/interface/set', '=numbers=' + number, '=upstream=no'] )
        return proxy

    def listMfcGroups(self):
        """
        Methodwill list mfx groups
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/print'] )
        if proxy == {}:
            print("no group found")
        else:
            print("Group\tSource\tUpstream\tDownstream\tPackets")
            for i in proxy:
                #print(proxy)
                print(proxy[i]['group']+"\t"+proxy[i]['source']+"\t"+proxy[i]['upstream-interface']+"\t"+proxy[i]
                ['downstream-interfaces']+"\t"+proxy[i]['packets'])
        return proxy

    def removeMfcGroup(self,number):
        """
        Method will remove Mfc group
        :param number:
        :return:
        """
        proxy = self.client.talk(['/routing/igmp-proxy/mfc/remove','=numbers='+number])
        return proxy

    def disableMfcGroup(self,number):
        """
        Method will disable ifce group
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/disable', '=numbers=' + number] )
        return proxy

    def enableMfcGroup(self, number):
        """
        Method will disable ifce group
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/enable', '=numbers=' + number] )
        return proxy

    def setGroup(self,number,group):
        """
        Method will set group
        :param number:
        :param group:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/set', '=numbers=' + number,'=group='+group] )
        return proxy


    def setSourceGroup(self,number,address):
        """
        Method will set source address
        :param number:
        :param address:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/set', '=numbers=' + number, '=source=' + address] )
        return proxy

    def setUpstreamInterface(self,number,interface="ether1"):
        """
        Method will set upstream iface
        :param number:
        :param interface:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/set', '=numbers=' + number, '=upstream-interface='+interface] )
        return proxy

    def setDownstreamInterface(self,number,interface="ether1"):
        """
        Method will set downstream iface
        :param number:
        :param interface:
        :return:
        """
        proxy = self.client.talk( ['/routing/igmp-proxy/mfc/set', '=numbers=' + number, '=downstream-interfaces='+interface] )
        return proxy
