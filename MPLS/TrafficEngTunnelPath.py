from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficEngTunnelPath:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPaths(self):
        """
        Method will list all paths
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/tunnel-path/print'])
        if mpls == {}:
            print("No entry found")
        else:
            print("Name\tuse cspf\thops")
            for i in mpls:
                print(mpls[i]['name']+"\t"+mpls[i]['use-cspf']+"\t"+mpls[i]['hops'])
        return mpls

    def addPath(self,name):
        """
        Method will add new parh
        :param name: name of path
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/add','=name='+name] )
        return mpls

    def removePath(self,name):
        """
        Method will remove path
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/remove','=numbers='+name] )
        return mpls

    def enablePath(self,name):
        """
        Method will enable path
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/enable','=numbers='+name] )
        return mpls

    def disablePath(self,name):
        """
        Method willdisable path
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/disable','=numbers='+name] )
        return mpls

    def setName(self,name,newName):
        """
        Methodwill rename parh
        :param name:
        :param newName:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/set','=numbers='+name,'=name='+newName] )
        return mpls

    def useCSPF(self,name):
        """
        Method will use cspf
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/set','=numbers='+name,'=use-cspf=yes'] )
        return mpls

    def setPriority(self,name,priority="0"):
        """
        Method will set priority
        :param name:
        :param priority:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=setup-priority='+priority] )
        return mpls

    def setHoldingPriority(self,name,priority="0"):
        """
        Method will set holding priotity
        :param name:
        :param priority:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=holding-priority='+priority] )
        return mpls

    def recordRoute(self,name):
        """
        Method will record route
        :param name:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=record-route=yes'] )
        return mpls

    def setAffinityIncludeAll(self,name,incl="0"):
        """
        Method will set affinity all
        :param name:
        :param incl:
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=affinity-include-all='+incl] )
        return mpls

    def setAffinityIncludeAny(self,name,incl="0"):
        """
        Method will set affinity
        :param name:
        :param incl:
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=affinity-include-any=' + incl] )
        return mpls

    def setAffinityExclude(self,name,excl="0"):
        """
        Method will exclude affinity
        :param name:
        :param excl:
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=affinity-exclude=' + excl] )
        return mpls

    def setHops(self,name,hop="0.0.0.0/:loose"):
        """
        Method will set all hops
        :param name:
        :param hop: IP/loose/strict
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/tunnel-path/set', '=numbers=' + name, '=hops='+hop] )
        return mpls