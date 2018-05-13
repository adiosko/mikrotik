from tikapy import TikapyClient
from tikapy import TikapySslClient

class MacServer:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enableMAcPingServer(self):
        """
        Method will enable mac ping server
        :return:
        """
        mac = self.client.talk(['/tool/mac-server/ping/set','=enabled=yes'])
        return mac

    def disableMacPingServer(self):
        """
        Method will disable mac ping server
        :return:
        """
        mac = self.client.talk( ['/tool/mac-server/ping/set', '=enabled=no'] )
        return mac

    def listMactelnetServer(self):
        """
        Method will list all mac servers
        :return:  list
        """
        mac = self.client.talk(['/tool/mac-server/print'])
        if mac == {}:
            print("No mac server found")
        else:
            print("Interface")
            for i in mac:
                print(mac[i]['interface'])
        return  mac

    def addMactelnetServer(self,interface):
        """
        Method will add interface to mactelnet server
        :param interface: all or specific interface
        :return: list
        """
        mac = self.client.talk(['/tool/mac-server/add','=interface='+interface])
        return mac

    def removeMacTelnetServer(self,number):
        """
        Method will remove mac telnet server
        :param number: number of server to remove
        :return:
        """
        mac = self.client.talk(['/tool/mac-server/remove','=numbers='+number])
        return mac

    def enableMactelnetServer(self,number):
        """
        Method will enable mac telnet server
        :param number: number of server to enable
        :return:
        """
        mac = self.client.talk(['/tool/mac-server/enable','=numbers='+number])
        return mac

    def disableMactelnetServer(self,number):
        """
        Method will disable mac telnet server
        :param number: list
        :return:
        """
        mac = self.client.talk(['/tool/mac-server/disable','=numbers='+number])
        return mac

    def listWinboxInterfaces(self):
        """
        Method will list all winbox interfaces
        :return: list
        """
        winbox = self.client.talk(['/tool/mac-server/mac-winbox/print'])
        if winbox == {}:
            print("No interface found")
        else:
            print("Interface")
            for i in winbox:
                print(winbox[i]['interface'])
        return winbox

    def addWinboxInterface(self,interface):
        """
        Method will add winbox interface
        :param interface: interface to add to be accessible via winbox
        :return: list
        """
        winbox = self.client.talk(['/tool/mac-server/mac-winbox/add','=interface='+interface])
        return winbox

    def removeWinboxInterface(self,number):
        """
        Method will remove winbox interface
        :param number: interafce to remove
        :return:
        """
        winbox = self.client.talk(['/tool/mac-server/mac-winbox/remove','=numbers='+number])
        return winbox

    def enableWinboxInterface(self,number):
        """
        Method will enable winbox interface
        :param number: interface to enable
        :return: list
        """
        winbox = self.client.talk(['/tool/mac-server/mac-winbox/enable','=numbers='+number])
        return winbox

    def disableWinboxInterface(self,number):
        """
        Method will disable winbox interface
        :param number: interafce to disable
        :return:
        """
        winbox = self.client.talk( ['/tool/mac-server/mac-winbox/disable', '=numbers=' + number] )
        return winbox

    def listActiveSessions(self):
        """
        Method will list all active sessions
        :return:
        """
        session = self.client.talk(['/tool/mac-server/sessions/print'])
        if session == {}:
            print("No session found")
        else:
            print(session)
        return session