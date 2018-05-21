from tikapy import TikapyClient
from tikapy import TikapySslClient

class bgpPeer:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPeers(self):
        """
        Mewthod will list peers
        :return:
        """
        peer = self.client.talk(['/routing/bgp/peer/print'])
        if peer == {}:
            print("No peer set")
        else:
            print("NAme\tInstance\tremote address\tremote as\tmultihop\troute-reflect\tttl\t""state")
            for i in peer:
                #print(peer)
                print(peer[i]['name']+"\t"+peer[i]['instance']+"\t"+peer[i]['remote-address']+"\t"+peer[i]['remote-as']+
                      "\t"+peer[i]['multihop']+"\t"+peer[i]['route-reflect']+"\t"+peer[i]['ttl']+"\t"+"\t"
                      +"\t"+"\t"+peer[i]['state'])
        return peer

    def addPeer(self,remAddress,remAS,instance):
        """
        Method wil ladd new peer
        :param remAddress:
        :param remAS:
        :return:
        """
        peer = self.client.talk(['/routing/bgp/peer/add','=remote-address='+remAddress,'=remote-as='+remAS,'=instance='
                                 +instance])
        return peer

    def removePeer(self,name):
        """
        Method will remove peer
        :param name:
        :return:
        """
        peer = self.client.talk(["/routing/bgp/peer/remove",'=numbers='+name])
        return peer

    def disablePeer(self,name):
        """
        Method will disable peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/disable", '=numbers=' + name] )
        return peer

    def enablePeer(self,name):
        """
        Method will enable peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/enable", '=numbers=' + name] )
        return peer

    def commentPeer(self,name,comment):
        """
        Method will comment peer
        :param name:
        :param comment:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/comment", '=numbers=' + name,'=comment='+comment] )
        return peer

    def refreshPeer(self,name):
        """
        Method will refresh single peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/refresh", '=numbers=' + name] )
        return peer

    def refreshPeers(self):
        """
        Method will refresh all peers
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/refresh-all"] )
        return peer

    def resendPeer(self,name):
        """
        Method will resend single peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/resend", '=numbers=' + name] )
        return peer

    def resendAll(self):
        """
        Method will resend all peers
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/resend-all"] )
        return peer

    def setPeerName(self,name,newNAme):
        """
        Method will rename peer
        :param name:
        :param newNAme:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=name='+newNAme] )
        return peer

    def setPeerInstance(self,name,instance):
        """
        Method will set peer instance
        :param name:
        :param instance: default,bgp,etc.
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=instance='+instance] )
        return peer

    def setPeerRemoteAddress(self,name,address):
        """
        Method will set peer remote addtess
        :param name:
        :param address:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=remote-address='+address] )
        return peer

    def setPeerPort(self,name,port):
        """
        Method will set port of remote address
        :param name:
        :param port:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=remote-port='+port] )
        return peer

    def setPeerRemoteAS(self,name,AS):
        """
        Method will set remote as
        :param name:
        :param AS:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=remote-as='+AS] )
        return peer

    def setPeerMD5Key(self,name,key):
        """
        Method will set md5 key
        :param name:
        :param key: key value
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=tcp-md5-key='+key] )
        return peer

    def setNextHopChoice(self,name,choice):
        """
        Method will set next hop choice
        :param name:
        :param choice: default, force-self,propagate
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=nexthop-choice='+choice] )
        return peer

    def enableMultihop(self,name):
        """
        Method will enable multihop
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=multihop=yes'] )
        return peer

    def enableROuteReflect(self,name):
        """
        Method will enable route reflect
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=route-reflect=yes'] )
        return peer

    def setHoldTime(self,name,hold="180"):
        """
        Method will set holdtime
        :param name:
        :param hold: 180s or infinity
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=hold-time='+hold] )
        return peer

    def setKeepAliveTime(self,name,time="0"):
        """
        Method will set keepalive time
        :param name:
        :param time: in secs
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=keepalive-time='+time] )
        return peer

    def setMAxPrefixLimit(self,name,prefix):
        """
        Method will set max prefix
        :param name:
        :param prefix:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=max-prefix-limit='+prefix] )
        return peer

    def setMaxPrefixRestartTime(self,name,time):
        """
        Method will set restart time of prefix
        :param name:
        :param time:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=max-prefix-restart-time='+time] )
        return peer

    def setInFilter(self,name,filter):
        """
        Method will set inpout filter
        :param name:
        :param filter: rip-in,rip-out,conencted-in,dynamic-in
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=in-filter='+filter] )
        return peer

    def setOutFilter(self,name,filter):
        """
        Method will set out filter
        :param name:
        :param filter:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=out-filter='+filter] )
        return peer

    def setAllowAS(self,name,AS="1"):
        """
        Method will set allowed AS
        :param name:
        :param AS:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=allow-as-in='+AS] )
        return peer

    def setRemoveASPrivate(self,name):
        """
        Method will remove private AS
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=remove-private-as=yes'] )
        return peer

    def unsetRemoveAsPrivate(self,name):
        """
        Method will unset AS private
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name,'=remove-private-as=no'] )
        return peer

    def setASOveride(self,name):
        """
        Method will set overiding AS
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=as-override=yes'] )
        return peer

    def unsetAsOveride(self,name):
        """
        Method wll unset as override
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=as-override=no'] )
        return peer

    def setDefaultOriginate(self,name,origin="never"):
        """
        Method will set originate
        :param name:
        :param origin: never, always, if-installed
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=default-originate='+origin] )
        return peer

    def setPassive(self,name):
        """
        Method will set passive peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=passive=yes'] )
        return peer

    def unsetPassive(self, name):
        """
        Method will set passive peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=passive=no'] )
        return peer

    def setUSeBFD(self, name):
        """
        Method will set passive peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=use-bfd=yes'] )
        return peer

    def unsetUSeBFD(self, name):
        """
        Method will set passive peer
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=use-bfd=no'] )
        return peer

    def setIPAddressFamily(self,name):
        """
        Method will set IP as addess family
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=address-families=ip'] )
        return peer

    def setIPv6AddressFamily(self, name):
        """
        Method will set IP as addess family
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=address-families=ipv6'] )
        return peer

    def setl2vpn(self,name):
        """
        Method will set l2vpn
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=address-families=l2vpn'] )
        return peer

    def setVpn4(self,name):
        """
        Method will set vpn4
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=address-families=vpnv4'] )
        return peer

    def setCiscoL2vp(self,name):
        """
        Method will set l2vpn from cisco
        :param name:
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=address-families=l2vpn-cisco'] )
        return peer

    def setUpdateSource(self,name,interface):
        """
        Method will set source inerface
        :param name:
        :param interface: none or interface
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=update-source='+interface] )
        return peer

    def setCiscoVPLSLength(self,name,length="auto-bits"):
        """
        Method will set cisco vpls length
        :param name:
        :param length:  auto-bites, auto-bytes, bites, bytes
        :return:
        """
        peer = self.client.talk( ["/routing/bgp/peer/set", '=numbers=' + name, '=cisco-vpls-nlri-len-fmt='+length] )
        return peer