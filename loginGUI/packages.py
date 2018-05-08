import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from System.PackageManager import PackageManager

qtCreatorFile = "packages.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class packages(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = PackageManager(self.server,self.user,self.pwd)
        self.listPackages()

    def listPackages(self):
        devices = self.addr.listPackages()
        self.packageField.clear()
        self.versionField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.packageField.addItem( devices[i]['name'])
            self.versionField.addItem( devices[i]['version'])
            state = ""
            try:
                state = devices[i]['disabled']
            except:
                state = "Unknown"
            self.disableField.addItem(state)
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enablePackage(self):
        try:
            current = self.packageField.currentRow()
            itemName = self.packageField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enablePackage(str( current ) )
            self.listPackages()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Package error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disablePackage(self):
        try:
            current = self.packageField.currentRow()
            itemName = self.packageField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enablePackage( str( current ) )
            self.listPackages()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Package error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def init_buttons(self):
        self.enableButton.clicked.connect( self.enablePackage )
        self.disableButton.clicked.connect( self.disablePackage )
        self.refreshButton.clicked.connect( self.listPackages )