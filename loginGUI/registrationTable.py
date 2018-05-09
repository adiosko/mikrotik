import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from wireless.registration import registration
#from loginGUI.addProfile import addProfile
#my designed file


qtCreatorFile = "registration.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class registrationGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = registration(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listDevices()

    def listDevices(self):
        devices = self.addr.listRegistration()
        self.nameField.clear()
        self.macField.clear()
        self.interfaceField.clear()
        self.address_to_id = {}
        for i in devices:
            self.nameField.addItem( devices[i]['radio-name'] )
            self.modeField.addItem(devices[i]['mac-address'])
            self.interfaceField.addItem(devices[i]['interface'])
            self.address_to_id[devices[i]['radio-name']] = devices[i]['.id']

    def removeDevice(self):
        try:
            current = self.nameField.currentRow()
            item = self.nameField.item( current )
            idItem = self.address_to_id[item.text()]
            self.addr.removeConnection( str( idItem ) )
            self.listDevices()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str( e ) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def resetDevice(self):
        try:
            current = self.nameField.currentRow()
            item = self.nameField.item( current )
            idItem = self.address_to_id[item.text()]
            self.addr.resetConnection( str( idItem ) )
            self.listDevices()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listDevices )
        #self.enableButton.clicked.connect(self.enableInterface)
        #self.disableButton.clicked.connect(self.disableInterface)
        self.removeButton.clicked.connect(self.removeDevice)
        self.resetButton.clicked.connect(self.resetDevice)