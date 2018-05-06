from tikapy import TikapyClient
from tikapy import TikapySslClient

class DhcpServer:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listDhcp(self):
        """
        Method will list dhcp
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/print'])
        if ipv4 == {}:
            print("No dhcp server found")
        else:
            print("Name\tInterface\tLease Time\tAddress pool")
            for i in ipv4:
                print(ipv4[i]['name']+"\t"+ipv4[i]['interface']+"\t"+ipv4[i]['lease-time']+"\t"+ipv4[i]['address-pool'])
        return ipv4

    def addDhcp(self,interface):
        """
        Method will add dhcp
        :param interface:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/add','=interface='+interface])
        return ipv4

    def removeDhcp(self,name):
        """
        Method will remove dhcp server
        :param name:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/remove','=numbers='+name])
        return ipv4

    def enableDhcp(self,name):
        """
        Method will enable dhcp
        :param name:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/enable', '=numbers=' + name] )
        return ipv4

    def disableDhcp(self, name):
        """
        Method will enable dhcp
        :param name:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/disable', '=numbers=' + name] )
        return ipv4

    #dhcp config
    def setLeaseTime(self,lease="00:05:00"):
        """
        Method will set
        :param lease:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/config/set','=store-leases-disk='+lease])
        return ipv4

    #netwrok
    def listNetwork(self):
        """
        Method will list networks
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/network/print'])
        if ipv4 == {}:
            print("No network found")
        else:
            print("Address\tGateway\tDNS")
            for i in ipv4:
                print(ipv4[i]['address']+"\t"+ipv4[i]['gateway']+"\t"+ipv4[i]['dns-server'])
        return ipv4

    def addNetwork(self,network):
        """
        Method will add network
        :param network:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/network/add','=address='+network])
        return ipv4

    def removeNetwork(self,number):
        """
        Method will remove network
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/network/remove','=numbers='+number])
        return ipv4

    def commentNetwrok(self,number,comment):
        """
        Method will comment network
        :param number:
        :param comment:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv4

    def setAddress(self,number,address):
        """
        Method will set address
        :param number:
        :param address:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=address=' + address] )
        return ipv4

    def setGateway(self,number,gw):
        """
        Method will set gw
        :param number:
        :param gw:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=gateway=' + gw] )
        return ipv4

    def setNetmask(self,number,mask):
        """
        Method will set netmask
        :param number:
        :param mask: 32 but amx
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=netmask=' + mask] )
        return ipv4

    def setDns(self,number,dns):
        """
        Method will set dns
        :param number:
        :param dns:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=dns-server=' + dns] )
        return ipv4

    def setDomain(self,number,domain):
        """
        Method will set domain
        :param number:
        :param domain:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=domain=' + domain] )
        return ipv4

    def setWinsServer(self,number,wins):
        """
        Method will set wins server
        :param number:
        :param wins: IP of wins server
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=wins-server=' + wins] )
        return ipv4

    def setNtpServer(self,number,ntp):
        """
        Method will set ntp server
        :param number:
        :param ntp:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=ntp-server=' + ntp] )
        return ipv4

    def setCapsIp(self,number,ip):
        """
        Method will set capsman ip
        :param number:
        :param ip:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=caps-manager=' + ip] )
        return ipv4

    def setNextServer(self,number,server):
        """
        Method will set next server
        :param number:
        :param server:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=next-server=' + server] )
        return ipv4

    def setBootFileName(self,number,name):
        """
        Method willset boot file name
        :param number:
        :param name:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=boot-file-name=' + name] )
        return ipv4

    def setDhcpOptions(self,number,option):
        """
        Method will set dhcp options
        :param number:
        :param option: code of option
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=dhcp-option=' + option] )
        return ipv4

    def setDhcpOptionSet(self,number,setof):
        """
        Method will set set of options
        :param number:
        :param setof: set of dhcp options
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/network/set', '=numbers=' + number, '=dhcp-option-set=' + setof] )
        return ipv4

    #Leases
    def listLeases(self):
        """
        Method will list leases
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/print'])
        return ipv4

    def addLease(self,address,mac,server):
        """
        Method will add lease
        :param cid: client id == IP address
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/add','=address='+address,'=mac-address='+mac,'=server='+server])
        return ipv4

    def removeLease(self,number):
        """
        Method will remove lease
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/remove','=numbers='+number])
        return ipv4

    def enableLease(self,number):
        """

        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/enable', '=numbers=' + number] )
        return ipv4

    def disableLease(self,number):
        """

        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/disable', '=numbers=' + number] )
        return ipv4

    def commentLease(self,number,comment):
        """
        Method will comment lease
        :param number:
        :param comment:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv4

    def checkStatus(self,number):
        """
        Method will check status
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/check-status','=numbers='+number])
        return ipv4

    def setLeaseAddress(self,number,address):
        """
        Method will set lease address
        :param number:
        :param address:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/set','=numbers='+number,'=address='+address])
        return ipv4

    def setLeaseMac(self,number,mac):
        """
        Method will set lease mac address
        :param number:
        :param mac:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number,'=mac-address='+mac] )
        return ipv4

    def useSrcMac(self,number):
        """
        Method will enable src mac address
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/set','=numbers='+number,'=use-src-mac=yes'])
        return ipv4

    def setCLientId(self,number,ID):
        """
        Method will set client id
        :param number:
        :param id:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=client-id=' + ID] )
        return ipv4

    def setLeaseServer(self,number,server="all"):
        """
        Method will set lease server
        :param number:
        :param server: all or specific dhcp server
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=server=' + server] )
        return ipv4

    def setLeaseTimes(self,number,time):
        """
        Method will set lease time
        :param number:
        :param time:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=lease-time=' + time] )
        return ipv4

    def blockAccess(self,number):
        """
        Method will block access for specific one
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=block-access=yes'] )
        return ipv4

    def alwaysBroadcast(self,number):
        """
        Method will always broadcast address
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=always-broadcast=yes'] )
        return ipv4

    def setLeaseDhcpOptions(self,number,options):
        """
        Method will set dhcp options
        :param number:
        :param options: generated in options
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=dhcp-option='+options] )
        return ipv4

    def setLeaseOptionsSet(self,number,options):
        """
        Method will set options set
        :param number:
        :param options:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=dhcp-option-set=' + options] )
        return ipv4

    def setRateLimit(self,number,limit):
        """
        Method will set rate limit
        :param number:
        :param limit: limit in kbps
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=rate-limit=' + limit] )
        return ipv4

    def setInserQueue(self,number,queue="first"):
        """
        Method will insert queue
        :param number:
        :param queue: first or bottom
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=insert-queue-before=' + queue] )
        return ipv4

    def setAddressList(self,number,adrlist):
        """
        Method will set address list
        :param number:
        :param adrlist: address list
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/lease/set', '=numbers=' + number, '=address-lists=' + adrlist] )
        return ipv4

    def makeStatic(self,number):
        ipv4 = self.client.talk(['/ip/dhcp-server/lease/make-static','=numbers='+number])
        return ipv4

    #options
    def listOptions(self):
        """
        Method will list options
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/print'])
        if ipv4 == {}:
            print("No option found")
        else:
            print("Name\toption\tvalue")
            for i in ipv4:
                print(ipv4[i]['name']+"\t"+ipv4[i]['code']+"\t"+ipv4[i]['value'])
        return ipv4

    def addOption(self,name,option):
        """
        Method will add option by name
        :param name:
        :param option: option number
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/add','=name='+name,'=code='+option])
        return ipv4

    def removeOption(self,name):
        """
        Method will remove option
        :param name:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/remove','=numbers='+name])
        return ipv4

    def setOptionName(self,name,newName):
        """
        Method will set new option name
        :param name:
        :param newName:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/option/set', '=numbers=' + name,'=name='+newName] )
        return ipv4

    def setOptionCode(self,name,code):
        """
        Method will set option
        :param name:
        :param code:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/option/set', '=numbers=' + name, '=code=' + code] )
        return ipv4

    def setOptionValue(self,name,value):
        """
        Method will set option value
        :param name:
        :param value:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/option/set', '=numbers=' + name, '=value=' + value] )
        return ipv4

    #option set
    def listSets(self):
        """
        Method will list all sets
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/sets/print'])
        if ipv4 == {}:
            print("no option set found")
        else:
            print("Name")
            for i in ipv4:
                print(ipv4[i]['name'])
        return ipv4

    def addOptionSet(self,name,option):
        """
        Method will add option set
        :param name:
        :param option: option1, created in options
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/sets/add','=name='+name,'=options='+option])
        return ipv4

    def removeSet(self,name):
        """
        Method will remove set
        :param name:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/sets/remove','=numbers='+name])
        return ipv4

    def setName(self,name,newName):
        """
        Method will set new name of set
        :param name:
        :param newName:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/option/sets/set','=numbers='+name,'=name='+newName])
        return ipv4

    def setOption(self,name,option):
        """
        Method will set set  option
        :param name:
        :param option:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/option/sets/set', '=numbers=' + name, '=options=' + option] )
        return ipv4

    #Alerts
    def listAlets(self):
        """
        Method will list dhcp alerts
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/alert/print'])
        if ipv4 == {}:
            print("No alert found")
        else:
            print("Interface\tTimeout")
            for i in ipv4:
                print(ipv4[i]['interface']+"\t"+ipv4[i]['alert-timeout'])
        return ipv4

    def addAlert(self,interface):
        """
        Methodwill add alert
        :param interface:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/alert/add','=interface='+interface])
        return ipv4

    def removeAlert(self,number):
        """
        Method will remove alert
        :param number:
        :return:
        """
        ipv4 = self.client.talk(['/ip/dhcp-server/alert/remove','=numbers='+number])
        return ipv4

    def enableAlert(self,number):
        """
        Method will enable alert
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/enable', '=numbers=' + number] )
        return ipv4

    def disableAlert(self, number):
        """
        Method will enable alert
        :param number:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/disable', '=numbers=' + number] )
        return ipv4

    def commentAlert(self,number,comment):
        """
        Method will commment alert
        :param number:
        :param comment:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/comment', '=numbers=' + number,'=comment='+comment] )
        return ipv4

    def setAlertInterface(self,number,iface):
        """
        Method will set alert interface
        :param number:
        :param iface:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/set', '=numbers=' + number, '=interface=' + iface] )
        return ipv4

    def setAlarmValidServer(self,number,server):
        """
        Method will set valid server mac address
        :param number:
        :param server: server amc address
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/set', '=numbers=' + number, '=valid-server=' + server] )
        return ipv4

    def setAlertTimeout(self,number,timeout="01:00:00"):
        """
        Method will set timeout
        :param number:
        :param timeout:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/set', '=numbers=' + number, '=alert-timeout=' + timeout] )
        return ipv4

    def setOnAlertScript(self,number,script):
        """
        Method will set script on alert
        :param number:
        :param script:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/dhcp-server/alert/set', '=numbers=' + number, '=on-alert=' + script] )
        return ipv4