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
address = "172.16.129.2"

#objects
interface = Interfaces.InterfaceManager(address)
users = Users.Users(address)
services = Services.Services(address)
filesmanager = Files.Files(address)

filesmanager.backupRouter()
filesmanager.listFiles()







