from tikapy import TikapyClient
from tikapy import TikapySslClient

class Resources:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def systemInfoPrint(self):
        """
        Method will list system resource info
        :return:  list
        """
        resource = self.client.talk(["/system/resource/print"])
        print(resource)
        return resource

    def listCPUInfo(self):
        """
        Method will list CPU info
        :return:
        """
        cpu = self.client.talk(["/system/resource/cpu/print"])
        print("CPU\t\t\t\tload\tIRQ\tdisk")
        for i in cpu:
            print(cpu[i]['cpu']+"\t\t\t\t"+cpu[i]['load']+"\t"+cpu[i]['irq']+"\t"+cpu[i]['disk'])
        return cpu

    def listIRQ(self):
        """
        Method will list all IRQ modules
        :return: list
        """
        irq = self.client.talk(['/system/resource/irq/print'])
        print("IRQ\tUSers\t\t\t\tcpu\tactive-cpu\tcount")
        for i in irq:
            print(irq[i]['irq']+"\t"+irq[i]['users']+"\t\t\t\t"+irq[i]['cpu']+"\t"+irq[i]['active-cpu']+"\t"+irq[i]
            ['per-cpu-count'])
        return irq

    def setIRQ(self,orderNo):
        """
        Method will setup auto method for cpu
        :param orderNo: numbe ron list
        :return: list
        """
        irq = self.client.talk(['/system/resource/irq/set','=numbers='+orderNo,'=cpu=auto'])
        return irq

    def listPCIslots(self):
        """
        Method will list PCI slots
        :return: list
        """
        pci = self.client.talk(['/system/resource/pci/print'])
        print("Device\tVendor\t\t\t\tName\tIRQ")
        for i in pci:
            print(pci[i]['device']+"\t"+pci[i]['vendor']+"\t\t\t\t"+pci[i]['name']+"\t"+pci[i]['irq'])
        return pci

    def UsbPowerReset(self,bus,slot):
        """
        Method will usb power reset the module
        :param bus: bus slot
        :param slot: slot name
        :return: list
        """
        pci = self.client.talk(['/system/resource/pci/usb-power-reset','=slot='+slot,'=bus='+bus])
        return pci

    def listUSBDevices(self):
        """
        Method will list usb devices
        :return: list
        """
        usb = self.client.talk(['/system/resource/usb/print'])
        print(usb)
        return usb

    def setUSB(self,oldName, newName):
        """
        Method will setup USB speed
        :param name: name of USB (hostname)
        :return:
        """
        usb = self.client.talk(['/system/resource/usb/set','=numbers='+oldName,'=name='+newName])
        return usb

    def monitorResources(self):
        """
        Method will monitor device
        :return: list
        """
        mon = self.client.talk(['/system/resource/monitor'])
        print(mon)
        return mon