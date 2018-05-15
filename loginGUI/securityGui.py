import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from wireless.securityProfile import securityProfile
from loginGUI.addProfile import addProfile
#my designed file


qtCreatorFile = "./loginGUI/security.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class securityGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = securityProfile(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listProfiles()

    def listProfiles(self):
        devices = self.addr.listProfiles()
        self.nameField.clear()
        self.modeField.clear()
        self.authField.clear()
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.modeField.addItem(devices[i]['mode'])
            self.authField.addItem(devices[i]['authentication-types'])

    def removeProfile(self):
        try:
            current = self.nameField.currentRow()
            self.addr.removeProfile( str( current ) )
            self.listProfiles()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Profile error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def addProfile(self):
        #self.nd = addProfile( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addProfile( self.user, self.pwd, self.server, self )
        self.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listProfiles )
        #self.enableButton.clicked.connect(self.enableInterface)
        #self.disableButton.clicked.connect(self.disableInterface)
        self.removeButton.clicked.connect(self.removeProfile)
        self.addButton.clicked.connect(self.addProfile)