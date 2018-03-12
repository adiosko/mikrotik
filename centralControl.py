import sys, posix, time, binascii, socket, select
import pexpect
import os
import scp
import Constructors

class centralControl:
    """ Class representing Microtic """

    def __init__(self, login,password):
        # self.host = hostIP
        self.username = login
        self.pwd = password

    def listMikrotikDevices(self):
        """
        method to list all mikrotik devices (near) using the os.system
        :return: list of mikrotik devices (mac addresses)
        """
        deviceList = []
        loadAddress = False
        os.system("mactelnet -l -t 20 2>&1 > mt.output")
        with open( "ip.output", "r" ) as file:
            for line in file:
                if loadAddress:
                   ipAddress = line.split( )[0]
                   deviceList.append( ipAddress )
                else:
                    header = line.split( )
                    if len( header ) > 1:
                        if "IP" in header[0]:
                            loadAddress = True
        return deviceList

