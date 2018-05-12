import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from System.Logging import Logging
from loginGUI.addDhcpServer import addDhcpServerGui
#my designed file


qtCreatorFile = "./loginGUI/logging.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class loggingGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = Logging(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listLogging()
        self.topicField.clear()
        self.actionField.clear()
        self.disableField.clear()
        self.defaultField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            statelocal = ""
            statedynamic = ""
            self.topicField.addItem(devices[i]['topics'])
            self.actionField.addItem(devices[i]['action'])
            self.disableField.addItem(devices[i]['disabled'])
            try:
                state = devices[i]['default']
            except:
                state = "Custom"
            self.defaultField.addItem(state)
            self.address_to_id[devices[i]['topics']] = devices[i]['.id']

    def enableAddress(self):
        try:
            current = self.topicField.currentRow()
            itemName = self.topicField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableRule( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableAddress(self):
        try:
            current = self.topicField.currentRow()
            itemName = self.topicField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableRule( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeAddress(self):
        try:
            current = self.topicField.currentRow()
            itemName = self.topicField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeLoggingRule( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def addAccoutn(self):
        self.addr.addAccount()
        self.listAddresses()

    def addBackup(self):
        self.addr.addBackup()
        self.listAddresses()

    def addCertificate(self):
        self.addr.addCertificate()
        self.listAddresses()

    def addDebug(self):
        self.addr.addDebug()
        self.listAddresses()

    def addDns(self):
        self.addr.addDns()
        self.listAddresses()

    def addError(self):
        self.addr.addError()
        self.listAddresses()

    def addEvent(self):
        self.addr.addEvent()
        self.listAddresses()

    def addFirewall(self):
        self.addr.addFirewall()
        self.listAddresses()

    def addInfo(self):
        self.addr.addInfo()
        self.listAddresses()

    def addIpsec(self):
        self.addr.addIpsec()
        self.listAddresses()

    def addOspf(self):
        self.addr.addOspf()
        self.listAddresses()

    def addOvpn(self):
        self.addr.addOvpn()
        self.listAddresses()

    def addPacket(self):
        self.addr.addPacket()
        self.listAddresses()

    def addRoute(self):
        self.addr.addRoute()
        self.listAddresses()

    def addSsh(self):
        self.addr.addSsh()
        self.listAddresses()

    def addWireless(self):
        self.addr.addWireless()
        self.listAddresses()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses)
        self.enableButton.clicked.connect(self.enableAddress)
        self.disableButton.clicked.connect(self.disableAddress)
        self.removeButton.clicked.connect(self.removeAddress)
        self.accountButton.clicked.connect(self.addAccoutn)
        self.backupButton.clicked.connect(self.addBackup)
        self.certButton.clicked.connect( self.addCertificate )
        self.debugButton.clicked.connect( self.addDebug )
        self.dnsButton.clicked.connect( self.addDns )
        self.errorButton.clicked.connect( self.addError )
        self.eventButton.clicked.connect( self.addEvent )
        self.fwButton.clicked.connect( self.addFirewall )
        self.infoButton.clicked.connect( self.addInfo )
        self.ipsecButton.clicked.connect( self.addIpsec )
        self.ospfButton.clicked.connect( self.addOspf )
        self.ovpnButton.clicked.connect( self.addOvpn )
        self.packetButton.clicked.connect( self.addPacket )
        self.routeButton.clicked.connect( self.addRoute )
        self.sshButton.clicked.connect( self.addSsh )
        self.wirelessButton.clicked.connect( self.addWireless )
        #self.staticButton.clicked.connect(self.makeStatic)