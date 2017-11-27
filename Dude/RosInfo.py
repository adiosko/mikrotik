from tikapy import TikapyClient
from tikapy import TikapySslClient

class RosInfo:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRosResources(self):
        """
        Method will print ros resource info
        :return: list
        """
        ros = self.client.talk(['/dude/ros/resource/print'])
        print(ros)
        return ros

    def listRouterboard(self):
        """
        Method will list routerboard info
        :return: list
        """
        ros = self.client.talk(['/dude/ros/routerboard/print'])
        print(ros)
        return ros

    def listHealthStatus(self):
        """
        Method will list health status of remote device
        :return:
        """
        ros = self.client.talk(['/dude/ros/health/print'])
        print(ros)

    def setHealthDevice(self,device,fanMode,useFan):
        """
        Method will set connected device
        :param device: device name f.e Mikrotik
        :param fanMode: manual/auto
        :param useFan: auxilary/main
        :return: list
        """
        fan = self.client.talk(['/dude/ros/health/set','=numbers='+device,'=device='+device,'=fan-mode='+fanMode,'=use-fan='
                                                                                                                 +useFan])
        return fan

    def listInterfaces(self):
        """
        Method will list all interfaces for Dude
        :return:  list
        """
        iface = self.client.talk(['/dude/ros/interface/print'])
        print(iface)
        return iface

    def setInterface(self,name,mtu,l2mtu,device,disabled):
        """
        Method will set interfaces on Dude
        :param name: name of iface
        :param mtu: auto
        :param l2mtu: l2mtu
        :param device: device name f.e Mikrotik
        :param disabled: yes/no
        :return: list
        """
        iface = self.client.talk(['/dude/ros/interface/set','=numbers='+name,'=mtu='+mtu,'=l2mtu='+l2mtu,
                                  '=device='+device,'=disabled='+disabled])
        return iface

    def listAddresses(self):
        """
        Method will list addresses
        :return: list
        """
        addr = self.client.talk(['/dude/ros/address/print'])
        print(addr)
        return addr

    def addAddress(self,device,address,network,interface):
        """
        Method will add dude address
        :param device: Mikrotik
        :param address: address of device
        :param network: network of device
        :param interface: interface to apply
        :return:
        """
        addr = self.client.talk(['/dude/ros/address/add','=device='+device,'=address='+address,'=network='+network
                                 ,'=interface='+interface])
        return addr

    def setAddress(self,number,device,address,network,interface):
        """
        Method will set Address which exists
        :param number: order no
        :param device: device name f.re Mikrotik
        :param address: address of device
        :param network: network of device
        :param interface: interface of device
        :return: list
        """
        addr = self.client.talk(['/dude/ros/address/set','=numbers='+number, '=device=' + device, '=address=' + address,
                                 '=network=' + network,'=interface=' + interface] )
        return addr

    def removeAddress(self,number):
        """
        Method will remove address by its number
        :param number: number of order
        :return: list
        """
        addr = self.client.talk(['/dude/ros/address/remove','=numbers='+number])
        return addr

    def listArp(self):
        """
        Method will list all arp records
        :return: list
        """
        arp = self.client.talk(['/dude/ros/arp/print'])
        if arp == {}:
            print("Nothing to show")
        else:
            for i in arp:
                print(arp)
        return arp
    def addArp(self,device,IP,MAC,Interface):
        """
        Method will add arp of device
        :param device: device name
        :param IP: IP address
        :param MAC: MAC address
        :param Interface: interface o apply
        :return: list
        """
        arp = self.client.talk(['/dude/ros/arp/add','=device='+device,'=interface='+Interface,'=address='+IP,
                                '=mac-address='+MAC])
        return arp

    def setArp(self,number,device,IP,MAC,Interface):
        """
        Method will set existing arp record
        :param number: number of record to set
        :param device: Mikrotik
        :param IP:IP
        :param MAC:MAC
        :param Interface: Interface to apply
        :return: list
        """
        arp = self.client.talk(['/dude/ros/arp/set','=numbers='+number,'=device='+device,'=interface='+Interface,
                                '=address='+IP,'=mac-address='+MAC])
        return arp

    def removeArpRecord(self,number):
        """
        Method will remove ARP record
        :param number:  number to delete
        :return:  list
        """
        arp = self.client.talk(['/dude/ros/arp/remove','=numbers='+number])
        return arp

    def enableArp(self,number):
        """
        Method will enable arp record
        :param number: numbe rof device
        :return:
        """
        arp = self.client.talk(['/dude/ros/arp/enable','=numbers='+number])
        return arp

    def disableArp(self,number):
        """
        Method will disable arp record
        :param number: list
        :return:list
        """
        arp = self.client.talk(['/dude/ros/arp/disable','=numbers='+number])
        return arp

    def listNeighbors(self):
        """
        Method will list all neighbors
        :return: list
        """
        neg= self.client.talk(['/dude/ros/neighbor/print'])
        if neg == {}:
            print("No neighbor found")
        else:
            for i in neg:
                print(neg)
        return neg

    def setNeighbor(self,number,device):
        """
        Method will set  neighbor
        :param number: number of neighbor
        :param device: device name
        :return: list
        """
        neg = self.client.talk(['/dude/ros/neighbor/set','=numbers='+number,'=device='+device])
        return neg

    def listQueues(self):
        """
        Method will list all Queues
        :return: list
        """
        que = self.client.talk(['/dude/ros/queue/print'])
        if que == {}:
            print("No queue found")
        else:
            for i in que:
                print(que)
        return que

    def addQueue(self,device,target,name):
        """
        Method will add Queue (simple)
        :param device: device to setup  queue
        :param target: list of targets
        :param name: name of rule
        :return: list
        """
        que = self.client.talk(['/dude/ros/queue/add','=name='+name,'=device='+device,'=target='+target])
        return que

    def setQueue(self,name,device,target):
        """
        Method will set existing queue by name
        :param name: name of queue
        :param device: dev name
        :param target: target to
        :return: list
        """
        que = self.client.talk(['/dude/ros/queue/set','=numbers='+name,'=device='+device,'=target='+target])
        return que

    def removeQueue(self,name):
        """
        Method will remove queue by name
        :param name: name to remove
        :return: list
        """
        que = self.client.talk(['/dude/ros/queue/remove','=numbers='+name])
        return que

    def enableQueue(self,name):
        """
        Method will enable existing rule
        :param name: name to enable
        :return: list
        """
        que = self.client.talk(['/dude/ros/queue/enable','=numbers='+name])
        return que

    def disableQueue(self,name):
        """
        Method will disable existing rule
        :param name: name of rule to disable
        :return:  list
        """
        que = self.client.talk(['/dude/ros/queue/disable','=numbers='+name])
        return que

    def unsetQueue(self,name):
        """
        Method will set queue
        :param name: name of rule
        :return: list
        """
        que = self.client.talk(['/dude/ros/queue/unset','=numbers='+name])
        return que

    def listRoutes(self):
        """
        Method will list all Dude routes
        :return:list
        """
        rtr = self.client.talk(['/dude/ros/route/print'])
        if rtr == {}:
            print("No route found")
        else:
            for i in rtr:
                print(rtr)
        return rtr

    def addRoute(self,device,dst,gw):
        """
        Method will add route to dude
        :param device: device name Mikrotik
        :param dst: dest address/network
        :param gw: ip next hop address
        :return: list
        """
        rtr = self.client.talk(['/dude/ros/route/add','=device='+device,'=dst-address='+dst,'=gateway='+gw])
        return rtr

    def setRoute(self,number,device,dst,gw):
        """
        Method will set existing route
        :param number: number of route
        :param device: device name MIkrotik
        :param dst: dst network
        :param gw: IP
        :return:  list
        """
        rtr = self.client.talk(['/dude/ros/route/set','=numbers='+number,'=device='+device,'=dst-address='+dst,
                                '=gateway='+gw])
        return rtr

    def removeRoute(self,name):
        """
        Method will remove route
        :param name: number of route
        :return: list
        """
        rtr = self.client.talk(['/dude/ros/route/remove','=numbers='+name])
        return rtr

    def unsetRoute(self,name):
        """
        Method will unset existing route
        :param name: name of route
        :return: list
        """
        rtr = self.client.talk(['/dude/ros/route/unset','=numbers='+name])
        return rtr

    def enableRoute(self,name):
        """
        Method will enable disabled route
        :param name: name of route
        :return: list
        """
        rtr = self.client.talk(['/dude/ros/route/enable','=numbers='+name])
        return rtr

    def disableRoute(self,name):
        """
        Method will disable enabled route
        :param name: name
        :return: list
        """
        rtr = self.client.talk(['/dude/ros/route/disable','=numbers='+name])
        return rtr

    def listRegistrationTable(self):
        """
        Method will list wireless registration table
        :return: list
        """
        wifi = self.client.talk(['/dude/ros/registration-table/print'])
        if wifi == {}:
            print("No registration record found")
        else:
            for i in wifi:
                print(wifi)
        return wifi

    def removeRegistrationRecord(self,name):
        """
        Method will remove record from registration table
        :param name: name of record to remove
        :return: list
        """
        wifi = self.client.talk(['/dude/ros/registration-table/remove','=numbers='+name])
        return wifi

    def listDhcpLeases(self):
        """
        Method will list all DHCP leases
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/print'])
        if dhcp == {}:
            print("No lease found")
        else:
            for i in dhcp:
                print(dhcp)
        return dhcp

    def addDhcpRecord(self,device,address,MAC):
        """
        Method will add DHCP lease record
        :param device: device Mikrotik
        :param address: IP
        :param MAC: MAC
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/add','=device='+device,'=address='+address,'=mac-address='+MAC])
        return dhcp

    def setDhcpRecord(self,name,device,address,MAC):
        """
        Method will set existing record
        :param name: name of device
        :param device: device name f.e Mikrotik
        :param address: IP
        :param MAC: MAC
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/set','=numbers='+name,'=device=' + device, '=address=' + address,
                                 '=mac-address=' + MAC] )
        return dhcp

    def unSetDhcpRecord(self,name):
        """
        Method will unset record
        :param name: name of device
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/unset','=numbers='+name])
        return dhcp

    def enableLease(self,name):
        """
        Method will enable rule by name
        :param name: name of lease to enable
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/enable','=numbers='+name])
        return dhcp

    def disableLease(self,name):
        """
        Method will disable current name
        :param name: name to disable
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/disable','=numbers='+name])
        return dhcp

    def removeLeases(self,name):
        """
        Method will remove Leashes from DHCP
        :param name: name to remove
        :return: list
        """
        dhcp = self.client.talk(['/dude/ros/lease/remove','=numbers='+name])
        return dhcp