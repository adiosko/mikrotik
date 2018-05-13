import pexpect,time
import LoginManager


class basicCOnfig:
    def __init__(self,interface,mac,ip):
        self.interface = interface
        self.mac = mac
        self.ip = ip

    def dhcp(self,username,password):
        child =pexpect.spawn('mactelnet '+self.mac)
        child.expect('Username:')
        child.sendline(username)
        child.expect('Password:')
        child.sendline(password)
        child.sendline('\r')
        try:
            child.expect('> ')
            child.sendline('ip dhcp-client add interface='+self.interface+"\r")
            child.expect('> ')
            child.close()
        except:
            print("error")
            child.close()
        time.sleep(1)

    def setAddress(self,username,password):
        """

        :param username:
        :param password:
        :return:
        """
        child = pexpect.spawn( 'mactelnet ' + self.mac )
        child.expect( 'Username:' )
        child.sendline( username )
        child.expect( 'Password:' )
        child.sendline( password )
        child.sendline( '\r' )
        try:
            child.expect( '> ' )
            child.sendline( 'ip address add address=' + self.ip + " interface="+self.interface+"\r" )
            child.expect( '> ' )
            child.close()
        except:
            print( "error" )
            child.close()
        time.sleep( 1 )





