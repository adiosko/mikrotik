from tikapy import TikapyClient
from tikapy import TikapySslClient

class BwServer:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listBwTestSettings(self):
        """
        Method will list all BW settings
        :return: list
        """
        bwt = self.client.talk(['/tool/bandwidth-server/print'])
        if bwt == {}:
            print("Nothing to show or api is not showing output")
        else:
            for i in bwt:
                print(bwt)
        return  bwt

    def enableBwServer(self,allocateUdpPorts,maxSessions):
        """
        Method will set BW server
        :param allocateUdpPorts: number of allowed upd ports f.e 2000
        :param maxSessions: max session setup f.e 100
        :return: list
        """
        bws = self.client.talk(['/tool/bandwidth-server/set','=enabled=yes','=authenticate=yes',
                                '=allocate-udp-ports-from='+allocateUdpPorts,'=max-sessions='+maxSessions])
        return bws

    def disableBwServer(self):
        """
        Method will disable bw server
        :return: list
        """
        bws = self.client.talk(['/tool/bandwidth-server/set','=enabled=no'])
        return bws

    def disableAuthenticationOfBwServer(self):
        """
        Method will disbale authentication of bw server
        :return: list
        """
        bws = self.client.talk(['/tool/bandwidth-server/set','=authenticate=no'])
        return bws

    def enableAuthenticationOfBwServer(self):
        """
        Method will enable authentication of bw server
        :return: list
        """
        bws = self.client.talk( ['/tool/bandwidth-server/set', '=authenticate=yes'] )
        return bws

    def listBwServerSession(self):
        """
        Method will list all BW sessions
        :return: list
        """
        bwc = self.client.talk(['/tool/bandwidth-server/session/print'])
        if bwc == {}:
            print("No seesion available")
        else:
            for i in bwc:
                print(bwc)
        return bwc

    def removeSession(self,name):
        """
        Method will remove BW session by name
        :param name: name to remove
        :return: list
        """
        bwc = self.client.talk(['/tool/bandwidth-server/session/remove','=numbers='+name])
        return bwc