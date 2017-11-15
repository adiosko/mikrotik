#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import socket
import Interfaces
import Users
import Services
import Files
import pexpect

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)
address = "172.16.49.2"

#objects
interface = Interfaces.InterfaceManager(address)
users = Users.Users(address)
services = Services.Services(address)
filesmaager = Files.Files(address)
#filesmaager.exportConfig("exportCOnfig")
filesmaager.importConfig("exportCOnfig.rsc")
"""
filepath = "/home/adrian/Desktop/Emacs-Cheat-Sheet.pdf"
client = pexpect.spawn( "scp " + filepath + " " + address + ":/files" )
client.expect( username + "@" + address + "s password:" )
client.sendline( password )
#client.expect( pexpect.EOF, timeout=10 )
"""





