from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from wireless.securityProfile import  securityProfile
import sys

qtCreatorFile = "./loginGUI/addProfile.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addProfile(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, wireless_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.wireless_window = wireless_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = securityProfile( self.server, self.user, self.pwd )

    def okLogin(self):
        try:
            name = self.nameField.toPlainText()
            password = self.passwordField.toPlainText()
            self.addr.addProfile(name,password)
            self.wireless_window.listProfiles()
        except Exception as e:
            from PyQt4.QtGui import QMessageBox
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Password length error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)