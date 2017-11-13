#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import socket
import Interfaces

login = LoginManager.LoginManager('admin','admin')
username = "admin"
password = 'admin'
interface = Interfaces.InterfaceManager('172.16.49.2')
interface.listInterfaces()
print("\n")
#interface.listEthernetInterfaces()
interface.listBridgeInterfaces()

#login.mactelnetLoginToSingleDevice('admin','admin')

