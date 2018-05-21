from tikapy import TikapyClient
from tikapy import TikapySslClient

class accessListSet:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setMacAddress(self,number,mac):
        """
        Method will set mac address
        :param number:
        :param mac:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/access-list/set','=numbers='+number,'=mac-address='+mac])
        return wifi

    def setInterface(self,number,interface="all"):
        """

        :param number:
        :param interface:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=interface=' + interface] )
        return wifi

    def setSignal(self,number,signalFrom="-120",signalTo="120"):
        """
        Method will set db filter
        :param number:
        :param signalFrom:
        :param signalTo:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=signal-range=' + signalFrom+".."+signalTo] )
        return wifi

    def setSignalOutOfRangeInterval(self,number,interval="00:00:10"):
        """

        :param number:
        :param interval:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=allow-signal-out-of-range=' + interval] )
        return wifi

    def setApTxLimit(self,number,limit="0"):
        """
        Method will  set limit
        :param number:
        :param limit:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=ap-tx-limit=' + limit] )
        return wifi

    def setClientTxLimit(self,number,limit="0"):
        """

        :param number:
        :param limit:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=client-tx-limit=' + limit] )
        return wifi

    def enableAuthentication(self,number):
        """
        Method will enable authentication
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=authentication=yes'] )
        return wifi

    def disableAuthentication(self,number):
        """
        Method will enable authentication
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=authentication=no'] )
        return wifi

    def enableForwarding(self,number):
        """
        Method will  enable forwarding
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=forwarding=yes'] )
        return wifi


    def disableForwarding(self, number):
        """
        Method will enable authentication
        :param number:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/access-list/set', '=numbers=' + number, '=forwarding=no'] )
        return wifi

    def setVlanMode(self,number,vlan="default"):
        """

        :param number:
        :param vlan:default,no-tag,use-service-tag,use-tag
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=vlan-mode='+vlan] )
        return wifi

    def setVlanId(self,number,vlan="1"):
        """

        :param number:
        :param vlan:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=vlan-id=' + vlan] )
        return wifi

    def setPrivateKeyAlgorhitm(self,number,mode):
        """

        :param number:
        :param mode:  40bit-wep,104bit-wep,aes-com,none,tkip
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=private-algo=' + mode] )
        return wifi

    def setPrivateKeyValue(self,number,value):
        """

        :param number:
        :param value:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=private-key=' + value] )
        return wifi

    def setPrivatePreSharedKey(self,number,password):
        """
        Method will set private psh
        :param number:
        :param password:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=private-pre-shared-key=' + password] )
        return wifi

    def setManagementProtectionKey(self,number,password):
        """

        :param number:
        :param password:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=management-protection-key=' + password] )
        return wifi

    def setTime(self,number,timeFrom,timeTo,days):
        """

        :param number:
        :param timeFrom:
        :param timeTo:
        :param days: mon,tue,wed,thu,fri,sat,sun
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/set', '=numbers=' + number, '=time=' + timeFrom+"-"+timeTo+","+days] )
        return wifi


