from tikapy import TikapyClient
from tikapy import TikapySslClient

class accessListSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setMacAddress(self,number,mac):
        """

        :param number:
        :param mac:
        :return:
        """
        wifi = self.client.talk(['/caps-man/access-list/set','=numbers='+number,'=mac-address='+mac])
        return wifi

    def setMacMask(self,number,mask):
        """

        :param number:
        :param mask:  00:00:00:00:00:00
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=mac-address-mask=' + mask] )
        return wifi

    def setInterface(self,number,iface):
        """

        :param number:
        :param iface:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=interface=' + iface] )
        return wifi

    def setSsidRegexp(self,number,ssid):
        """

        :param number:
        :param ssid:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=ssid-regexp=' + ssid] )
        return wifi

    def setSignalRange(self,number,signalFrom,signalTo):
        """

        :param number:
        :param signalFrom: -120 eg.
        :param signalTo: 120 eg
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=signal-rnage=' + signalFrom+".."+signalTo] )
        return wifi

    def setAction(self,number,action="accept"):
        """

        :param number:
        :param action: accept,query-radius,reject
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=action=' + action] )
        return wifi

    def setApTxLimit(self,number,limit):
        """

        :param number:
        :param limit:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=ap-tx-limit=' + limit] )
        return wifi

    def setClientTxLimit(self,number,limit):
        """

        :param number:
        :param limit:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=client-tx-limit=' + limit] )
        return wifi

    def setPrivatePassphrase(self,number,passphrase):
        """

        :param number:
        :param passphrase:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=private-passphrase=' + passphrase] )
        return wifi

    def setClient2ClientForward(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number,'=client-to-client-forwarding=yes'] )
        return wifi

    def unsetClient2ClientForward(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(
            ['/caps-man/access-list/set', '=numbers=' + number, '=client-to-client-forwarding=no'] )
        return wifi

    def enableRadius(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk(['/caps-man/access-list/set', '=numbers=' + number, '=radius-accounting=yes'] )
        return wifi

    def disableRadius(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=radius-accounting=no'] )
        return wifi

    def setVlanMode(self,number,mode="no-tag"):
        """

        :param number:
        :param mode: no-tag,use-service-tag,use-tag
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=vlan-mode='+mode] )
        return wifi

    def setVladID(self,number,vlan):
        """

        :param number:
        :param vlan:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/access-list/set', '=numbers=' + number, '=vlan-id='+vlan] )
        return wifi