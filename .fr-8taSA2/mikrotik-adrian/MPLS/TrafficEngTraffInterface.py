from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficEngTraffInterface:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterface(self):
        """
        Methodwill list interface for traffici\engineering
        :return:
        """
        mpls = self.client.talk(['/interface/traffic-eng/print'])
        if mpls == {}:
            print("No interface found")
        else:
            print("Name\tMTU")
            for i in mpls:
                print(mpls[i]['name']+"\t"+mpls[i]['mtu'])
        return mpls

    def addInterface(self):
        """
        Method will add te interface
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/add','=disabled=no'] )
        return mpls

    def removeInterface(self,name):
        """
        Method will remove interface
        :param name: name of interface
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/remove','=numbers='+name] )
        return mpls

    def enableInterface(self,name):
        """
        Methodwill enable interface
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/enable', '=numbers=' + name] )
        return mpls

    def disableInterface(self, name):
        """
        Methodwill enable interface
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/disable', '=numbers=' + name] )
        return mpls

    def commentInterface(self,name,comment):
        """
        Method will comment iface
        :param name:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/comment', '=numbers=' + name,'=comment='+comment] )
        return mpls

    #general
    def setName(self,name,newName):
        """
        Method will set new name
        :param name:
        :param newName:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=name=' + newName] )
        return mpls

    def setMtu(self,name,mtu="1500"):
        """
        Method will set new mtu
        :param name:
        :param mtu:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=mtu=' + mtu] )
        return mpls

    def setToAddress(self,name,address):
        """
        Method will set interface to address
        :param name:
        :param address: <IP>
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=to-address=' + address] )
        return mpls

    def setBandwidth(self,name,bw="0"):
        """
        Method will set bw
        :param name:
        :param bw:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=bandwidth=' + bw] )
        return mpls

    def setPrimaryPath(self,name,path):
        """
        Method will set primary path
        :param name:
        :param path: created from TunnelPath
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=primary-path=' + path] )
        return mpls

    def setSecondaryPaths(self,name,path):
        """
        Method will set secondary paths created in Tunnel Path
        :param name:
        :param path:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=secondary-paths=' + path] )
        return mpls

    #TE
    def setPrimaryRetryInterval(self,name,interval="00:01:00"):
        """
        Method will set new retry interval
        :param name:
        :param interval:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=primary-retry-interval=' + interval] )
        return mpls

    def setPriority(self,name,priority="0"):
        """
        Method will set priority
        :param name:
        :param priority:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=setup-priority=' + priority] )
        return mpls

    def setHoldingPriority(self,name,priority="0"):
        """
        Method will set hold priority
        :param name:
        :param interval:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=holding-priority=' + priority] )
        return mpls

    def recordRoute(self,name):
        """
        Method will record route
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name,'record-route=yes'] )
        return mpls

    def setAffinityIncludeAll(self,name,incl="0"):
        """
        Method will set affinity all
        :param name:
        :param incl:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=affinity-include-all=' + incl] )
        return mpls

    def setAffinityIncludeAny(self,name,incl="0"):
        """
        Method will include any affinity
        :param name:
        :param incl:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=affinity-include-any=' + incl] )
        return mpls

    def setExcludeAffinity(self,name,excl="0"):
        """
        Method will set affinity
        :param name:
        :param excl:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=affinity-exclude=' + excl] )
        return mpls

    def setReoptimizeInterval(self,name,interval="00:00:00"):
        """
        Method will reoptimize interval
        :param name:
        :param interval:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=reoptimize-interval=' + interval] )
        return mpls

    #BW
    def setBwLimit(self,name,limit="0"):
        """
        Method will limit bw
        :param name:
        :param limit: in %
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=bandwidth-limit=' + limit] )
        return mpls

    def setAutoBandwidthRange(self,name,rng="0-0"):
        """
        Method will set range for bw
        :param name:
        :param rng: disabled-number,number-number
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=auto-bandwidth-range=' + rng] )
        return mpls

    def setAutoBwReserve(self,name,reserve="0"):
        """
        Method will set bw reserve %
        :param name:
        :param reserve:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=auto-bandwidth-reserve=' + reserve] )
        return mpls

    def setAutoBwAvgInterval(self,name,interval="00:05:00"):
        """
        Method will set avg bw interval
        :param name:
        :param interval:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=auto-bandwidth-avg-interval=' + interval] )
        return mpls

    def setAutoBwUpdateInterval(self,name,interval="01:00:00"):
        """
        Method will set update interval
        :param name:
        :param interval:
        :return:
        """
        mpls = self.client.talk( ['/interface/traffic-eng/set', '=numbers=' + name, '=auto-bandwidth-update-interval=' + interval] )
        return mpls