from tikapy import TikapyClient
from tikapy import TikapySslClient

class PingSpeed:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def pingSpeedTest(self,dst,smallPacketSize,bigPacketSize,count):
        """
        Method will test ping test
        :param dst: srv to ping
        :param smallPacketSize:  min 32 b
        :param bigPacketSize: max 1500
        :return:
        """
        ping = self.client.talk(['/tool/ping-speed','=address='+dst,'first-ping-size='+smallPacketSize,
                                 '=second-ping-size='+bigPacketSize,'=count='+count])
        return ping