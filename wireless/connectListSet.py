from tikapy import TikapyClient
from tikapy import TikapySslClient

class connectListSet:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setInterface(self,number,interface):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/set','=numbers='+number,'=interface='+interface])
        return wifi

    def setMacAddress(self,number,mac):
        """
        Method wil lset mac address
        :param number:
        :param mac:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/connect-list/set', '=numbers=' + number, '=mac--address=' + mac] )
        return wifi

    def connect(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/connect-list/set', '=numbers=' + number, '=connect=yes'] )
        return wifi

    def disconnect(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/connect-list/set', '=numbers=' + number, '=connect=no'] )
        return wifi

    def setSsid(self,number,ssid):
        """
        Method will set ssid
        :param number:
        :param ssid:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/connect-list/set', '=numbers=' + number, '=ssid='+ssid] )
        return wifi

    def setAreaPrefix(self,number,prefix):
        """

        :param number:
        :param prefix:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/connect-list/set', '=numbers=' + number, '=area-prefix=' + prefix] )
        return wifi

    def setSignalRange(self,number,signalFrom,signalTo):
        """

        :param number:
        :param signalFrom:
        :param signalTo:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/set','=numbers='+number,'=signal-range='+signalFrom+".."+signalTo])
        return wifi

    def allowSignalOutOfRange(self,number,signal):
        """
        Method will set out of ignal range
        :param number:
        :param signal:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/connect-list/set', '=numbers=' + number,'=allow-signal-out-of-range='+signal ])
        return wifi

    def setWirelessProtocol(self,number,protocol="any"):
        """
        Method will set wireless protocol
        :param number:
        :param protocol:any,802.11,stream,nv2
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/set','=numbers='+number,'=wireless-protocol='+protocol])
        return wifi

    def setSecurityProfile(self,number,profile="default"):
        """

        :param number:
        :param profile: default,default-encrypt,custom
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/set','=numbers='+number,'=security-profile='+profile])
        return wifi