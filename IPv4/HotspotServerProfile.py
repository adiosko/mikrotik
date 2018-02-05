from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotServerProfile:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listProfile(self):
        """
        Methgod will list profiles
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/profile/print'])
        if hotspot == {}:
            print("No profile dound")
        else:
            print("Name\tHtml Directory")
            for i in hotspot:
                print(hotspot[i]['name']+"\t"+hotspot[i]['html-directory'])
        return hotspot

    def addProfile(self,name):
        """
        Method will add profile
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/add','=name='+name] )
        return hotspot

    def removeProfile(self,name):
        """
        Method will remove profile
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/remove', '=numbers=' + name] )
        return hotspot

    #general set
    def setName(self,name,newName):
        """
        Method will rename profile
        :param name:
        :param newName:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name,'=name='+newName] )
        return hotspot

    def setHotspotAddress(self,name,address):
        """
        Method will ser address of hpot
        :param name:
        :param address:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=hotspot-address=' + address] )
        return hotspot

    def setDnsName(self,name,dns):
        """
        Method will set dns for hpot
        :param name:
        :param dns:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=dns-name=' + dns] )
        return hotspot

    def setHtmlDirectory(self,name,dir="flash/hotspot"):
        """
        Method will set hostpot html dir
        :param name:
        :param dir: flash,flash/skins,flash/hotspot/img,flash/hotspot/lv,flash/hotspot,flash/hotspot/xml
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=html-directory=' + dir] )
        return hotspot

    def setHtmlDirecdtoryOverride(self,name,dir):
        """
        Method will set hpot override html
        :param name:
        :param dir:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=html-directory-override=' + dir] )
        return hotspot

    def setRateLimit(self,name,limit):
        """
        Method will set limit tx/rx
        :param name:
        :param limit:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=rate-limit=' + limit] )
        return hotspot

    def setHttpProxy(self,name,address,port):
        """
        Method will set proxy
        :param name:
        :param address:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=http-proxy=' + address+":"+port] )
        return hotspot

    def setSmtpServer(self,name,server):
        """
        Method will set smtp server
        :param name:
        :param server:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=smtp-server=' + server] )
        return hotspot

    #Login
    def setLoginBy(self,name,typeoflogin):
        """
        Method will set logi type
        :param name:
        :param typeoflogin: mac,cookie,http-chap,https,http-pap,trial,mac-cookie
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=login-by=' + typeoflogin] )
        return hotspot

    def setMacAuthenticationMode(self,name,mode):
        """
        Methodw will set auth mode
        :param name:
        :param mode: mac-as-username,mac-as-username-and-password
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=login-by=mac','=mac-auth-mode=' + mode] )
        return hotspot

    def setMacAUthenticationPassword(self,name,password):
        """
        Method will set authenticatuion password
        :param name:
        :param password:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=login-by=mac', '=mac-auth-password=' + password] )
        return hotspot

    def setHttpCookieLifetime(self,name,life="1d 00:00:00"):
        """
        Method will set cookie lifetime
        :param name:
        :param life:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=http-cookie-lifetime=' + life] )
        return hotspot

    def setSslCertificate(self,name,cert):
        """
        Method will set certificate
        :param name:
        :param cert:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=ssl-certificate=' + cert] )
        return hotspot

    def splitUserDomain(self,name):
        """
        Method will spolit domain
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=split-user-domain=yes'] )
        return hotspot

    def setTrialUptimeLimit(self,name,limit="00:30:00"):
        """
        Method will set trial uptime limit
        :param name:
        :param limit:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=trial-uptime-limit=' + limit] )
        return hotspot

    def setTrialUptimeReset(self,name,reste="1d 00:00:00"):
        """
        Method will set reset timeout
        :param name:
        :param reste:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=trial-uptime-reset=' + reste] )
        return hotspot

    def setTrialUptimeUser(self,name,user="default"):
        """
        Method will set trial user
        :param name:
        :param user:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=trial-user-profile=' + user] )
        return hotspot

    #RADIUS
    def enableRadius(self,name):
        """
        Method will enable radius
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=use-radius=yes'] )
        return hotspot

    def setDefaultDOmain(self,name,domain):
        """
        Method will setradius domain
        :param name:
        :param domain:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/profile/set', '=numbers=' + name, '=radius-default-domain=' + domain] )
        return hotspot

    def setLocationId(self,name,ID):
        """
        Method will set radius id
        :param name:
        :param ID:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=radius-location-id=' + ID] )
        return hotspot

    def setLocationName(self,name,location):
        """
        Method will set location name
        :param name:
        :param location:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=radius-location-name=' + location] )
        return hotspot

    def setMacFormat(self,name,formatMac="XX:XX:XX:XX:XX:XX"):
        """
        Method will set mac format
        :param name:
        :param format:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=radius-mac-format=' + formatMac] )
        return hotspot

    def enableAccounting(self,name):
        """
        Method will enable accounting
        :param name:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=radius-accounting=yes'] )
        return hotspot

    def setInterimUpdate(self,name,update="00:00:00"):
        """

        :param name:
        :param update:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=radius-interim-update=' + update] )
        return hotspot

    def setNasPortType(self,name,port="wireless-802.11"):
        """
        Method will set nas port type
        :param name:
        :param port: cable,ethernet,wireless-802.11
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/profile/set', '=numbers=' + name, '=nas-port-type=' + port] )
        return hotspot