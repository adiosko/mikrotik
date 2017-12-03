from tikapy import TikapyClient
from tikapy import TikapySslClient

class Netwatch:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNetwatchSessions(self):
        """
        Method will list all netwatch sessions
        :return:
        """
        net = self.client.talk(['/tool/netwatch/print'])
        if net == {}:
            print("No netwatch found")
        else:
            print("host\tinterval\tstatus\tsince")
            for i in net:
                print(net[i]['host']+"\t"+net[i]['interval']+"\t"+net[i]['status']+"\t"+net[i]['since'])
        return net

    def addNetwatch(self,host,interval,timeout):
        """
        Method will add netwarch host
        :param host: ip
        :param interval: time interval f.e 00:00:10
        :param timeout: 1000 default
        :return:
        """
        net = self.client.talk(['/tool/netwatch/add','=host='+host,'=interval='+interval,'=timeout='+timeout])
        return net

    def setNetwachHost(self,number,host):
        """
        Method will set host of current netwatch record
        :param number: number to edit
        :param host: host t chanbe
        :return:
        """
        net = self.client.talk(['/tool/netwatch/set','=numbers='+number,'=host=' + host] )
        return net

    def setNetwatchInterval(self,number,interval):
        """
        Method will set netwatch interval
        :param number: number of netwatch record to change
        :param interval: interval
        :return:
        """
        net = self.client.talk(['/tool/netwatch/set','=numbers='+number,'=interval='+interval])
        return net

    def setNetwatchTimeout(self,number,timeout):
        """
        Method will set timeout
        :param number: numbe rof record to set
        :param timeout: timeout to set
        :return:
        """
        net = self.client.talk( ['/tool/netwatch/set', '=numbers=' + number, '=timeout=' + timeout] )
        return net

    def removeNetwatch(self,number):
        """
        Method will remove netwatch
        :param number: numbe rof netwatch to remove
        :return:
        """
        net = self.client.talk(['/tool/netwatch/remove','=numbers='+number])
        return net

    def enableNetwatch(self,number):
        """
        Method will enable netwatch
        :param number: number to enable
        :return:
        """
        net = self.client.talk(['/tool/netwatch/enable','=numbers='+number])
        return net

    def disableNetwatch(self,number):
        """
        Method will disable netwatch
        :param number: number to disable
        :return:
        """
        net = self.client.talk(['/tool/netwatch/disable','=numbers='+number])
        return net

    def commentRule(self,number,comment):
        """
        Method will comment existing rule
        :param number: number to commment
        :param comment: comment
        :return:
        """
        net = self.client.talk(['/tool/netwatch/comment','=numbers='+number,'=comment='+comment])
        return net

