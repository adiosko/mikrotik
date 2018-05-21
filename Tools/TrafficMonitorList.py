from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficMonitorList:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listMonitorlist(self):
        """
        Method will list all monitor lists
        :return:
        """
        mon = self.client.talk(['/tool/traffic-monitor/print'])
        if mon == {}:
            print("No monitoring enabled")
        else:
            print("Name\tInterface\tTraffic\tTrigger\tThreshold")
            for i in mon:
                print(mon[i]['name']+"\t"+mon[i]['interface']+"\t"+mon[i]['traffic']+"\t"+mon[i]['trigger']+
                      "\t"+mon[i]['threshold'])
        return mon

    def addInterface(self,interface):
        """
        method will add interface to monitor
        :param interface:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/add','=interface='+interface] )
        return mon

    def setName(self,number,newName):
        """
        Method wu\ill set monitor name
        :param name:
        :param newName:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/set', '=numbers=' + number,'=name='+newName] )
        return mon

    def setInterface(self,number,interface):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/set', '=numbers=' + number, '=interface=' + interface] )
        return mon

    def setTraffic(self,number,traffic):
        """
        Method will set traffic
        :param number:
        :param traffic: transmitted, received
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/set', '=numbers=' + number, '=traffic=' + traffic] )
        return mon

    def setTrigger(self,number,trigger):
        """
        Method will set trigger
        :param number:
        :param trigger: abow, always,below
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/set', '=numbers=' + number, '=trigger=' + trigger] )
        return mon

    def setThreshold(self,number,threshold):
        """
        Method will set threshold
        :param number:
        :param threshold:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/set', '=numbers=' + number, '=threshold=' + threshold] )
        return mon

    def removeItem(self,number):
        """
        Method will remove item number
        :param number:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/remove', '=numbers=' + number] )
        return mon

    def enableItem(self,number):
        """
        Method will enable item
        :param number:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/enable', '=numbers=' + number] )
        return mon

    def disableItem(self,number):
        """
        Method will disable item
        :param number:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/disable', '=numbers=' + number] )
        return mon

    def commentItem(self,number,comment):
        """
        Method will comment item absed o order number
        :param number:
        :param comment:
        :return:
        """
        mon = self.client.talk( ['/tool/traffic-monitor/set', '=numbers=' + number, '=comment=' + comment] )
        return mon