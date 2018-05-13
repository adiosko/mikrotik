from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficEngInterface:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterface(self):
        """
        Method will list interfaces
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/interface/print'])
        if mpls == {}:
            print("No iface found")
        else:
            print("Interface\tbandwidth\tMetric\tRemaining bw")
            for i in mpls:
                print(mpls[i]['interface']+"\t"+mpls[i]['bandwidth']+"\t"+mpls[i]['te-metric']+"\t"+mpls[i]['remaining-bw'])
        return mpls

    def addInterface(self,interface):
        """
        Method will add interface
        :param interface:
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/interface/add','=interface='+interface])
        return mpls

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/remove', '=numbers=' + number] )
        return mpls

    def enableInterface(self,number):
        """
        Method will enable interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/enable', '=numbers=' + number] )
        return mpls

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/disable', '=numbers=' + number] )
        return mpls

    def setInterface(self,number,interface):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number,'=interface='+interface] )
        return mpls

    def setBandwidth(self,number,bw):
        """
        Method will set bw
        :param number:
        :param bw: integer value
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number,'=bandwidth='+bw] )
        return mpls

    def setKFactor(self,number,factor="3"):
        """
        Methodwill set k factor for bw calculation
        :param number:
        :param factor:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=bandwidth-k-factor=' + factor] )
        return mpls

    def setResourceClass(self,number,rsc="0"):
        """
        Method will set resource class
        :param number:
        :param rsc: hex value
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=resource-class=' + rsc] )
        return mpls

    def setRefreshTime(self,number,time="30.000"):
        """
        Method will set refresher
        :param number:
        :param time:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=refresh-time=' + time] )
        return mpls

    def useUdp(self,number):
        """
        Method will use udp protocol
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=use-udp=yes'] )
        return mpls

    def blockadeKFactor(self,number,factor="3"):
        """
        Method will set k factor blockade
        :param number:
        :param factor:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=blockade-k-factor=' + factor] )
        return mpls

    def setMetric(self,number,metric="1"):
        """
        Method will set te metric
        :param number:
        :param metric:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=te-metric=' + metric] )
        return mpls

    def setIgpFloodPeriod(self,number,period="00:03:00"):
        """
        Method will set flood period
        :param number:
        :param period:
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=igp-flood-period=' + period] )
        return mpls

    def setUpFloodThreshold(self,number,trs="15,30,45,60,75,80,85,90,95,97,98,99,100"):
        """
        Method will set threshold
        :param number:
        :param trs:15,30,45,60,75,80,85,90,95,97,98,99,100
        :return:
        """
        mpls = self.client.talk( ['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=up-flood-threshold=' + trs] )
        return mpls

    def setDownFloodThreshold(self,number,trs="15,30,45,60,75,80,85,90,95,97,98,99,100"):
        """
        Method will set down flood threshold
        :param number:
        :param trs: 15,30,45,60,75,80,85,90,95,97,98,99,100
        :return:
        """
        mpls = self.client.talk(['/mpls/traffic-eng/interface/set', '=numbers=' + number, '=down-flood-threshold=' + trs] )
        return mpls