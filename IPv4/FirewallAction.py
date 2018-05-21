from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallActions:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setAcceptFilter(self,number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=action=accept'])
        return ip

    def setFilterLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number,'=log=yes'] )
        return ip

    def setFilterLogPrefix(self, number,prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number,'=log-prefix='+prefix] )
        return ip

    def setAcceptMangle(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=accept'] )
        return ip

    def setMangleFilterLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=log=yes'] )
        return ip

    def setMangleFilterLogPrefix(self, number, prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=log-prefix=' + prefix] )
        return ip

    def setAcceptnat(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=action=accept'] )
        return ip

    def setnatLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=log=yes'] )
        return ip

    def setnatLogPrefix(self, number, prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=log-prefix=' + prefix] )
        return ip

    def addToDstAddressListFilter(self,number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=action=add-dst-to-address-list'] )
        return ip

    def setAddressListFilter(self,number,addr):
        """
        Method will set address list
        :param number:
        :param addr: address lst t oadd
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set', '=numbers=' + number, '=address-list='+addr] )
        return ip

    def setAddressListTimeoutFilter(self,number,timeout):
        """
        Method will set address list timeout
        :param number:
        :param timeout:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=address-list-timeout=' + timeout] )
        return ip

    def addToDstAddressListMangle(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=add-dst-to-address-list'] )
        return ip

    def setAddressListMangle(self, number, addr):
        """
        Method will set address list
        :param number:
        :param addr: address lst t oadd
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=address-list=' + addr] )
        return ip

    def setAddressListTimeoutMangle(self, number, timeout):
        """
        Method will set address list timeout
        :param number:
        :param timeout:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=address-list-timeout=' + timeout] )
        return ip

    def addToDstAddressListnat(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=action=add-dst-to-address-list'] )
        return ip

    def setAddressListnat(self, number, addr):
        """
        Method will set address list
        :param number:
        :param addr: address lst t oadd
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=address-list=' + addr] )
        return ip

    def setAddressListTimeoutnat(self, number, timeout):
        """
        Method will set address list timeout
        :param number:
        :param timeout:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=address-list-timeout=' + timeout] )
        return ip

    def addToSrcAddressListFilter(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/filter/set', '=numbers=' + number, '=action=add-src-to-address-list'] )
        return ip

    def addToSrcAddressListMangle(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=add-src-to-address-list'] )
        return ip

    def addToSrcAddressListnat(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=action=add-src-to-address-list'] )
        return ip

    def setDscpActionMangle(self,number):
        """
        Method wil lset  mangle action
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=change-dscp'])
        return ip

    def setDscpAValue(self, number,balue="0"):
        """
        Method wil lset  mangle action
        :param number:
        :param balue: value of param
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=new-dscp='+balue] )
        return ip

    def setPasthroughMangle(self,number):
        """
        Method will set passthrough
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=passthrough=yes'] )
        return ip

    def setMssActionMangle(self,number):
        """
        Method will allow mss action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=change-mss'] )
        return ip

    def setMssValueMangle(self,number,value="0"):
        """
        Method will set mss value
        :param number:
        :param value: for tcp syn set value or clamp-to-pmtu
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=new-mss=' + value] )
        return ip

    def setTtlValueMangle(self,number,action="change-ttl"):
        """
        Method will set action for ttl
        :param number:
        :param action:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'action='+action])
        return ip

    def setNewTtlMangle(self,number,ttl="0"):
        """
        Method will set ttl
        :param number:
        :param ttl:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=new-ttl='+ttl])
        return ip

    def setClearDf(self,number):
        """
        Method will clear df
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=clear-df'])
        return ip

    def setFasttrackConnectionMangle(self,number):
        """
        Method will set fast track connection
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=fastrack-connection'])
        return ip

    def setFasttrackConnectionFilter(self, number):
        """
        Method will set fast track connection
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=action=fastrack-connection'] )
        return ip

    def setDstNatNat(self,number):
        """
        Method wil lset ds tnat
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=action=dst-nat'])
        return ip

    def setDstNatAddressNat(self, number,address):
        """
        Method wil lset ds tnat
        :param number:
        :param address: address to translate
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=to-addresses='+address] )
        return ip

    def setDstNatPortNat(self, number, port):
        """
        Method wil lset ds tnat
        :param number:
        :param port: port to translate
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=to-ports=' + port] )
        return ip

    def setJumpActionFilter(self,number,target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=action=jump','=jump-target='+target] )
        return ip

    def setJumpActionMangle(self, number, target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=jump', '=jump-target=' + target] )
        return ip

    def setJumpActionnat(self, number, target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=action=jump', '=jump-target=' + target] )
        return ip

    def setActionLogFilter(self,number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/filter/set', '=numbers=' + number, '=action=log'] )
        return ip

    def setActionLogMangle(self, number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=log'] )
        return ip

    def setActionLognat(self, number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=action=log'] )
        return ip

    def setMasquaradeNat(self,number):
        """
        Method will set masquarade action for src nat
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=action=masquerade'])
        return ip

    def setNetmapNat(self,number):
        """
        Method will set action netmap
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=action=netmap'])
        return ip

    def setMarkCOnenctionMangle(self,number):
        """
        Method will mark connection
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=mark-connection'] )
        return ip

    def setMarkConnectionValueMangle(self,number,val="no-mark"):
        """
        Method will set value
        :param number:
        :param val: no-mark or specific value
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=new-connection-mark=' + val] )
        return ip

    def setMarkPacketMangle(self, number):
        """
        Method will mark connection
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=mark-packet'] )
        return ip

    def setMarkPacketValueMangle(self, number, val="no-mark"):
        """
        Method will set value
        :param number:
        :param val: no-mark or specific value
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=new-packet-mark=' + val] )
        return ip

    def setMarkRouting(self,number):
        """
        Method will routing mark
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=action=mark-routing'])
        return ip

    def setNewRoutingmark(self,number,mark="main"):
        """
        Method will set new routing mark
        :param number:
        :param mark:
        :return:
        """
        ip =self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=new-routing-mark='+mark])
        return ip

    def setPassthroughActionFilter(self,number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/filter/set', '=numbers=' + number, '=action=passthrough'] )
        return ip

    def setPassthroughActionMangle(self, number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=passthrough'] )
        return ip

    def setPassthroughActionnat(self, number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=action=passthrough'] )
        return ip

    def setRejectActionFIlter(self,number):
        """
        Method will
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=action=reject'])
        return ip

    def setRejectMessageFilter(self,number,message="icmp-no-route"):
        """
        Method will set reject message
        :param number:
        :param message: icmp-address-unreachable,icmp-admin-prohibited,icmp-no-route,icmp-no-neighbor,icmp-port-unreachable,icmp-reset
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=reject-with='+message])
        return ip

    def setRedirectNat(self,number):
        """
        Method will redirect rule to port
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=action=redirect'])
        return ip

    def setActionReturnFilter(self,number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=action=return'] )
        return ip

    def setActionReturnMangle(self, number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=action=return'] )
        return ip

    def setActionReturnnat(self, number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=action=return'] )
        return ip

    def setTarpitFilter(self,number):
        """
        Method will set tarpit action
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'action=tarpit'])
        return ip

    def setSameNat(self,number):
        """
        Method will set same action
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=action=same'])
        return ip

    def setSrcNatNat(self,number):
        """
        Methodwill set src nat
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/nat/set','=numbers='+number,'=action=src-nat'])
        return ip

    def setRouteActionMangle(self,number):
        """
        Method will se tmangle action
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=route'])
        return ip

    def setDstAddressMangle(self,number,address):
        """
        Method will set route address
        :param number:
        :param address:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=route-dst='+address])
        return ip

    def setPriorityActionMangle(self,number):
        """
        Method will set action priority
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=set-priority'])
        return ip

    def setPriorityMangle(self,number,priority):
        """
        Method will set priority
        :param number:
        :param priority:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=new-priority='+priority])
        return ip

    def setSniffPcActionMAngle(self,number):
        """
        Method will sniff pc
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=sniff-pc'])
        return ip

    def setSniffTargetMangle(self,number,tgt):
        """
        Method will set sniffing target
        :param number:
        :param tgt:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=sniff-target='+tgt])
        return ip

    def setSniffTargetPortMangle(self,number,port):
        """
        Method will set sniff target port
        :param number:
        :param port:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=sniff-target-port=' + port] )
        return ip

    def setSniffIdMangle(self,numbre,ID):
        """
        Method will set sniff id
        :param numbre:
        :param ID:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + numbre, '=sniff-id=' + ID] )
        return ip

    def setSniffTZSPActionMangle(self,number):
        """
        Method will set TZSP action
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=sniff-tzsp'])
        return ip

    def setStripIpOptionMangle(self,number):
        """
        Method will strip ipv4 options
        :param number:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/mangle/set','=numbers='+number,'=action=strip-ipv4-options'])
        return ip