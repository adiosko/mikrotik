from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecPolicy:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)


    def listPolicies(self):
        """
        Method will list ipsec policies
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/print'])
        print("Src address\tsrc port\tDst address\t Dst port\tprotocol\taction\ttunnel")
        for i in ipsec:
            print(ipsec[i]['src-address']+"\t"+ipsec[i]['src-port']+"\t"+ipsec[i]['dst-address']+"\t"+ipsec[i]['dst-port']+"\t"+ipsec[i]['protocol']+"\t"+ipsec[i]['action']+"\t"+ipsec[i]['tunnel'])
        return ipsec

    def addPolicy(self,src,dst,srcsa):
        """
        Method will ad policy
        :param src: src LAN address
        :param dst: dst LAN address
        :param srcsa: src WAN address
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/add','=src-address='+src,'=dst-address='+dst,'=sa-src-address='+srcsa,'=tunnel=yes'])
        return ipsec

    def removePolicy(self,number):
        """
        Method will remove policy
        :param number:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/remove','=numbers='+number])
        return ipsec

    def enablePolicy(self,number):
        """
        Method will enable policy
        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/enable', '=numbers=' + number] )
        return ipsec

    def disablePolicy(self,number):
        """
        Method will disable policy
        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/disable', '=numbers=' + number] )
        return ipsec

    def commentPolicy(self,number,comment):
        """
        Method will comment policy
        :param number:
        :param comment:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/comment', '=numbers=' + number,'=comment='+comment] )
        return ipsec

    #General
    def setSrcAddress(self,number,src):
        """
        Method will set src address
        :param number:
        :param src:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=src-address=' + src] )
        return ipsec

    def setSrcPort(self,number,port):
        """
        Method will set src port
        :param number:
        :param port:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=src-port=' + port] )
        return ipsec

    def setDstAddress(self,number,dst):
        """
        Method will set tunnel dst address
        :param number:
        :param dst:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ipsec

    def setDstPort(self,number,port):
        """
        Method will set dst port
        :param number:
        :param port:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=dst-port=' + port] )
        return ipsec

    def setProtocol(self,number,protocol):
        """
        Method will set protocol
        :param number:
        :param protocol: all,ddp,egp,encap,etherip,ggp,gre,hmp,icmp,icmpv6,idpr-cmtp,igmp,ipencap,ipip,ipsec-ah,ipsec-eps,ipv6,ipv6-frag,ipv6-nonxt,ipv6-opts,ipv6-route,
        iso-tp4,l2tp,ospf,pim,pup,rdp,rspf,rsvp,st,tcp,udp,vmtp,vrrp,xns-idp,xtp
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=protocol=' + protocol] )
        return ipsec

    def setTemplate(self,number,group="default"):
        """
        Method will set template
        :param number:
        :param group:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=template=yes','=group=' + group] )
        return ipsec

    #Action
    def setAction(self,number,action="encrypt"):
        """
        Method will set action
        :param number:
        :param action: encrypt,discard,none
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=action=' + action] )
        return ipsec

    def setLevel(self,number,level="require"):
        """
        Method will set level of tunnel
        :param number:
        :param level:require, unique,use
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=level=' + level] )
        return ipsec

    def setIpsecProtocols(self,number,prot="esp"):
        """
        Method will set connection protocol
        :param number:
        :param prot: ah, esp, ah-esp
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=ipsec-protocols=' + prot] )
        return ipsec

    def setTunnel(self,number):
        """
        Method will set ipsec rule as tunnel
        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=tunnel=yes'] )
        return ipsec

    def setSaSrc(self,number,src):
        """
        Method will set sa src address
        :param number:
        :param src: public wan address oif source
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=sa-src-address=' + src] )
        return ipsec

    def setSaDst(self,number,dst):
        """
        Method will set dst
        :param number:
        :param dst:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=sa-dst-address=' + dst] )
        return ipsec

    def setProposal(self,number,proposal="default"):
        """
        Method will set proposal
        :param number:
        :param proposal:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=proposal=' + proposal] )
        return ipsec

    def setPriority(self,number,priority="0"):
        """
        Method will set priority
        :param number:
        :param priority:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/policy/set', '=numbers=' + number, '=priority='+priority] )
        return ipsec