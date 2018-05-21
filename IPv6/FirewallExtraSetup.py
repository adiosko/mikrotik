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
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=connection-limit=' + limit+","+netmask] )
        return ipv6

    #netmask sth

    def setConnectionLimitLimitMangle(self, number, limit="100", netmask="32"):
        """
        Method wil lset conenction limit of limit
        :param number:
        :param limit: 100 is amount of packets
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=connection-limit=' + limit + "," + netmask] )
        return ipv6

    def setConnectionLimitLimitRaw(self, number, limit="100", netmask="32"):
        """
        Method wil lset conenction limit of limit
        :param number:
        :param limit: 100 is amount of packets
        :return:
        """
        ipv6 = self.client.talk(
            ['/ipv6/firewall/raw/set', '=numbers=' + number, '=connection-limit=' + limit + "," + netmask] )
        return ipv6

    def setLimitRateFilter(self,number,limit="0/sec"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=limit=' + limit] )
        return ipv6

    def setLimitRateMangle(self, number, limit="0/sec"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=limit=' + limit] )
        return ipv6

    def setLimitRateRaw(self, number, limit="0/sec"):
        """
        Method will set limit rate
        :param number:
        :param limit: sec,min,hour format number/sec
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=limit=' + limit] )
        return ipv6

    def setDstLimitFilter(self,number,limit="1/sec"):
        """
        Method will set destination limit
        :param number:
        :param limit: number/sec,min,hour
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=dst-limit=' + limit] )
        return ipv6

    def setDstLimitMangle(self, number, limit="1/sec"):
        """
        Method will set destination limit
        :param number:
        :param limit: number/sec,min,hour
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=dst-limit=' + limit] )
        return ipv6

    def setDstLimitRaw(self, number, limit="1/sec"):
        """
        Method will set destination limit
        :param number:
        :param limit: number/sec,min,hour
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=dst-limit=' + limit] )
        return ipv6

    def setNthFilter(self,number,repeatcycle="2/0"):
        """
        Method will set nth factor
        :param number:
        :param repeatcycle:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=nth=' + repeatcycle] )
        return ipv6

    def setNthMangle(self, number, repeatcycle="2/0"):
        """
        Method will set nth factor
        :param number:
        :param repeatcycle:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=nth=' + repeatcycle] )
        return ipv6

    def setNthRaw(self, number, repeatcycle="2/0"):
        """
        Method will set nth factor
        :param number:
        :param repeatcycle:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=nth=' + repeatcycle] )
        return ipv6

    def setTimeFilter(self,number,timefilt="00:00:01d 00:00:00,mon,tue,wed,thu,fri,sat,sun"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=time=' + timefilt] )
        return ipv6

    def setTimeMangle(self, number, timefilt="00:00:01d 00:00:00,mon,tue,wed,thu,fri,sat,sun"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=time=' + timefilt] )
        return ipv6

    def setTimeRaw(self, number, timefilt="00:00:01d 00:00:00,mon,tue,wed,thu,fri,sat,sun"):
        """
        Method will limit rule for specific time
        :param number:
        :param timefilt:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=time=' + timefilt] )
        return ipv6

    def setHeaderFilter(self,number,header="!frag:exact"):
        """
        Methodwill set header
        :param number:
        :param header: proto,none,esp,ah,frag,route,dst,hop:exact,contains ! to invert
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=headers=' + header] )
        return ipv6

    def setHeaderFilterMangle(self, number, header="!frag:exact"):
        """
        Methodwill set header
        :param number:
        :param header: proto,none,esp,ah,frag,route,dst,hop:exact,contains ! to invert
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=headers=' + header] )
        return ipv6

    def setHeaderRaw(self, number, header="!frag:exact"):
        """
        Methodwill set header
        :param number:
        :param header: proto,none,esp,ah,frag,route,dst,hop:exact,contains ! to invert
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=headers=' + header] )
        return ipv6

    def setHopLimitFilter(self,number,filt="equal/0"):
        """
        Method will set filter
        :param number:
        :param filt: equal,greater-than,less-than,not-equal
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/filter/set', '=numbers=' + number, '=hop-limit=' + filt] )
        return ipv6

    def setHopLimitMangle(self, number, filt="equal/0"):
        """
        Method will set filter
        :param number:
        :param filt: equal,greater-than,less-than,not-equal
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/mangle/set', '=numbers=' + number, '=hop-limit=' + filt] )
        return ipv6

    def setHopLimitRaw(self, number, filt="equal/0"):
        """
        Method will set filter
        :param number:
        :param filt: equal,greater-than,less-than,not-equal
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/firewall/raw/set', '=numbers=' + number, '=hop-limit=' + filt] )
        return ipv6