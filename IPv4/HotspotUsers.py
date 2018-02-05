from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotUsers:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listUsers(self):
        """
        Method will list users
        :return:
        """
        user = self.client.talk(['/ip/hotspot/user/print'])
        if user == {}:
            print("No user found")
        else:
            print("Server\tName\tUptime")
            for i in user:
                print(user[i]['name']+"\t"+user[i]['uptime'])
        return user

    def addUser(self,name):
        """
        Method wil ladd user
        :param name:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/add','=name='+name] )
        return user

    def removeUser(self,name):
        """
        Method will remove user
        :param name:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/remove', '=numbers=' + name] )
        return user

    def enableUser(self,name):
        """
        Method will enable user
        :param name:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/enable', '=numbers=' + name] )
        return user

    def disableUser(self,name):
        """
        Method will disable user
        :param name:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/disable', '=numbers=' + name] )
        return user

    def commentUser(self,name,comment):
        """
        Method will comment user
        :param name:
        :param comment:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/comment', '=numbers=' + name,'=comment='+comment] )
        return user

    def resetCounters(self,name):
        """
        Method will reset counters
        :param name:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/reset-counters', '=numbers=' + name] )
        return user

    #general
    def setServer(self,name,server="all"):
        """
        Method will se tcounters
        :param name:
        :param server: all,created servers
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name,'=server='+server] )
        return user

    def setName(self,name,newName):
        """
        Method will set new name
        :param name:
        :param newName:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=name=' + newName] )
        return user

    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=password=' + password] )
        return user

    def setAddress(self,name,address):
        """
        Method will set address
        :param name:
        :param address:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=address=' + address] )
        return user

    def setMacAddress(self,name,mac):
        """
        Method will set mac address
        :param name:
        :param mac:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=mac-server=' + mac] )
        return user

    def setProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=profile=' + profile] )
        return user

    def setRoutes(self,name,route):
        """
        Method will set routes
        :param name:
        :param route:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=routes=' + route] )
        return user

    def setEmail(self,name,mail):
        """
        Method will set mail
        :param name:
        :param mail:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=email=' + mail] )
        return user

    #Limits
    def setLimitUptime(self,name,uptime="00:00:00"):
        """
        Method will set uptime limit
        :param name:
        :param uptime:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=limit-uptime=' + uptime] )
        return user

    def setLimitBytesIn(self,name,bteIn="0"):
        """
        Method will set byets in limit
        :param name:
        :param bteIn:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=limit-bytes-in=' + bteIn] )
        return user

    def setLimitBytesOut(self, name, bteOut="0"):
        """
        Method will set byets in limit
        :param name:
        :param bteIn:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=limit-bytes-out=' + bteOut] )
        return user

    def setLimitBytesTotal(self,name,bteTotal="0"):
        """
        Method will set bytes in total
        :param name:
        :param bteTotal:
        :return:
        """
        user = self.client.talk( ['/ip/hotspot/user/set', '=numbers=' + name, '=limit-bytes-total=' + bteTotal] )
        return user

