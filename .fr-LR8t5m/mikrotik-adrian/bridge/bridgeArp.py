from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeNatArp:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setArpOpcode(self,number,oper="0()"):
        """
        Method will set arp operation code
        :param number:
        :param oper: 0(),arp-nak,drarp-error,drarp-reply,drarp-request,inarp-reply,unarp-request,reply,reply-reverse,request,request-reverse
        :return:
        """
        arp = self.client.talk(['/interface/bridge/nat/set','=numbers='+number,'=arp-opcode='+oper])
        return arp

    def setArpHadrwareType(self,number,hw="0"):
        """
        Method will set arp hw type
        :param number:
        :param hw:
        :return:
        """
        arp = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=arp-hardware-type=' + hw] )
        return arp

    def setArpPacketType(self, number, pkt="0"):
        """
        Method will set arp hw type
        :param number:
        :param pkt:
        :return:
        """
        arp = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=arp-packet-type=' + pkt] )
        return arp

    def setArpSrcAddr(self, number, src):
        """
        Method will set arp hw type
        :param number:
        :param src:
        :return:
        """
        arp = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=arp-src-address=' + src] )
        return arp

    def setArpSrcmAcAdress(self, number,src,mask):
        """
        Method will set arp hw type
        :param number:
        :param src:
        :return:
        """
        arp = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=arp-src-mac-address=' + src+"/"+mask] )
        return arp

    def setArpDstmAcAdress(self, number, dst, mask):
        """
        Method will set arp hw type
        :param number:
        :param dst:
        :return:
        """
        arp = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=arp-dst-mac-address=' + dst + "/" + mask] )
        return arp

    def setArpGratitinuous(self, number,arp="none"):
        """
        Method will set arp hw type
        :param number:
        :param arp: none,no,yes
        :return:
        """
        arp = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=arp-gratuitous=' + arp] )
        return arp





