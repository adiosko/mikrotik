from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallActions:
    def __init__(self,address,username,password):
        sself.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setAcceptFilter(self,number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set','=numbers='+number,'=action=accept'])
        return ipv6

    def setFilterLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number,'=log=yes'] )
        return ipv6

    def setFilterLogPrefix(self, number,prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number,'=log-prefix='+prefix] )
        return ipv6

    def setAcceptMangle(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=accept'] )
        return ipv6

    def setMangleFilterLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=log=yes'] )
        return ipv6

    def setMangleFilterLogPrefix(self, number, prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=log-prefix=' + prefix] )
        return ipv6

    def setAcceptRaw(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=accept'] )
        return ipv6

    def setRawLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=log=yes'] )
        return ipv6

    def setRawLogPrefix(self, number, prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=log-prefix=' + prefix] )
        return ipv6

    def addToDstAddressListFilter(self,number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=action=add-dst-to-address-list'] )
        return ipv6

    def setAddressListFilter(self,number,addr):
        """
        Method will set address list
        :param number:
        :param addr: address lst t oadd
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set', '=numbers=' + number, '=address-list='+addr] )
        return ipv6

    def setAddressListTimeoutFilter(self,number,timeout):
        """
        Method will set address list timeout
        :param number:
        :param timeout:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=address-list-timeout=' + timeout] )
        return ipv6

    def addToDstAddressListMangle(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=add-dst-to-address-list'] )
        return ipv6

    def setAddressListMangle(self, number, addr):
        """
        Method will set address list
        :param number:
        :param addr: address lst t oadd
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=address-list=' + addr] )
        return ipv6

    def setAddressListTimeoutMangle(self, number, timeout):
        """
        Method will set address list timeout
        :param number:
        :param timeout:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=address-list-timeout=' + timeout] )
        return ipv6

    def addToDstAddressListRAw(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=add-dst-to-address-list'] )
        return ipv6

    def setAddressListRaw(self, number, addr):
        """
        Method will set address list
        :param number:
        :param addr: address lst t oadd
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=address-list=' + addr] )
        return ipv6

    def setAddressListTimeoutRaw(self, number, timeout):
        """
        Method will set address list timeout
        :param number:
        :param timeout:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=address-list-timeout=' + timeout] )
        return ipv6

    def addToSrcAddressListFilter(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/filter/set', '=numbers=' + number, '=action=add-src-to-address-list'] )
        return ipv6

    def addToSrcAddressListMangle(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=add-src-to-address-list'] )
        return ipv6

    def addToSrcAddressListRaw(self, number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=add-src-to-address-list'] )
        return ipv6

    def setDscpActionMangle(self,number):
        """
        Method wil lset  mangle action
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/mangle/set','=numbers='+number,'=action=change-dscp'])
        return ipv6

    def setDscpAValue(self, number,balue="0"):
        """
        Method wil lset  mangle action
        :param number:
        :param balue: value of param
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=new-dscp='+balue] )
        return ipv6

    def setPasthroughMangle(self,number):
        """
        Method will set passthrough
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=passthrough=yes'] )
        return ipv6

    def setMssActionMangle(self,number):
        """
        Method will allow mss action
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=change-mss'] )
        return ipv6

    def setMssValueMangle(self,number,value="0"):
        """
        Method will set mss value
        :param number:
        :param value: for tcp syn set value or clamp-to-pmtu
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=new-mss=' + value] )
        return ipv6

    def setActionChangeHopLimitMangle(self,number):
        """
        Method will set change hop limit
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=change-hop-limit'] )
        return ipv6

    def setHopLimitValueMangle(self,number,value="set/0"):
        """
        Mathod will set hop limit value
        :param number:
        :param value: set,increment,decrement/0 (decimal value)
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=new-hop-limit=' + value] )
        return ipv6

    def setJumpActionFilter(self,number,target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=action=jump','=jump-target='+target] )
        return ipv6

    def setJumpActionMangle(self, number, target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=jump', '=jump-target=' + target] )
        return ipv6

    def setJumpActionRaw(self, number, target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=jump', '=jump-target=' + target] )
        return ipv6

    def setActionLogFilter(self,number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/filter/set', '=numbers=' + number, '=action=log'] )
        return ipv6

    def setActionLogMangle(self, number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=log'] )
        return ipv6

    def setActionLogRaw(self, number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=log'] )
        return ipv6

    def setMarkCOnenctionMangle(self,number):
        """
        Method will mark connection
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=mark-connection'] )
        return ipv6

    def setMarkConnectionValueMangle(self,number,val="no-mark"):
        """
        Method will set value
        :param number:
        :param val: no-mark or specific value
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=new-connection-mark=' + val] )
        return ipv6

    def setMarkPacketMangle(self, number):
        """
        Method will mark connection
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=mark-packet'] )
        return ipv6

    def setMarkPacketValueMangle(self, number, val="no-mark"):
        """
        Method will set value
        :param number:
        :param val: no-mark or specific value
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=new-packet-mark=' + val] )
        return ipv6

    def setNoTrackActionRaw(self,number):
        """
        methodwill not tracm rule
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=notrack'] )
        return ipv6

    def setPassthroughActionFilter(self,number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/filter/set', '=numbers=' + number, '=action=passthrough'] )
        return ipv6

    def setPassthroughActionMangle(self, number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=passthrough'] )
        return ipv6

    def setPassthroughActionRaw(self, number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=passthrough'] )
        return ipv6

    def setRejectActionFIlter(self,number):
        """
        Method will
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set','=numbers='+number,'=action=reject'])
        return ipv6

    def setRejectMessageFilter(self,number,message="icmp-no-route"):
        """
        Method will set reject message
        :param number:
        :param message: icmp-address-unreachable,icmp-admin-prohibited,icmp-no-route,icmp-no-neighbor,icmp-port-unreachable,icmp-reset
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/firewall/filter/set','=numbers='+number,'=reject-with='+message])
        return ipv6

    def setActionReturnFilter(self,number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=action=return'] )
        return ipv6

    def setActionReturnMangle(self, number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=action=return'] )
        return ipv6

    def setActionReturnRaw(self, number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=action=return'] )
        return ipv6