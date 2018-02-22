from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeNatAction:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setAcceptFilter(self,number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk(['/interface/bridge/nat/set','=numbers='+number,'=action=accept'])
        return ip

    def setArpReply(self,number):
        """
        Method wil lset acation
        :param number:
        :return:
        """
        ip = self.client.talk(['/interface/bridge/nat/set','=numbers='+number,'=action=arp-reply'])
        return ip

    def setSrcMAcAddress(self,number,mac):
        """
        Method wil lset arp src mac address
        :param number:
        :param mac:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=src-mac-address='+mac] )
        return ip


    def setLog(self, number):
        """
        Method will accept rule
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=log=yes'] )
        return ip

    def setLogPrefix(self, number, prefix):
        """
        Method will accept rule
        :param number:
        :param prefix: log prefix
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=log-prefix=' + prefix] )
        return ip

    def setDrop(self,number):
        """
        Method will set drop action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=drop'] )
        return ip

    def setDstNat(self, number):
        """
        Method wil lset ds tnat
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=dst-nat'] )
        return ip

    def setDstNatAddress(self, number, address):
        """
        Method wil lset ds tnat
        :param number:
        :param address: address to translate
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=to-dst-mac-address=' + address] )
        return ip

    def setJumpActionTarget(self, number, target):
        """
        Method will set  jump action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=action=jump', '=jump-target=' + target] )
        return ip

    def setJump(self,number):
        """
        Method will set jump action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=jump'] )
        return ip

    def setActionLog(self, number):
        """
        Method will set action log
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=action=log'] )
        return ip

    def setMarkPacket(self, number):
        """
        Method will mark connection
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=action=mark-packet'] )
        return ip

    def setMarkPacketValue(self, number, val="no-mark"):
        """
        Method will set value
        :param number:
        :param val: no-mark or specific value
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=new-packet-mark=' + val] )
        return ip

    def setPassthroughAction(self, number):
        """
        Method will set passthrough action
        :param number:
        :return:
        """
        ip = self.client.talk(
            ['/interface/bridge/nat/set', '=numbers=' + number, '=action=passthrough'] )
        return ip

    def setRedirect(self, number):
        """
        Method will redirect rule to port
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=redirect'] )
        return ip

    def setActionReturn(self, number):
        """
        Method will set return action
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=return'] )
        return ip

    def setPriorityAction(self, number):
        """
        Method will set action priority
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=set-priority'] )
        return ip

    def setPriorityValue(self, number, priority):
        """
        Method will set priority
        :param number:
        :param priority:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=new-priority=' + priority] )
        return ip

    def setPasthroughEnable(self, number):
        """
        Method will set passthrough
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=passthrough=yes'] )
        return ip

    def setSrcNat(self, number):
        """
        Methodwill set src nat
        :param number:
        :return:
        """
        ip = self.client.talk( ['/interface/bridge/nat/set', '=numbers=' + number, '=action=src-nat'] )
        return ip