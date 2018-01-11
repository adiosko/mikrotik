from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimInterfaces:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list pim interfaces
        :return:
        """
        pim = self.client.talk(['/routing/pim/interface/print'])
        if pim == {}:
            print("No pim iface found")
        else:
            print("Interface\tProtocols\tDseig router\talternative subnets")
            for i in pim:
                print(pim[i]['interface']+"\t"+pim[i]['protocols']+"\t"+pim[i]['alternative-subnets'])
        return pim

    def addPimInterface(self):
        """
        Method will add interface
        :return:
        """
        pim = self.client.talk(['/routing/pim/interface/add'])
        return pim

    def removePimInterface(self,number):
        """
        Method will remove pi iface
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/remove','=numbers='+number] )
        return pim

    def enableInterface(self,number):
        """
        Method will enable pim iface
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/enable','=numbers='+number] )
        return pim

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/disable','=numbers='+number] )
        return pim

    def commentInterface(self,number,comment):
        """
        Method will comment interface
        :param number:
        :param comment:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/comment','=numbers='+number,'=comment='+comment] )
        return pim

    def setInterface(self,number,interface="all"):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=interface=' + interface] )
        return pim

    def setProtocol(self,number,protocol="pim"):
        """
        Method will set protocol pim
        :param number:
         :param protocol: pim,igmp
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=protocol=' + protocol] )
        return pim

    def setDesignatedRouterPriority(self,number,priority="1"):
        """
        Method will set igmp priority
        :param number:
        :param priority:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=dr-priority==' + priority] )
        return pim

    def setHelloPeriod(self,number,period="00:00:30"):
        """
        Method will set hello interval
        :param number:
        :param period:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=hello-period=' + period] )
        return pim

    def setHelloTrigerDelay(self,number,delay="00:00:05"):
        """
        Method will set delay
        :param number:
        :param delay:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=hello-trigerred-delay=' + delay] )
        return pim

    def setHelloHoldTime(self,number,time="00:01:45"):
        """
        Method will set hold time
        :param number:
        :param time:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=hello-holdtime=' + time] )
        return pim

    def setPropagationDelay(self,number,delay="50"):
        """
        Method will set delay
        :param number:
        :param delay:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=propagation-delay=' + delay] )
        return pim

    def setOverideInterval(self,number,interval="250"):
        """
        Method will set override interval
        :param number:
        :param interval:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=override-interval=' + interval] )
        return pim

    def enableTrackingSupport(self,number):
        """
        Method will enable track support
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=tracking-support=yes'] )
        return pim

    def disableTrackingSupport(self,number):
        """
        Method will disable track support
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=tracking-support=no'] )
        return pim

    def requiereHello(self,number):
        """
        Method will reuqire hello
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=require-hello=yes'] )
        return pim

    def unrequiereHello(self,number):
        """
        Method will not requiere hello interval
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=require-hello=no'] )
        return pim

    def setJoinPrunePeriod(self,number,period="00:01:00"):
        """
        Method will join prune period interval set
        :param number:
        :param period:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=join-prune-period=' + period] )
        return pim

    def setJoinPruneHoldtime(self,number,time="00:03:30"):
        """
        Method will join holdtime
        :param number:
        :param time:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=join-prune-holdtime=' + time] )
        return pim

    def setAssertTime(self,number,time="00:03:00"):
        """
        Method will set assert time
        :param number:
        :param time:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=assert-time=' + time] )
        return pim

    def setAssertOverrideInterval(self,number,interval="00:00:03"):
        """
        Method will set override interval
        :param number:
        :param interval:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=assert-override-interval='+interval] )
        return pim

    def setAlternativeSubnet(self,number,subnet="0.0.0.0/0"):
        """
        mETHOD will set alternate subnet
        :param number:
        :param subnet:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=alternative-subnets=' + subnet] )
        return pim

    def setIgmpVersion(self,number,version="IGMPv2"):
        """
        Method will set igmp version
        :param number:
        :param version: IGMPv1,IGMPv2,IGMPv3
        :return:
        """
        pim = self.client.talk( ['/routing/pim/interface/set', '=numbers=' + number, '=igmp-version=' + version] )
        return pim