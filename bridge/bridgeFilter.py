from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgefilter:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listfilter(self):
        """
        Method will list filter rules
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/print'] )
        print( "Action\tChain" )
        for i in filter:
            print( filter[i]['action'] + "\t" + filter[i]['chain'] )
        return filter

    def addfilter(self, chain, action):
        """
        Method will add filter
        :param chain: srcfilter,dstfilter
        :param action: accept,arp-only,drop,dst-filter,jump,log,mark-packet,pastshrough,redirect,return,set-priority,src-filter
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/add', '=chain=' + chain, '=action=' + action] )
        return filter

    def removefilter(self, number):
        """
        Methdo will remove filter
        :param number:
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/remove', '=numbers=' + number] )
        return filter

    def enablefilter(self, number):
        """
    
        :param number:
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/enable', '=numbers=' + number] )
        return filter

    def disablefilter(self, number):
        """
    
        :param number:
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/disable', '=numbers=' + number] )
        return filter

    def commentfilter(self, number, comment):
        """
    
        :param number:
        :param comment:
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/comment', '=numbers=' + number, '=comment=' + comment] )
        return filter

    def resetCounters(self, number):
        """
        Method will reset single counters
        :param number:
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/reset-counters', '=numbers=' + number] )
        return filter

    def resetAllCOunters(self):
        """
        Method will reset all counters
        :return:
        """
        filter = self.client.talk( ['/interface/bridge/filter/reset-counters-all'] )
        return filter