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
qtCreatorFile = "login.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class loginGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_buttons()
        user = self.userField.text()
        pwd = self.passwordField.text()
        self.loginmanager = LoginManager( user, pwd )
        self.loginIpManager = centralControl( user )
        #self.recordIPAddress()
        #self.recordMacAddress()
        #self.ui.calc_tax_button.clicked.connect(self.calculateTax())

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.loginButton.clicked.connect(self.loginLogin)

    def helloWorld(self,strword):
        print("Hello "+strword)

    def cancelLogin(self):
        sys.exit()


    def loginLogin(self):
        user = self.userField.text()
        pwd = self.passwordField.text()
        server = self.addressField.text()
        self.loginIP()
    """
    def recordMacAddress(self):
        devices = self.loginmanager.listMikrotikDevices()
        print(devices)
        for device in devices:   
            self.macList.append(device)

    def recordIPAddress(self):
        devices = self.loginIpManager.listMikrotikDevices()
        print(devices)
        for device in devices:
            self.ipList.append(device)
    """

    def loginMac(self):
        server = self.addressField.text()
        user = self.userField.text()
        pwd = self.passwordField.text()
        result = self.loginmanager.mactelnetLoginToSingleDevice(user,pwd,server)
        if result == 0:
            self.nd = loginMikrotik()
            self.nd.show()
            client = tikapy.TikapyClient("192.168.1.1")
            client.login(user,pwd)
            print(client.talk(['/ip/address/print']))
        else:
            print("retry")


    def loginIP(self):
        server = self.addressField.text()
        user = self.userField.text()
        pwd = self.passwordField.text()
        mikrotik = tikapy.TikapyClient( server)
        result = mikrotik.login(user,pwd)
        if result is None:
            self.nd = loginMikrotik()
            self.nd.show()
            """
            login = mikrotik.talk(['/ip/address/print'])
            for i in login:
                
            resulttik = str(self.textCustom.setText(login))
            self.nd.textCustom.setText(resulttik)
            """
        else:
            self.textEdit.text("Wrong username or password")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = loginGui()
    window.show()
    sys.exit(app.exec_())