from tikapy import TikapyClient
from tikapy import TikapySslClient

class UPS:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def  listUPS(self):
        """
        Method will list all UPS connected
        :return:
        """
        ups = self.client.talk(['/system/ups/print'])
        return ups

    def addUPS(self,name,port,offtime,runtime,alarm):
        """
        Method will add new UPS unit
        :param name: name of unit
        :param port: port connected
        :param offtime: time to go offline f.e 00:05:00
        :param runtime:  never or time
        :param alarm: delayed, immediate, low-battery, none
        :return: list
        """
        ups = self.client.talk(['/system/ups/add','=name='+name,'=port='+port,'=offiline-time='+offtime
                                ,'=min-runtime='+runtime,'=alarm-settings='+alarm])
        return ups

    def enableUPS(self,name):
        """
        Method will enable UPS
        :param name: name of ups to enable
        :return: list
        """
        ups = self.client.talk(['/system/ups/set','=numbers='+name,'=disable=no'])
        return ups

    def disableUPS(self,name):
        """
        Method will disable UPS
        :param name: name of UPS to disable
        :return: list
        """
        ups = self.client.talk(['/system/ups/set','=numbers='+name,'=disable=yes'])
        return ups

    def setUPS(self, name,port,offtime,runtime,alarm):
        """
        Method will set existing UPS
        :param name: name f ups to edit
        :param port: port of ups
        :param offtime: offline time
        :param runtime: runtime never or time
        :param alarm: delayed, immediate,low-battery,none
        :return: list
        """
        ups = self.client.talk(['/system/ups/set','=numbers='+name,'=port='+port,'=offiline-time='+offtime
                                ,'=min-runtime='+runtime,'=alarm-settings='+alarm])
        return ups

