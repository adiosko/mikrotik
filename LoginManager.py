import sys, posix, time, binascii, socket, select
import pexpect
import os


class LoginManager:
    """ Class representing Microtic """

    def __init__(self, login,password):
        # self.host = hostIP
        self.username = login
        self.pwd = password

    # telnet na mikrotik
    def loginTelnet(self, login, password):
        """
        Function to login to mikrotik via telnet
        :param login:
        :param password:
        :return:
        """
        import telnetlib
        try:
            host = '172.16.49.2'
            port = 23
            telnetcon = telnetlib.Telnet( host, port )
            telnetcon = telnetlib.Telnet( host )
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
    def loginSSH(self, login, password):
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
            connect.logout( )
            '''
            commands.expect('Please press "Enter" to continue!')
            commands.sendline('\013')
            connect.sendline('/ip address print')
            connect.prompt()
            print connect.before
            '''
        except pxssh.ExceptionPxssh as e:
            print( "Error" )
            print( str( e ) )


# router = RouterOS('172.16.49.2', 'admin', 'admin')
# router.loginTelnet('admin','admin')


# os.system("mactelnet -l -t 50 > mt.output 2>&1")
# zoznam devicov

    def listMikrotikDevices(self):
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


def unusedCode(self):
    # username = 'admin'
    #  password = '""'
    # os.system("/interface/print")
    # os.system("/quit")
    # print "test na git"
    pass
