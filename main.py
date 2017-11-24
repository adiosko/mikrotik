#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
import Interfaces, Users, Services, Files, PackageManager, SystemMaintenance
import SystemClock, Certificates, Identity, AutoUpdate, Console, Health, History, LCD

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)
address = "192.168.1.1"

#objects
interface = Interfaces.InterfaceManager(address,username,password)
users = Users.Users(address,username,password)
services = Services.Services(address,username,password)
filesmanager = Files.Files(address,username,password)
packages = PackageManager.PackageManager(address,username,password)
system = SystemMaintenance.SystemMaintenance(address,username,password)
clock = SystemClock.SystemClock(address,username,password)
certs = Certificates.Certificates(address,username,password)
host = Identity.Identity(address,username,password)
update = AutoUpdate.AutoUpdate(address,username,password)
console = Console.Console(address,username,password)
helth = Health.Health(address,username,password)
history = History.History(address,username,password)
LCD =  LCD.LCD(address,username,password)

system.shutdownRouter()
#client.talk( ['/certificate/create-certificate-request', '=template=cert1', '= key-passphrase=pass'])
#packages.unschedulePackageDisable("ipv6")
#system.shutdownRouter()






