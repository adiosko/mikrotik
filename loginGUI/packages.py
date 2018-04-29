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
        for i in devices:
            self.packageField.addItem( devices[i]['name'])
            self.versionField.addItem( devices[i]['version'])

    def enablePackage(self):
        currentName = self.packageField.currentRow()
        currentVersion = self.versionField.currentRow()
        itemName = self.packageField.item( currentName )
        itemVersion = self.versionField.item( currentVersion )
        self.addr.enablePackage(str( currentName ) )
        self.addr.enablePackage( str( currentVersion ) )
        itemName.setFlags( Qt.ItemIsSelectable )
        itemVersion.setFlags( Qt.ItemIsSelectable )

    def disablePackage(self):
        currentName = self.packageField.currentRow()
        currentVersion = self.versionField.currentRow()
        itemName = self.packageField.item( currentName )
        itemVersion = self.versionField.item( currentVersion )
        self.addr.disablePackage( str( currentName ) )
        self.addr.disablePackage(str(currentVersion))
        itemName.setFlags( Qt.ItemIsSelectable )
        itemVersion.setFlags( Qt.ItemIsSelectable )

    def init_buttons(self):
        self.enableButton.clicked.connect( self.enablePackage )
        self.disableButton.clicked.connect( self.disablePackage )
        self.refreshButton.clicked.connect( self.listPackages )