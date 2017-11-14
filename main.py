#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import socket
import Interfaces
import Users

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)

#objects
interface = Interfaces.InterfaceManager('192.168.1.1')
users = Users.Users("192.168.1.1")
#users.addUser("adrian","adrian","no","full")
#users.addUser("test","test","yes","read")
#users.listUsers()
#users.changeUserPassword("adrian","adrian1")
#users.changeUserGroup("adrian","read")
#print("\n")
#users.listUsers()
#print("\n")
#users.disableUser("adrian","yes")
#users.listUsers()
#users.enableSystemUser("adrian","no")
#users.listUsers()
#print("\n")
#users.deleteUser("adrian")
#users.deleteUser("adrian1")



