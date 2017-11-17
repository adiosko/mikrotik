#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import Interfaces, Users, Services, Files, PackageManager, SystemMaintenance

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)
address = "172.16.129.2"

#objects
interface = Interfaces.InterfaceManager(address,username,password)
users = Users.Users(address,username,password)
services = Services.Services(address,username,password)
filesmanager = Files.Files(address,username,password)
packages = PackageManager.PackageManager(address,username,password)
system = SystemMaintenance.SystemMaintenance(address,username,password)

#calling methods
#packages.unschedulePackageDisable("ipv6")
#system.shutdownRouter()






