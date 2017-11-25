#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
from System import Interfaces, Users, Services, Files, PackageManager, SystemMaintenance
from System import SystemClock, Certificates, Identity, AutoUpdate, Console, Health, History, LCD, LED
from System import Licence,Logging, NTPclient,NTPserver,ResetConfig, Resources, RouterBoard, Scheduller, Scripts, SpecialLogin
from System import UPS, WatchDog

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
clock = SystemClock.SystemClock(address,username,password)
certs = Certificates.Certificates(address,username,password)
host = Identity.Identity(address,username,password)
update = AutoUpdate.AutoUpdate(address,username,password)
console = Console.Console(address,username,password)
helth = Health.Health(address,username,password)
history = History.History(address,username,password)
LCD =  LCD.LCD(address,username,password)
led = LED.LED(address,username,password)
licence = Licence.Licence(address,username,password)
log = Logging.Logging(address,username,password)
ntpc = NTPclient.NTPclient(address,username,password)
ntps = NTPserver.NTPserver(address,username,password)
reset = ResetConfig.ResetConfig(address,username,password)
resc = Resources.Resources(address,username,password)
rbr = RouterBoard.RouterBoard(address,username,password)
schd = Scheduller.Scheduller(address, username, password)
scr = Scripts.Scripts(address,username,password)
spl = SpecialLogin.SpecialLogin(address,username,password)
ups = UPS.UPS(address,username,password)
wdg = WatchDog.WatchDog(address,username,password)

system.shutdownRouter()
#client.talk( ['/certificate/create-certificate-request', '=template=cert1', '= key-passphrase=pass'])
#packages.unschedulePackageDisable("ipv6")
#system.shutdownRouter()






