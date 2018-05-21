from tikapy import TikapyClient
from tikapy import TikapySslClient

class LED:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSystemLEDs(self):
        """
        Method will list all leds status
        :return:list of leds or empty dictionary
        """
        leds = self.client.talk(["/system/leds/print"])
        if leds == {}:
            print("No leds enabled")
        else:
            print(leds)
        return leds

    def addLedTrigger(self,type,interface):
        """
        Method will add LED Triger
        :param type:  ap-cap, interface-activity, interface-speed, interface-status, interface-receive, interface-speed-1G
        interface-transmit, off, wireless-signal-strength,, fan-fault, modem-signal, on, wireless-status, flash-access,
         modem-technology, poe-out
        :param interface: interface on mikrotik
        :return:
        """
        leds = self.client.talk(['/system/leds/add','=type='+type,'=interface='+interface])
        return leds

    def setLedTrigger(self,type,interface):
        """
        Method will edit system led trigger
        :param type: ap-cap, interface-activity, interface-speed, interface-status, interface-receive, interface-speed-1G
        interface-transmit, off, wireless-signal-strength,, fan-fault, modem-signal, on, wireless-status, flash-access,
         modem-technology, poe-out
        :param interface: interface on mikrotik
        :return: list of ifaces
        """
        leds = self.client.talk( ['/system/leds/set', '=type=' + type, '=interface=' + interface] )
        return leds

    def enableTrigger(self,number):
        """
        Method will enable trigger
        :param triggerName: type: ap-cap, interface-activity, interface-speed, interface-status, interface-receive, interface-speed-1G
        interface-transmit, off, wireless-signal-strength,, fan-fault, modem-signal, on, wireless-status, flash-access,
         modem-technology, poe-out
        :return: list of trogers
        """
        leds = self.client.talk(['/system/leds/enable','=numbers='+number])
        return leds

    def disableTrigger(self, number):
        """
        Method will enable trigger
        :param triggerName: type: ap-cap, interface-activity, interface-speed, interface-status, interface-receive, interface-speed-1G
        interface-transmit, off, wireless-signal-strength,, fan-fault, modem-signal, on, wireless-status, flash-access,
         modem-technology, poe-out
        :return: list of trogers
        """
        leds = self.client.talk( ['/system/leds/disable', '=numbers=' + number] )
        return leds

    def removeTrigger(self,number):
        """
        Method will remove trigger
        :param number: number of trigger from list
        :return: list of words
        """
        leds = self.client.talk(['/system/leds/remove','=numbers='+number])
        return leds

    def turnoffLEDS(self,when):
        """
        Method will setup all leds on mikrotik
        :param when: after-1h, after-1m, immediate, never
        :return: list of words response
        """
        leds = self.client.talk(['/system/leds/settings/set','=all-leds-off='+when])
        return leds