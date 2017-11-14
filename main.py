#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import socket
import Interfaces
import Users
import Services

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)

#objects
interface = Interfaces.InterfaceManager('192.168.1.1')
users = Users.Users("192.168.1.1")
services = Services.Services("192.168.1.1")
services.enableService("www")
services.listServices()





