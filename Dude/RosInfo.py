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

    def addAddress(self):
        """Not colable to API"""
        pass

    def setAddress(self):
        """Teoretical just"""
        pass

