from tikapy import TikapyClient
from tikapy import TikapySslClient

class RouterBoard:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listRouterboard(self):
        """
        Method will list routerboard info
        :return: list
        """
        rtr = self.client.talk(['/system/routerboard/print'])
        print(rtr)
        return rtr

    def upgradeRouterBoard(self):
        """
        Method will upgrade router board
        :return: list
        """
        rtr = self.client.talk(['/system/routerboard/upgrade'])
        return rtr

    def listFanControll(self):
        """
        Method will list fan status
        :return: list
        """
        fan = self.client.talk(['/system/routerboard/fan-control','=state=yes'])
        return fan

    def listBIOS(self):
        """
        Method will list BIOS
        :return: list
        """
        bios = self.client.talk(['/system/routerboard/bios/print'])
        print(bios)
        return bios

    def setBios(self,baud,bootDelay,bootDev,cpu,debug,enter,bootTO, memSet = None, pci = None, vga = None, beep = None):
        """
        Method will setup mikrotik boot process
        :param baud: baud rate  - 115200,1200,19200,2400,38400,4800,57600,9600
        :param beep: beep on boot: yes/no (optional)
        :param bootDelay: boot delay [s]
        :param bootDev: etherboot-only, etherboot-ide, ide-only, try=etherboot-once
        :param cpu: cpuMode power-save/regular
        :param debug: debug level none/high/low
        :param enter: Enter setup on: any-key/delete-key
        :param bootTO: boot Time out: 00:00:00
        :param memSet: memory settings: optimal/fail-safe (optional)
        :param pci: pci backoff (optional)
        :param vga: vga to serial (optional)
        :return: list
        """
        if memSet == None or pci == None or vga == None or beep == None:
            bios =self.client.talk(['/system/routerboard/bios/set','=baud-rate='+baud,'=boot-delay='+bootDelay
                                 ,'=boot-device='+bootDev,'=cpu-mode='+cpu,'=debug-level='+debug,
                                 '=enter-setup-on='+enter,'=enterboot-timeout='+bootTO])
        else:
            bios = self.client.talk(['/system/routerboard/bios/set','=baud-rate='+baud,'=boot-delay='+bootDelay
                                 ,'=boot-device='+bootDev,'=cpu-mode='+cpu,'=debug-level='+debug,
                                 '=enter-setup-on='+enter,'=enterboot-timeout='+bootTO,
                                 '=memory-settings='+memSet,'=pci-backoff='+pci,'=vga-to-serial='+vga
                                 ,'=beep-on-boot='+beep])
        return bios

    def resetBios(self):
        """
        Method will reset BIOS settings
        :return: list
        """
        bios = self.client.talk(['/system/routerboard/bios/reset'])
        print("Reseting bios")
        return bios