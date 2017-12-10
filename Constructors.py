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
from Radius import Radius
from Queues import SimpleQueues, QueueInterfaces, QueueTree, QueueTypes
from Routing import BFD, bgpInstance


class Mikrotik:
    def __init__(self,username,password,address):
        self.username = "admin"
        self.password = 'admin'
        self.login = LoginManager.LoginManager( username, password )
        self.address = "172.16.53.2"
        self.interface = Interfaces.InterfaceManager( address, username, password )
        self.users = Users.Users( address, username, password )
        self.services = Services.Services( address, username, password )
        self.filesmanager = Files.Files( address, username, password )
        self.packages = PackageManager.PackageManager( address, username, password )
        self.system = SystemMaintenance.SystemMaintenance( address, username, password )
        self.clock = SystemClock.SystemClock( address, username, password )
        self.certs = Certificates.Certificates( address, username, password )
        self.host = Identity.Identity( address, username, password )
        self.update = AutoUpdate.AutoUpdate( address, username, password )
        self.console = Console.Console( address, username, password )
        self.helth = Health.Health( address, username, password )
        self.history = History.History( address, username, password )
        self.LCD = LCD.LCD( address, username, password )
        self.led = LED.LED( address, username, password )
        self.licence = Licence.Licence( address, username, password )
        self.log = Logging.Logging( address, username, password )
        self.ntpc = NTPclient.NTPclient( address, username, password )
        self.ntps = NTPserver.NTPserver( address, username, password )
        self.reset = ResetConfig.ResetConfig( address, username, password )
        self.resc = Resources.Resources( address, username, password )
        self.rbr = RouterBoard.RouterBoard( address, username, password )
        self.schd = Scheduller.Scheduller( address, username, password )
        self.scr = Scripts.Scripts( address, username, password )
        self.spl = SpecialLogin.SpecialLogin( address, username, password )
        self.ups = UPS.UPS( address, username, password )
        self.wdg = WatchDog.WatchDog( address, username, password )
        self.sup = makeSupport.makeSupport( address, username, password )
        self.dev = Devices.Devices( address, username, password )
        self.notif = Notifications.Notifications( address, username, password )
        self.probe = Probes.Probes( address, username, password )
        self.ros = RosInfo.RosInfo( address, username, password )
        self.serv = Services.Services( address, username, password )
        self.sett = Settings.Settings( address, username, password )
        self.bws = BwServer.BwServer( address, username, password )
        self.bwt = BwTest.BwTest( address, username, password )
        self.mail = Email.Email( address, username, password )
        self.fping = FloodPing.FloodPing( address, username, password )
        self.graf = Graphing.Graphing( address, username, password )
        self.ips = IpScan.IpScan( address, username, password )
        self.mac = MacServer.MacServer( address, username, password )
        self.nwc = Netwatch.Netwatch( address, username, password )
        self.sniff = PacketSniffer.PacketSniffer( address, username, password )
        self.ping = Ping.Ping( address, username, password )
        self.speed = PingSpeed.PingSpeed( address, username, password )
        self.prof = Profile.Profile( address, username, password )
        self.romon = RoMon.RoMon( address, username, password )
        self.SMS = SMS.SMS( address, username, password )
        self.torch = Torch.Torch( address, username, password )
        self.traff = TrafficGenerator.TrafficGenerator( address, username, password )
        self.mon = TrafficMonitorList.TrafficMonitorList( address, username, password )
        self.log = Log.Log( address, username, password )
        self.radius = Radius.Radius( address, username, password )
        self.queue = SimpleQueues.SimpleQueues( address, username, password )
        self.qiface = QueueInterfaces.QueueInterfaces( address, username, password )
        self.tree = QueueTree.QueueTree( address, username, password )
        self.qtypes = QueueTypes.QueueTypes( address, username, password )
        self.bfd = BFD.BFD(address,username,password)
        self.inst = bgpInstance.BGPInstance(address,username,password)


