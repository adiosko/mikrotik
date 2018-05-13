from tikapy import TikapyClient
from tikapy import TikapySslClient

class RoMon:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setSecrets(self,secret):
        """
        Method will set romon secrte
        :param secret: password to romon
        :return:
        """
        romon = self.client.talk(['/tool/romon/set','=secrets='+secret,'=enabled=yes'])
        return romon

    def setId(self,ID):
        """
        Method will enable romon mode with id MAC address
        :param ID: mac address
        :return:
        """
        romon = self.client.talk( ['/tool/romon/set', '=secrets=' + ID, '=enabled=yes'] )
        return romon

    def disableRomon(self):
        """
        Method will disable romon mode
        :return:
        """
        romon = self.client.talk(['/tool/romon/set','=enabled=no'])
        return romon

    def listRomon(self):
        """
        Method will list romon settings
        :return:
        """
        romon = self.client.talk(['/tool/romon/print'])
        print(romon)
        return romon

    def listRomonPorts(self):
        """
        Method will list romon ports
        :return:
        """
        romon = self.client.talk(['/tool/romon/port/print'])
        if romon == {}:
            print("No romon port set")
        else:
            print("Interface\tforbid\tcost")
            for i in romon:
                print(romon[i]['interface']+"\t"+romon[i]['forbid']+"\t"+romon[i]['cost'])
        return romon

    def addRomonPort(self,interface,forbid,cost):
        """
        Method will set romon port
        :param interface: interface to set
        :param forbid: def no otherwise yes
        :param cost: 100 def
        :param secret: optional
        :return:
        """
        romon = self.client.talk(['/tool/romon/port/add','=interface='+interface,'=forbid='+forbid
                                  ,'=cost='+cost])
        return romon

    def addRomonPortWithPassword(self,interface,forbid,cost,password):
        """
        Method will add romon port with password
        :param interface: interface to set
        :param forbid: yes/no
        :param cost: cost of port
        :param password: password
        :return:
        """
        romon = self.client.talk(['/tool/romon/port/add', '=interface=' + interface, '=forbid=' + forbid, '=cost=' + cost
                , '=secret=' + password] )
        return romon

    def removeRomonPort(self,number):
        """
        Method will remove romon port
        :param number: mum,ber of port
        :return:
        """
        romon = self.client.talk(['/tool/romon/port/remove','=numbers='+number])
        return romon

    def enableRomonPort(self,number):
        """
        Method will enable romon port
        :param number: number of romon port
        :return:
        """
        romon = self.client.talk(['/tool/romon/port/enable','=numbers='+number])
        return romon

    def disableROmonPort(self,number):
        """
        Method will disable romon port
        :param number: numbe rof port in use
        :return:
        """
        romon = self.client.talk( ['/tool/romon/port/disable', '=numbers=' + number] )
        return romon

    def commentPortSetup(self,number,comment):
        """
        Method will comment romon port config
        :param number: number in order
        :param comment: comment
        :return:
        """
        romon = self.client.talk(['/tool/romon/port/comment','=numbers='+number,'=comment='+comment])
        return romon

    def listRomonDiscoveryDevices(self,duration):
        """
        To run this method romon must be running
        :param duration: length of discovery
        :return:
        """
        romon = self.client.talk(['/tool/romon/discover','=duration='+duration])
        if romon == {}:
            print("No romon device found")
        else:
            print(romon)
        return romon

    def romonMacPing(self,ID,packetSize,intervalInMilis,count):
        """
        Method will use macping to verify connectivity of device
        :param ID: mac address of device
        :param packetSize: packet size normaly 32 b
        :param intervalInMilis: normally 1000 ms
        :param count: number of packets
        :return:
        """
        romon = self.client.talk(['/tool/romon/ping','=id='+ID,'=size='+packetSize,'=interval='+intervalInMilis
                                  ,'=count='+count])
        return romon

