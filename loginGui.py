import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import tikapy
from PyQt4 import QtCore, QtGui, uic
from loginGUI.loginWindow import loginMikrotik
from LoginManager import *
from centralControl import centralControl
#import  LoginManager
#my designed file
qtCreatorFile = "./loginGUI/login.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class loginGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_buttons()
        self.user = self.userField.text()
        self.pwd = self.passwordField.text()
        self.server = self.addressField.text()
        self.loginmanager = LoginManager( self.user, self.pwd )
        self.loginIpManager = centralControl( self.user )
        self.ipList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.login_windows = []
        self.ipList.itemClicked.connect(self.paste)
        self.macList.itemClicked.connect(self.pastemac)
        #self.recordIPAddress()
        #self.recordMacAddress()
        #self.ui.calc_tax_button.clicked.connect(self.calculateTax())

    def paste(self):
        selected = self.ipList.selectedItems()
        self.addressField.setText(selected[0].text())

    def pastemac(self):
        selected = self.macList.selectedItems()
        self.addressField.setText( selected[0].text() )

    def helloWorld(self,strword):
        print("Hello "+strword)

    def cancelLogin(self):
        self.close()


    def loginLogin(self):
        self.user = self.userField.text()
        self.pwd = self.passwordField.text()
        self.server = self.addressField.text()
        self.loginIP()


    def recordMacAddress(self):
        self.macList.clear()
        self.ipList.clear()
        devices = self.loginmanager.listMikrotikDevices()
        for device in devices:
            self.macList.addItem(str(device))

    def recordIPAddress(self):
        self.ipList.clear()
        devices = self.loginIpManager.listMikrotikDevices()
        print( devices )
        for device in devices:
            self.ipList.addItem( str(device) )

    def refresh(self):
        self.ipList.clear()
        self.macList.clear()
        devices = self.loginmanager.listMikrotikDevices()
        devicesip = self.loginIpManager.listMikrotikDevices()
        #devicesIp = self.loginmanager.listMikrotikDevicesIp()
        print(devices)
        for device in devices:
            self.macList.addItem(str(device))
        for device in devicesip:
           self.ipList.addItem( str( device ) )


    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.loginButton.clicked.connect(self.loginLogin)
        self.refreshButton.clicked.connect(self.refresh)

    """
    def loginMac(self):
        self.server = self.addressField.text()
        self.user = self.userField.text()
        self.pwd = self.passwordField.text()
        result = self.loginmanager.mactelnetLoginToSingleDevice(self.user,self.pwd,self.server)
        if result == 0:
            self.nd = loginMikrotik(self.user,self.pwd,self.server)
            self.nd.show()
            client = tikapy.TikapyClient("192.168.1.1")
            client.login(self.user,self.pwd)
            print(client.talk(['/ip/address/print']))
        else:
            print("retry")
    """

    def loginIP(self):
        try:
            self.server = self.addressField.text()
            self.user = self.userField.text()
            self.pwd = self.passwordField.text()
            mikrotik = tikapy.TikapySslClient( self.server,8729)
            result = mikrotik.login(self.user,self.pwd)
            if result is None:
                #self.nd = loginMikrotik(self.user,self.pwd,self.server)
                #self.nd.show()
                self.login_windows.append(loginMikrotik(self.user,self.pwd,self.server))
                self.login_windows[-1].show()
                self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Authentication error" )
            self.msg.setInformativeText(str(e))
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = loginGui()
    window.show()
    sys.exit(app.exec_())