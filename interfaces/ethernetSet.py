from tikapy import TikapyClient
from tikapy import TikapySslClient


class ethernetSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def enableAutoNegotiation(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/ethernet/set','=numbers='+name,'=auto-negotiation=yes'])
        return iface

    def disableAutoNegotiation(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=auto-negotiation=no'] )
        return iface

    def setTxFlow(self,name,txFlow="off"):
        """

        :param name:
        :param txFlow:off,on,auto
        :return:
        """
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=tx-flow-control='+txFlow] )
        return iface

    def setRxFlowControl(self,name,rxFlow="off"):
        """

        :param name:
        :param rxFlow: off, on, auto
        :return:
        """
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=rx-flow-control='+rxFlow] )
        return iface

    def setAdvertiseSpeed(self,name,speed="10M-full,10M-half,100M-full,100M-half,1000M-full,1000M-half"):
        """

        :param name:
        :param speed: 10M-full,10M-half,100M-full,100M-half,1000M-full,1000M-half
        :return:
        """
        self.enableAutoNegotiation(name)
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=advertise=' + speed] )
        return iface

    def setSpeed(self,name,speed="100Mbps"):
        """

        :param name:
        :param speed:1Gbps,10Gbps,10Mbps,100Mbps
        :return:
        """
        self.disableAutoNegotiation(name)
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=speed=' + speed] )
        return iface

    def enableFullDuplex(self,name):
        """

        :param name:
        :return:
        """
        self.disableAutoNegotiation(name)
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=full-duplex=yes'] )
        return iface

    def disableFullDuplex(self,name):
        """

        :param name:
        :return:
        """
        self.disableAutoNegotiation(name)
        iface = self.client.talk( ['/interface/ethernet/set', '=numbers=' + name, '=full-duplex=no'] )
        return iface