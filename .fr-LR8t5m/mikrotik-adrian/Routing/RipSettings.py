from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipSettings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setDefaultDistribution(self,distribution="never"):
        """
        Method will set default redistribution
        :param distribution: never, always, if-installed
        :return:
        """
        rip = self.client.talk(['/routing/rip/set','=distribute-default='+distribution])
        return rip

    def redistributeStaticRoutes(self):
        """
        Method will redistribute static routes
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=redistribute-static=yes'] )
        return rip

    def redistributeConnectedRoutes(self):
        """
        Method will redistribute connected networks
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=redistribute-connected=yes'] )
        return rip

    def redistributeOspf(self):
        """
        Method will redistribute ospf
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=redistribute-ospf=yes'] )
        return rip

    def redistributeBgp(self):
        """
        Method will redistribute bgp routes
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=redistribute-bgp=yes'] )
        return rip

    def setDefaultMetric(self,metric="1"):
        """
        Method will set default emtric
        :param metric:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=metric-default='+metric] )
        return rip

    def setStaticRoutesMetric(self, metric="1"):
        """
        Method will set default emtric
        :param metric:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=metric-static=' + metric] )
        return rip

    def setConnectedNetworksMetric(self, metric="1"):
        """
        Method will set default emtric
        :param metric:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=metric-connected=' + metric] )
        return rip

    def setOspfMetric(self, metric="1"):
        """
        Method will set default emtric
        :param metric:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=metric-ospf=' + metric] )
        return rip

    def setBgpMetric(self, metric="1"):
        """
        Method will set default emtric
        :param metric:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=metric-bgp=' + metric] )
        return rip

    def setUpdateTimer(self,timer="00:00:30"):
        """
        Method will set rip update timer
        :param timer:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=update-timer=' + timer] )
        return rip

    def setTimeOutTimer(self,timer="00:03:00"):
        """
        Method will set timeout timer
        :param timer:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=timeout-timer=' + timer] )
        return rip

    def setGarbageTimer(self,timer="00:02:00"):
        """
        Method will set garbage timer
        :param timer:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=garbage-timer=' + timer] )
        return rip

    def setRoutingTable(self,table="main"):
        """
        Method will set routing table
        :param table: main, or custom routing table
        :return:
        """
        rip = self.client.talk( ['/routing/rip/set', '=routing-table=' + table] )
        return rip


