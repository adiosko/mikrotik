#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import Interfaces, Users, Services, Files, PackageManager, SystemMaintenance

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)
address = "172.16.129.2"

#objects
interface = Interfaces.InterfaceManager(address)
users = Users.Users(address)
services = Services.Services(address)
filesmanager = Files.Files(address)
packages = PackageManager.PackageManager(address)
system = SystemMaintenance.SystemMaintenance(address,username,password)

#calling methods
#packages.unschedulePackageDisable("ipv6")
system.shutdownRouter()






