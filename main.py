import Constructors
import LoginManager
import centralControl

mikrotik = Constructors.Mikrotik(address="192.168.1.1",username="admin",password="admin")
#login = LoginManager.LoginManager("admin","admin")
central = centralControl.centralControl("admin","admin")
central.listMikrotikDevices()
#mikrotik.wchannel.listChannels()