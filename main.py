#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import socket
import Interfaces
import Users
import Services
import Files

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)
address = "192.168.1.1"

#objects
interface = Interfaces.InterfaceManager(address)
users = Users.Users(address)
services = Services.Services(address)
filesmaager = Files.Files(address)

services.enableService("www")
services.listServices()





