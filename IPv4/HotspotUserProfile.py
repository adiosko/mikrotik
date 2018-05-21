from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotUserProfile:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listProfiles(self):
        """
        Method will list profiles
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/user/profile/print'])
        if hotspot == {}:
            print("No profile found")
        else:
            print("Name\tIdle timeout\tShared users")
            for i in hotspot:
                print(hotspot[i]['name']+"\t"+hotspot[i]['idle-timeout']+"\t"+hotspot[i]['shared-users'])
        return hotspot

    def addProfile(self,name):
        """
        Method will add progile
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/add','=name='+name] )
        return hotspot

    def removeProfile(self,name):
        """
        Method will remove profile
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/remove', '=numbers=' + name] )
        return hotspot

    #General
    def setName(self,name,newName):
        """
        Methodwill rename profile
        :param name:
        :param newName:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/set', '=numbers=' + name,'=name='+newName] )
        return hotspot

    def setAddressPool(self,name,pool):
        """
        Method will set pool
        :param name:
        :param pool:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=address-pool=' + pool] )
        return hotspot

    def setSessionTimeout(self,name,timeout):
        """
        Methodwill set session timeout
        :param name:
        :param timeout:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=session-timeout=' + timeout] )
        return hotspot

    def setIdleTimeout(self,name,timeout):
        """
        Method will set idle timeout
        :param name:
        :param timeout:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=idle-timeout=' + timeout] )
        return hotspot

    def setKeepaliveTimeout(self,name,timeout="00:02:00"):
        """
        Method will set keepalive timeout
        :param name:
        :param timeout:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=keepalive-timeout=' + timeout] )
        return hotspot

    def setStatusAutorefresh(self,name,refresh="00:01:00"):
        """
        Method will refresh timeout
        :param name:
        :param refresh:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=status-autorefresh=' + refresh] )
        return hotspot

    def setSharedUsers(self,name,shared="1"):
        """
        Method will set shared users account
        :param name:
        :param shared:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=shared-users=' + shared] )
        return hotspot

    def setRateLimit(self,name,limit):
        """
        Method will set rate limit tx/rx
        :param name:
        :param limit:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=rate-limit=' + limit] )
        return hotspot

    def addMacCookie(self,name):
        """
        Method will enable mac cookie
        :param name:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=add-mac-cookie=yes'] )
        return hotspot

    def setAddressList(self,name,adlist):
        """
        Method will set address list
        :param name:
        :param adlist:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=address-list=' + adlist] )
        return hotspot

    def setIncomingFilter(self,name,filter):
        """
        Method will set incoming filter
        :param name:
        :param filter:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=incoming-filter=' + filter] )
        return hotspot

    def setOutCOmingFilter(self,name,filter):
        """
        Method will set outcoming filter
        :param name:
        :param filter:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=outgoing-filter=' + filter] )
        return hotspot

    def setIncomingPacketMark(self,name,mark):
        """
        Method will set packet mark
        :param name:
        :param mark:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=incoming-packet-mark=' + mark] )
        return hotspot

    def setOutcomingPacketMark(self,name,mark):
        """
        Method will set out packet mark
        :param name:
        :param mark:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=outgoing-packet-mark=' + mark] )
        return hotspot

    def setOpenStatusPage(self,name,page="always"):
        """
        Method will set opening page
        :param name:
        :param page:always, http-login
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=open-status-page=' + page] )
        return hotspot

    def useTransparentProxy(self,name):
        """
        Method will se ttransparent proxy usage
        :param name:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=transparent-proxy=yes'] )
        return hotspot

    #Queue
    def setInsertQueueBefore(self,name,use="before"):
        """

        :param name:
        :param use: firs,last,hs<server1>
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=insert-queue-before=' + use] )
        return hotspot

    def setParenQueue(self,name,queue="none"):
        """
        Method will set parent queue
        :param name:
        :param queue:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=parent-queue=' + queue] )
        return hotspot

    def setQueueType(self,name,queue="default-small"):
        """
        Method will set queue type
        :param name:
        :param queue:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=queue-type=' + queue] )
        return hotspot

    #Advertise
    def advertise(self,name):
        """
        Method will advertise enable
        :param number:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=advertise=yes'] )
        return hotspot

    def setAdvertiseUrl(self,name,url):
        """
        Method will advertise specific web
        :param name:
        :param url:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=advertise-url=' + url] )
        return hotspot

    def setAdvertiseInterval(self,name,interval="00:00:30"):
        """
        Method will advertise web
        :param name:
        :param interval:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=advertise-interval=' + interval] )
        return hotspot

    def setAdvertiseTimeout(self,name,tieout):
        """
        Method will set timeout
        :param name:
        :param tieout:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=advertise-timeout=' + tieout] )
        return hotspot

    #Scripts
    def setOnLoginScript(self,name,script):
        """
        Method will set script on login
        :param name:
        :param script:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=on-login=' + script] )
        return hotspot

    def setOnLogoutScript(self,name,script):
        """
        Method will set logout script
        :param name:
        :param script:
        :return:
        """
        hotspot = self.client.talk(
            ['/ip/hotspot/user/profile/set', '=numbers=' + name, '=on-logout=' + script] )
        return hotspot