import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.FirewallServicePOrts import FirewallServicePOrts
#from loginGUI.addProfile import addProfile
#my designed file


qtCreatorFile = "./loginGUI/servicePort.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class servicePortGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = FirewallServicePOrts(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listServices()

    def listServices(self):
        devices = self.addr.listPorts()
        self.nameField.clear()
        self.portField.clear()
        self.sipmediaField.clear()
        self.siptimeField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            statePort = ""
            statesipmedia = ""
            statesiptimeout = ""
            self.nameField.addItem( devices[i]['name'] )
            try:
                statePort = devices[i]['ports']
            except:
                statePort = "None"
            self.portField.addItem(statePort)
            try:
                statesipmedia = devices[i]['sip-direct-media']
            except:
                statesipmedia = "None"
            self.sipmediaField.addItem(statesipmedia )
            try:
                statesiptimeout = devices[i]['sip-timeout']
            except:
                statesiptimeout = "None"
            self.siptimeField.addItem( statesiptimeout)
            statedis = ""
            try:
                statedis = devices[i]['disabled']
            except:
                statedis = "unknown"
            self.disableField.addItem( statedis )
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableService(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enablePort( str( idName ) )
            self.listServices()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Service error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableService(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disablePort( str( idName) )
            self.listServices()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Service error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listServices )
        #self.enableButton.clicked.connect(self.enableInterface)
        #self.disableButton.clicked.connect(self.disableInterface)
        self.enableButton.clicked.connect(self.enableService)
        self.disableButton.clicked.connect(self.disableService)