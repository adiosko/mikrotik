#THIS IS MAIN LIBRARY WHRE MAIN CODE WILL RUN CONSISTING OF ALL LIBRARIES CREATED IN THIS PROJECT
import LoginManager
import tikapy
from System import Interfaces, Users, Services, Files, PackageManager, SystemMaintenance
from System import SystemClock, Certificates, Identity, AutoUpdate, Console, Health, History, LCD, LED
from System import Licence,Logging, NTPclient,NTPserver,ResetConfig, Resources, RouterBoard, Scheduller, Scripts, SpecialLogin
from System import UPS, WatchDog
from makeSupportFile import makeSupport
from Dude import Devices,Notifications, Probes, RosInfo, Services, Settings
from Tools import BwServer, BwTest, Email, FloodPing, Graphing, IpScan, MacServer, Netwatch, PacketSniffer, Ping, PingSpeed
from Tools import Profile, RoMon, SMS, Telnet, Torch, TrafficGenerator, TrafficMonitorList
from log import Log

username = "admin"
password = 'admin'
login = LoginManager.LoginManager(username,password)
address = "172.16.53.2"

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
sup = makeSupport.makeSupport(address,username,password)
dev = Devices.Devices(address,username,password)
notif = Notifications.Notifications(address,username,password)
probe = Probes.Probes(address,username,password)
ros = RosInfo.RosInfo(address,username,password)
serv = Services.Services(address,username,password)
sett = Settings.Settings(address,username,password)
bws = BwServer.BwServer(address,username,password)
bwt = BwTest.BwTest(address,username,password)
mail = Email.Email(address,username,password)
fping = FloodPing.FloodPing(address,username,password)
graf = Graphing.Graphing(address,username,password)
ips = IpScan.IpScan(address,username,password)
mac = MacServer.MacServer(address,username,password)
nwc = Netwatch.Netwatch(address,username,password)
sniff = PacketSniffer.PacketSniffer(address,username,password)
ping = Ping.Ping(address,username,password)
speed = PingSpeed.PingSpeed(address,username,password)
prof = Profile.Profile(address,username,password)
romon = RoMon.RoMon(address,username,password)
SMS = SMS.SMS(address,username,password)
torch = Torch.Torch(address,username,password)
traff = TrafficGenerator.TrafficGenerator(address,username,password)
mon = TrafficMonitorList.TrafficMonitorList(address,username,password)
log = Log.Log(address,username,password)

log.listLog()
#client.talk( ['/certificate/create-certificate-request', '=template=cert1', '= key-passphrase=pass'])
#packages.unschedulePackageDisable("ipv6")
#system.shutdownRouter()
