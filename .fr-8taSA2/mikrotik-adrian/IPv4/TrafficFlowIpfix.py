from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficFlowIpfix:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setLastForwarded(self):
        """
        Method will set last forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=last-forwarded=yes'] )
        return ipfix

    def setFirstForwarded(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=first-forwarded=yes'] )
        return ipfix

    def setInInterface(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=in-interface=yes'] )
        return ipfix

    def setOutInterface(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=out-interface=yes'] )
        return ipfix

    def setSrcPort(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=src-port=yes'] )
        return ipfix

    def setDstPort(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=dst-port=yes'] )
        return ipfix

    def setGateway(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=gateway=yes'] )
        return ipfix

    def setSrcAddressMask(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=src-address-mask=yes'] )
        return ipfix

    def setDstMac(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=dst-mac-address=yes'] )
        return ipfix

    def setSrcMac(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=src-mac-address=yes'] )
        return ipfix

    def setNatSrcPort(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=nat-src-port=yes'] )
        return ipfix

    def setNatDstPort(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=nat-dst-port=yes'] )
        return ipfix

    def setIsMulticast(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=is-multicast=yes'] )
        return ipfix

    def setIpHeaderLength(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=ip-header-length=yes'] )
        return ipfix

    def setTcpSeqNumber(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=tcp-seq-num=yes'] )
        return ipfix

    def setAckNumber(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=tcp-ack-number=yes'] )
        return ipfix

    def setIcmpType(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=icmp-type=yes'] )
        return ipfix

    def setIcmpCode(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=icmp-code=yes'] )
        return ipfix

    def setPackets(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=packets=yes'] )
        return ipfix

    def setBytes(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=bytes=yes'] )
        return ipfix

    def setSrcAddress(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=src-address=yes'] )
        return ipfix

    def setDstAddress(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=dst-address=yes'] )
        return ipfix

    def setProtocol(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=protocol=yes'] )
        return ipfix

    def setIpTos(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=tos=yes'] )
        return ipfix

    def setDstAddressMask(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=dst-address-mask=yes'] )
        return ipfix

    def setTcpFlags(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=tcp-flags=yes'] )
        return ipfix

    def setNatSrcAddress(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=nat-src-address=yes'] )
        return ipfix

    def setNatDstAddress(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=nat-dst-address=yes'] )
        return ipfix

    def setIpv6FlowLabel(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=ipv6-flow-label=yes'] )
        return ipfix

    def setTtl(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=ttl=yes'] )
        return ipfix

    def setIpTotalLength(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=ip-total-length=yes'] )
        return ipfix

    def setUdpLength(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=udp-length=yes'] )
        return ipfix

    def setTcpWindowSize(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=tcp-window-size=yes'] )
        return ipfix

    def setIgmpType(self):
        """
        Method will set first forwarded
        :return:
        """
        ipfix = self.client.talk( ['/ip/traffic-flow/ipfix/set', '=igmp-type=yes'] )
        return ipfix