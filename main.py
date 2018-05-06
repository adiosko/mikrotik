from PyQt5.QtWidgets import QApplication, QWidget

import Constructors
import LoginManager
import centralControl
import tikapy
import dhcpClient

#mikrotik = Constructors.Mikrotik(address="192.168.1.1",username="admin",password="admin")
#mikrotik.addresses.listAddresses()
#api = tikapy.TikapySslClient("192.168.1.1",8729)
#api.login("admin","admin")
#print(api.talk(['/ip/address/print']))
#dhcp = dhcpClient.DhcpClient("ether2","64:d1:54:53:59:72")
#dhcp.dhcp("admin","admin")
api = tikapy.TikapySslClient("192.168.1.1")
api.login("admin","admin")
print(api.talk(['/interface/bridge/port/print']))