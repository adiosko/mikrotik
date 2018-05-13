from tikapy import TikapyClient
from tikapy import TikapySslClient

class Devices:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listDudeDevices(self):
        """
        Method will list all dude devices
        :return:  list
        """
        dev = self.client.talk(['/dude/device/print'])
        if dev == {}:
            print("No dude device found")
        else:
            print("Name")
            for i in dev:
                print(dev[i]['name'])
        return dev

    def addDudeDevice(self,name):
        """
        Method will add device to Dude by its name
        :param name:  name of the device u wanna add
        :return:  list
        """
        dev = self.client.talk(['/dude/device/add','=name='+name])
        return dev

    def setDudeDevice(self,orderNoOfDevice,name):
        """
        Method will rename DUde device
        :param orderNoOfDevice: order Number of device
        :param name: new name of device
        :return: list
        """
        dev = self.client.talk(['/dude/device/set','=numbers='+orderNoOfDevice,'=name='+name])
        return dev

    def removeDevice(self,deviceNumber):
        """
        Method will remove device by its number
        :param deviceNumber: number of device to remove (from bottom 0 to up)
        :return:  list
        """
        dev = self.client.talk(['/dude/device/remove','=numbers='+deviceNumber])
        return dev

    def listDeviceTypes(self):
        """
        Method will list all device types
        :return: list
        """
        dev = self.client.talk(['/dude/device-type/print'])
        if dev == {}:
            print("No device type found")
        else:
            print("Name")
            for i in dev:
                print(dev[i]['name'])
        return dev

    def addDeviceType(self,name):
        """
        Method will add new device type
        :param name: name of new type of device
        :param image: image name: none or list of images or custom image
        :param scale: number (1-N)
        :param url: url of image
        :param requested: cpu,dik,dns,ftp, gother, hp jedirect, http, imap4, memory, mikrotik, netbios, nntp, ping, pop3,
        printer, radius, rnd 50:50, router, routeros-management, smt, ssh, switch, tcp-echo, telnet, time, virtual-memory,
        windows
        :param allowed:cpu,dik,dns,ftp, gother, hp jedirect, http, imap4, memory, mikrotik, netbios, nntp, ping, pop3,
        printer, radius, rnd 50:50, router, routeros-management, smt, ssh, switch, tcp-echo, telnet, time, virtual-memory,
        windows
        :param ignored:cpu,dik,dns,ftp, gother, hp jedirect, http, imap4, memory, mikrotik, netbios, nntp, ping, pop3,
        printer, radius, rnd 50:50, router, routeros-management, smt, ssh, switch, tcp-echo, telnet, time, virtual-memory,
        windows
        :return: list
        """
        dev = self.client.talk(['/dude/device-type/add','=name='+name])
        return dev

    def removeDeviceType(self,name):
        """
        Method will remove device by its name
        :param name: name of  device type to remove
        :return: list
        """
        dev = self.client.talk(['/dude/device-type/remove','=numbers='+name])
        return dev

    def setDudeDeviceType(self, orderNoOfDevice, name):
        """
        Method will rename DUde device-type
        :param orderNoOfDevice: order Number of device
        :param name: new name of device
        :return: list
        """
        dev = self.client.talk( ['/dude/device-type/set', '=numbers=' + orderNoOfDevice, '=name=' + name] )
        return dev

    def listDeviceGroup(self):
        """
        Method will list device groups, not aplicable via api
        :return: list
        """
        pass

    def listMACMapping(self):
        """
        Method will list all mac mapping, not aplicable via api
        :return: list
        """
        pass









