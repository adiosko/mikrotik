from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallExtraSetup:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setConnectionLimitLimitFilter(self,number,limit="100",netmask="32"):
        """
        Method wil lset conenction limit of limit
        :param number:
        :param limit: 100 is amount of packets
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=connection-limit=' + limit+","+netmask] )
        return ip

    #netmask sth

    def setConnectionLimitLimitMangle(self, number, limit="100", netmask="32"):
        """
        Method wil lset conenction limit of limit
        :param number:
        :param limit: 100 is amount of packets
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=connection-limit=' + limit + "," + netmask] )
        return ip

    def setConnectionLimitLimitnat(self, number, limit="100", netmask="32"):
        """
        Method wil lset conenction limit of limit
        :param number:
        :param limit: 100 is amount of packets
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=connection-limit=' + limit + "," + netmask] )
        return ip

    def setLimitRateFilter(self,number,rate="0/sec",burst="5",mode="packet"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec or
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=limit=' + rate+","+burst+","+mode] )
        return ip

    def setLimitRateMangle(self, number, rate="0/sec", burst="5", mode="packet"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec or
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, '=limit=' + rate + "," + burst + "," + mode] )
        return ip

    def setLimitRateNat(self, number, rate="0/sec", burst="5", mode="packet"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec or
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, '=limit=' + rate + "," + burst + "," + mode] )
        return ip

    def setDstLimitFilter(self,number,rate="1/sec",burst="5",limitBy="dst-address",expire="100"):
        """
        Method will set destination limit
        :param number:
        :param limit: number/sec,min,hour
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=dst-limit=' +rate+","+burst+","+limitBy+"/"+expire] )
        return ip

    def setDstLimitMangle(self, number, rate="1/sec", burst="5", limitBy="dst-address", expire="100"):
        """
        Method will set destination limit
        :param number:
        :param limitBy: address-and-dst-port,dst-address,dst-address-and-port,src-address,src-and-dst-address
        :param limit: number/sec,min,hour
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number,
                                '=dst-limit=' + rate + "," + burst + "," + limitBy + "/" + expire] )
        return ip

    def setDstLimitNat(self, number, rate="1/sec", burst="5", limitBy="dst-address", expire="100"):
        """
        Method will set destination limit
        :param number:
        :param limit: number/sec,min,hour
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number,
                                '=dst-limit=' + rate + "," + burst + "," + limitBy + "/" + expire] )
        return ip

    def setNthFilter(self,number,repeattime="2",packet="0"):
        """
        Method will set nth factor
        :param number:
        :param repeatcycle:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=nth=' + repeattime+","+packet] )
        return ip

    def setNthMangle(self, number, repeattime="2", packet="0"):
        """
        Method will set nth factor
        :param number:
        :param repeatcycle:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=nth=' + repeattime + "," + packet] )
        return ip

    def setNthNat(self, number, repeattime="2", packet="0"):
        """
        Method will set nth factor
        :param number:
        :param repeatcycle:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=nth=' + repeattime + "," + packet] )
        return ip

    def setTimeFilter(self,number,fromDate="00:00:00",toDate="1d 00:00:00",day="mon,tue"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number,"=time="+fromDate+","+toDate+","+day] )
        return ip

    def setTimeMangle(self, number, fromDate="00:00:00", toDate="1d 00:00:00", day="mon,tue"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/mangle/set', '=numbers=' + number, "=time=" + fromDate + "," + toDate + "," + day] )
        return ip

    def setTimeNat(self, number, fromDate="00:00:00", toDate="1d 00:00:00", day="mon,tue"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ip = self.client.talk(
            ['/ip/firewall/nat/set', '=numbers=' + number, "=time=" + fromDate + "," + toDate + "," + day] )
        return ip

    def setSrcAddressTypeFilter(self,number,filter="unicast"):
        """
        Method will set src nat fil;ter
        :param number:
        :param filter: blackhole, broadcast, local,multicast,prohibit,unicastmunreachable,!
        :return:
        """
        ip =self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=src-address-type='+filter])
        return ip

    def setSrcAddressTypeNat(self, number, filter="unicast"):
        """
        Method will set src nat fil;ter
        :param number:
        :param filter: blackhole, broadcast, local,multicast,prohibit,unicastmunreachable,!
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=src-address-type=' + filter] )
        return ip

    def setSrcAddressTypeMangle(self, number, filter="unicast"):
        """
        Method will set src nat fil;ter
        :param number:
        :param filter: blackhole, broadcast, local,multicast,prohibit,unicastmunreachable,!
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=src-address-type=' + filter] )
        return ip

    def setDstAddressTypeFilter(self, number, filter="unicast"):
        """
        Method will set src nat fil;ter
        :param number:
        :param filter: blackhole, broadcast, local,multicast,prohibit,unicastmunreachable,!
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/filter/set', '=numbers=' + number, '=dst-address-type=' + filter] )
        return ip

    def setDstAddressTypeMangle(self, number, filter="unicast"):
        """
        Method will set src nat fil;ter
        :param number:
        :param filter: blackhole, broadcast, local,multicast,prohibit,unicastmunreachable,!
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=dst-address-type=' + filter] )
        return ip

    def setDstAddressTypeNat(self, number, filter="unicast"):
        """
        Method will set src nat fil;ter
        :param number:
        :param filter: blackhole, broadcast, local,multicast,prohibit,unicastmunreachable,!
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=dst-address-type=' + filter] )
        return ip

    def setPsdFilter(self,number,weightThreshold="21",delayThreshold="00:00:03",lowPortWight="3",highPortWeight="1"):
        """
        Metho will set port filter
        :param number:
        :param weightThreshold:
        :param delayThreshold:
        :param lowPortWight:
        :param highPortWeight:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=psd='+weightThreshold+","+delayThreshold+","+lowPortWight+","+highPortWeight])
        return ip

    def setPsdMangle(self, number, weightThreshold="21", delayThreshold="00:00:03", lowPortWight="3",
                     highPortWeight="1"):
        """
        Metho will set port filter
        :param number:
        :param weightThreshold:
        :param delayThreshold:
        :param lowPortWight:
        :param highPortWeight:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number,
                                '=psd=' + weightThreshold + "," + delayThreshold + "," + lowPortWight + "," + highPortWeight] )
        return ip

    def setPsdNat(self, number, weightThreshold="21", delayThreshold="00:00:03", lowPortWight="3",
                     highPortWeight="1"):
        """
        Metho will set port filter
        :param number:
        :param weightThreshold:
        :param delayThreshold:
        :param lowPortWight:
        :param highPortWeight:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number,
                                '=psd=' + weightThreshold + "," + delayThreshold + "," + lowPortWight + "," + highPortWeight] )
        return ip

    def setHotspotFilter(self,number,hotspot="from-client"):
        """
        Method will set hotspot authentication
        :param number:
        :param hotspot: auth,from-client,http,local-dst,to-client
        :return:
        """
        ip = self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=hotspot='+hotspot])
        return ip

    def setHotspotMangle(self, number, hotspot="from-client"):
        """
        Method will set hotspot authentication
        :param number:
        :param hotspot: auth,from-client,http,local-dst,to-client
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=hotspot=' + hotspot] )
        return ip

    def setHotspotNat(self, number, hotspot="from-client"):
        """
        Method will set hotspot authentication
        :param number:
        :param hotspot: auth,from-client,http,local-dst,to-client
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=hotspot=' + hotspot] )
        return ip

    def setIpFragmentFilter(self,number):
        """
        Method will allow ip fragment
        :param number:
        :return:
        """
        ip =self.client.talk(['/ip/firewall/filter/set','=numbers='+number,'=fragment=yes'])
        return ip

    def setIpFragmentMangle(self, number):
        """
        Method will allow ip fragment
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/mangle/set', '=numbers=' + number, '=fragment=yes'] )
        return ip

    def setIpFragmentNat(self, number):
        """
        Method will allow ip fragment
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/nat/set', '=numbers=' + number, '=fragment=yes'] )
        return ip