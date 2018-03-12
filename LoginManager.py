import sys, posix, time, binascii, socket, select
import pexpect
import os
import scp
from centralControl import centralControl

credentials = {
    "192.168.26.5" : "jozo1",
    "192.175.16.15" : "jozo2"
}

class LoginManager:
    """ Class representing Microtic """

    def __init__(self, login,password):
        # self.host = hostIP
        self.username = login
        self.pwd = password

    # telnet na mikrotik
    def loginTelnet(self, password, login="admin"):
        """
        Function to login to mikrotik via telnet
        :param login:
        :param password:
        :return:
        """
        import telnetlib
        central = centralControl(login, password)
        server_list = central.listMikrotikDevices()
        print(server_list)
        for server in server_list:
            try:
                #host = '172.16.49.2'
                #port = 23
                telnetcon = telnetlib.Telnet( host=server, port=23 )
                #telnetcon = telnetlib.Telnet( server )
                # user input
                telnetcon.read_until( b"Login: " )
                telnetcon.write( login.encode( ) + "\n" )
                # user password
                telnetcon.read_until( b"Password: " )
                telnetcon.write( password.encode( ) + b"\n" )
                time.sleep( 10 )
                telnetcon.close( )
                '''
                telnetcon.read_until()
                telnetcon.read_all('Please press "Enter" to continue!'+"\n")
                telnetcon.write('\013')
                telnetcon.read_all('/ip address print')
                '''
            except:
                print( "Cannot connect to router via telnet" )

    # metoda na prihlasenie pomocou SSH
    def loginSSH(self, server,login, password):
        """
        method to login to mikrotik device via SSH with username and password using the library pxssh
        :param server: server to conenct
        :param login: username on mikrotik
        :param password: password of user
        :return: connection to mikrotik or exception
        """
        from pexpect import pxssh, spawn, expect
        import getpass
        try:
            # self.login = login
            # self.password = password
            connect = pxssh.pxssh( )
            server = '172.16.49.2'
            login = 'admin'
            password = 'admin'
            port = 22
            connect.login( server, login, password )
            commands = pxssh.spawn( )
            time.sleep( 10 )
        except pxssh.ExceptionPxssh as e:
            print( "Error" )
            print( str( e ) )


# router = RouterOS('172.16.49.2', 'admin', 'admin')
# router.loginTelnet('admin','admin')


# os.system("mactelnet -l -t 50 > mt.output 2>&1")
# zoznam devicov

    def listMikrotikDevices(self):
        """
        method to list all mikrotik devices (near) using the os.system
        :return: list of mikrotik devices (mac addresses)
        """
        deviceList = []
        loadMacAddress = False
        os.system("mactelnet -l -t 20 2>&1 > mt.output")
        with open( "mt.output", "r" ) as file:
            for line in file:
                if loadMacAddress:
                   macAddress = line.split( )[1]
                   deviceList.append( macAddress )
                else:
                    header = line.split( )
                    if len( header ) > 1:
                        if "IP" in header[0] and "MAC-Address" in header[1]:
                            loadMacAddress = True
        return deviceList


    def mactelnetLoginToSingleDevice(self, username, password, address=None):
        """
        Method to login to device via mactelnet using username and password and using macaddress of previous method
        :param username: username on mikrotik
        :param password: password of user
        :param address: mac address of mikrotik
        :return:
        """
        deviceList = self.listMikrotikDevices()
        print( deviceList )
        if address:
            print('mactelnet {} -u {} -p {}'.format( address, username, password ))
            os.system( 'mactelnet {} -u {} -p {}'.format( address, username, password ) )
        elif deviceList:
            print( 'mactelnet {} -u {} -p {}'.format( deviceList[0], username, password ) )
            os.system( 'mactelnet {} -u {} -p {}'.format( deviceList[0], username, password ) )
        else:
            print("No device was found")
