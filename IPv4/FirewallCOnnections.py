from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallConnections:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listConnections(self):
        """
        Method will list all connections
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/print'] )
        return ip

    def setTrackingMode(self,mode="yes"):
        """
        Method will set tracking
        :param mode:  auto,no,yes
        :return:
        """
        ip = self.client.talk(['/ip/firewall/connection/tracking/set','=enabled=yes'])
        return ip

    def setTcpSynSendTimeout(self, timeout="00:00:05"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-syn-sent-timeout=' + timeout] )
        return ip

    def setTcpSynRcvTimeout(self, timeout="00:00:05"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-syn-received-timeout=' + timeout] )
        return ip

    def setTcpEstablishedTimeout(self, timeout="1d 00:00:00"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-established-timeout=' + timeout] )
        return ip

    def setTcpFinWaitTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-fin-wait-timeout=' + timeout] )
        return ip

    def setTcpCloseWaitTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-close-wait-timeout=' + timeout] )
        return ip

    def setTcpLastAckTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-last-ack-timeout=' + timeout] )
        return ip

    def setTcpTimeWaitTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-time-wait-timeout=' + timeout] )
        return ip

    def setTcpCloseTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-close-timeout=' + timeout] )
        return ip

    def setTcpMaxRetransmitTimeout(self, timeout="00:05:00"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-max-retrans-timeout=' + timeout] )
        return ip

    def setTcpUnackedTimeout(self, timeout="00:05:00"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=tcp-unacked-timeout=' + timeout] )
        return ip

    def setUdpTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=udp-timeout=' + timeout] )
        return ip

    def setUdpStreamTimeout(self, timeout="00:03:00"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=udp-stream-timeout=' + timeout] )
        return ip

    def setIcmpTimeout(self, timeout="00:00:10"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=icmp-timeout=' + timeout] )
        return ip

    def setGenericTimeout(self, timeout="00:10:00"):
        """
        Method will tcp timeout
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/connection/tracking/set', '=generic-timeout=' + timeout] )
        return ip