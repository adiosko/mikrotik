from tikapy import TikapyClient
from tikapy import TikapySslClient

class securityProfileRadius:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enableMacAuthentication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=radius-mac-authentication=yes'])
        return wifi

    def disableMacAuthentication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=radius-mac-authentication=no'])
        return wifi

    def enableMacAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=radius-mac-accounting=yes'])
        return wifi

    def disableMacAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=radius-mac-accounting=no'])
        return wifi

    def enableEapAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=radius-eap-accounting=yes'])
        return wifi

    def disableEapAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=radius-eap-accounting=no'])
        return wifi

    def setInterimUpdate(self,name,update="00:00:00"):
        """
        Method will set interim update
        :param name:
        :param update:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set', '=numbers=' + name, '=interim-update='+update] )
        return wifi

    def setMacFormat(self,name,format="XX:XX:XX:XX:XX:XX"):
        """

        :param name:
        :param format: "XX XX XX XX XX XX",XX-XX-XX-XX-XX-XX,XX:XX:XX:XX:XX:XX,XXXX:XXXX:XXXX,XXXXXX-XXXXXX,XXXXXX:XXXXXX,XXXXXXXXXXXX
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=radius-mac-format=' + format] )
        return wifi

    def setMacMode(self,name,mode="as-username"):
        """

        :param name:
        :param mode: as-username,as-username-and-password
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=radius-mac-mode=' + mode] )
        return wifi

    def setMacCahingTime(self,name):
        """
        Method will set mac caching time
        :param name:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=radius-mac-caching=disabled'] )
        return wifi