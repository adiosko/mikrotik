from tikapy import TikapyClient
from tikapy import TikapySslClient

class LCD:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listLCD(self):
        """
        Method will list LCD not applicable by API
        :return: list
        """
        LCD = self.client.talk(['/system/lcd/print'])
        print(LCD)
        return LCD

    def setLCD(self,enabled,type,port,contrast):
        """
        Method will setup LCD of mikrotik
        :param enabled: enable status yes or no
        :param type: 24x4, 24x2,
        :param port: parallel
        :param contrast: 0
        :return: list
        """
        LCD = self.client.talk(['/system/lcd/set','=port='+port,'=enabled='+enabled,'=type='+type,'=contrast='+contrast
                                ])
        return LCD

    def listLCDProperties(self):
        prop = self.client.talk(["/system/lcd/page/print"])
        print("display-time\tdescription")
        for i in prop:
            print(prop[i]['display-time']+"\t"+prop[i]['description'])
        return prop

    def enableProperty(self,props):
        """
        Method will enable property on LCD
        :param property: bits, ether1, identity, packets, resources, time, uptime, version
        :return: list
        """
        prop = self.client.talk(["/system/lcd/page/enable","=numbers="+props])
        return prop

    def disableLCDProperty(self,props):
        """
        Method will disable LCD property by its name
        :param props:  LCD property you wanna disable
        :return:  list of response
        """
        prop = self.client.talk( ["/system/lcd/page/disable", "=numbers=" + props] )
        return prop



