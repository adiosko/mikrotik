import LoginManager
import apiList
import tikapy
import socket
import Interfaces

login = LoginManager.LoginManager('admin','admin')
username = "admin"
password = 'admin'
interface = Interfaces.InterfaceManager('172.16.49.2')
interface.listInterfaces()
#login.mactelnetLoginToSingleDevice('admin','admin')

