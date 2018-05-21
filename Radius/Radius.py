from tikapy import TikapyClient
from tikapy import TikapySslClient

class Radius:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRadius(self):
        """
        Method will list radius settings
        :return:
        """
        radius = self.client.talk(['/radius/print'])
        if radius == {}:
            print("No radius server is set up")
        else:
            print("Service\tCalledID\tDomain\taddress\tsecret")
            for i in radius:
                print(radius[i]['service']+"\t"+radius[i]['called-id']+"\t"+radius[i]['domain']+
                      "\t"+radius[i]['address']+"\t"+radius[i]['secret'])
        return radius

    def addRadius(self,address):
        """
        Method will add radius with its address
        :param address: IP of radius
        :return:
        """
        radius = self.client.talk(['/radius/add','=address='+address])
        return radius

    def removeRadius(self,number):
        """
        Method will remove radius server
        :param number: order no
        :return:
        """
        radius = self.client.talk( ['/radius/remove', '=numbers=' + number] )
        return radius

    def disableRadius(self,number):
        """
        Method will disable radius server
        :param number:
        :return:
        """
        radius = self.client.talk( ['/radius/disable', '=numbers=' + number] )
        return radius

    def enableRadius(self,number):
        """
        Method will enable radius server
        :param number:
        :return:
        """
        radius = self.client.talk( ['/radius/enable', '=numbers=' + number] )
        return radius

    def commentRadius(self,number,comment):
        """
        Method will set comment
        :param number:
        :param comment:
        :return:
        """
        radius = self.client.talk( ['/radius/comment', '=numbers=' + number,'=comment='+comment] )
        return radius

    def printIncommingSettings(self):
        """
        Method will set incoming settings
        :return:
        """
        radius = self.client.talk( ['/radius/incoming/print'] )
        print(radius)
        return radius

    def enableIncomming(self):
        """
        Method will enable incomming communication
        :return:
        """
        radius = self.client.talk( ['/radius/incoming/set','=accept=yes'] )
        return radius

    def setIncommingPort(self,port="3379"):
        """
        Method will set custom incomming port
        :param port:  def 3379
        :return:
        """
        radius = self.client.talk( ['/radius/incoming/set', '=port='+port] )
        return radius

    def disableIncommingTraffic(self):
        """
        Method will disable incomming traffic
        :return:
        """
        radius = self.client.talk( ['/radius/incoming/set', '=accept=no'] )
        return radius

    def resetIncommingCounters(self):
        """
        Method will reset incoming stats
        :return:
        """
        radius = self.client.talk( ['/radius/incoming/reset-counters'] )
        return radius

    def resetAllRadiusCounters(self):
        """
        Method will reset all stats
        :return:
        """
        radius = self.client.talk( ['/radius/reset-counters'] )
        return radius

    def monitorRadius(self,number,interval="5s"):
        """
        Method will list all stats in time interval
        :param number:
        :param interval:
        :return:
        """
        radius = self.client.talk( ['/radius/monitor', '=numbers='+number,'=interval='+interval] )
        return radius

    def setRadiusService(self,number,service):
        """
        Method will set service on number
        :param number:
        :param service: ppp, hotspot,dhcp,login,wireless,ipsec
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers='+number,'=service='+service] )
        return radius

    def setCalledId(self,number,ID):
        """
        Method will set called id
        :param number: number to use
        :param ID: ID
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=called-id=' +ID] )
        return radius

    def setDomain(self,number,domain):
        """
        Method will set domain of radius
        :param number:
        :param domain:
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=domain=' + domain] )
        return radius

    def setAddress(self,number,address):
        """
        Method will set radius address
        :param number:
        :param address:
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=address=' + address] )
        return radius

    def setSecret(self,number,secret):
        """
        Method will set radius password
        :param number:
        :param secret:
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=secret=' + secret] )
        return radius

    def setAuthenticationPort(self,number,port="1812"):
        """
        Method will set custom authentication port
        :param number:
        :param port: def 1812
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=authentication-port=' + port] )
        return radius

    def setAccountingPort(self,number,port="1813"):
        """
        Method will set accounting port
        :param number:
        :param port: def 1813
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=accounting-port=' + port] )
        return radius

    def setTimeout(self,number,timeout="300"):
        """
        method will set custom timeout
        :param number:
        :param timeout: 00:00:00:010 - 00:00:10
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=timeout=' + timeout] )
        return radius

    def enableAccountingBackup(self,number):
        """
        Method will set enable backup
        :param number:
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=accounting-backup=yes'] )
        return radius

    def disableAccountingBackup(self,number):
        """
        Method will disable accounting backup
        :param number:
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=accounting-backup=no'] )
        return radius

    def setRealm(self,number,realm):
        """
        Method will set realm for backup for accounting
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=realm='+realm] )
        return radius

    def setSourceAddress(self,number,src):
        """
        Method will set src address for accounting backup
        :param number:
        :param src:
        :return:
        """
        radius = self.client.talk( ['/radius/set', '=numbers=' + number, '=src-address='+src] )
        return radius