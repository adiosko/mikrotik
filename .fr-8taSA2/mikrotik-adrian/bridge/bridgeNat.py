from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeNat:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNat(self):
        """
        Method will list nat rules
        :return:
        """
        nat = self.client.talk(['/interface/bridge/nat/print'])
        print("Action\tChain")
        for i in nat:
            print(nat[i]['action']+"\t"+nat[i]['chain'])
        return nat

    def addNat(self,chain,action):
        """
        Method will add nat
        :param chain: srcnat,dstnat
        :param action: accept,arp-only,drop,dst-nat,jump,log,mark-packet,pastshrough,redirect,return,set-priority,src-nat
        :return:
        """
        nat = self.client.talk(['/interface/bridge/nat/add','=chain='+chain,'=action='+action])
        return nat

    def removeNat(self,number):
        """
        Methdo will remove nat
        :param number:
        :return:
        """
        nat = self.client.talk(['/interface/bridge/nat/remove','=numbers='+number])
        return nat

    def enableNat(self,number):
        """

        :param number:
        :return:
        """
        nat = self.client.talk( ['/interface/bridge/nat/enable', '=numbers=' + number] )
        return nat

    def disableNat(self,number):
        """

        :param number:
        :return:
        """
        nat = self.client.talk( ['/interface/bridge/nat/disable', '=numbers=' + number] )
        return nat

    def commentNat(self,number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        nat = self.client.talk( ['/interface/bridge/nat/comment', '=numbers=' + number,'=comment='+comment] )
        return nat

    def resetCounters(self,number):
        """
        Method will reset single counters
        :param number:
        :return:
        """
        nat = self.client.talk( ['/interface/bridge/nat/reset-counters', '=numbers=' + number] )
        return nat

    def resetAllCOunters(self):
        """
        Method will reset all counters
        :return:
        """
        nat = self.client.talk( ['/interface/bridge/nat/reset-counters-all'] )
        return nat