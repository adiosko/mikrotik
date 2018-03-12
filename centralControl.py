import sys, posix, time, binascii, socket, select
import pexpect
import os
import scp
import Constructors
import LoginManager




class centralControl:
    """ Class representing Microtic """

    def __init__(self, login):
        # self.host = hostIP
        self.username = login
        self.credentials = {
            "192.168.1.1": "admin",
            "192.168.2.1": ""
        }

    def listMikrotikDevices(self):
        """
        method to list all mikrotik devices (near) using the os.system
        :return: list of mikrotik devices (mac addresses)
        """
        deviceList = []
        loadAddress = False
        os.system("mactelnet -l -t 20 2>&1 > mt.output")
        with open( "mt.output", "r" ) as file:
            for line in file:
                if loadAddress:
                   address = line.split( )[0]
                   deviceList.append( address )
                else:
                    header = line.split( )
                    if len( header ) > 1:
                        if "IP" in header[0]:
                            loadAddress = True
            for i in deviceList:
                print(i)
        return deviceList

    def addCredentials(self, login="admin"):
        """
        :param login:
        :return:
        """
        server_list = self.listMikrotikDevices()
        print( server_list )
        for server in server_list:
            try:
                password = self.credentials[server]
            except KeyError:
                password = input( "Please eneter the password for " + server + ":" )
                self.credentials[server] = password
        return server_list

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
        for server in self.credentials:
            try:
                # self.login = login
                # self.password = password
                connect = pxssh.pxssh( )
                server = self.credentials
                login = 'admin'
                password = self.credentials[server]
                port = 22
                connect.login( server, login, password )
                commands = pxssh.spawn( )
                time.sleep( 10 )
            except pxssh.ExceptionPxssh as e:
                print( "Error" )
                print( str( e ) )
