import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.FirewallNAT import FirewallNAT
from loginGUI.addMasquaradeGui import addMasquaradeGui
from loginGUI.addSrcNat import addSrcNatGui
from loginGUI.addDstNatGui import addDstNatGui
from loginGUI.addSrcAccept import addSrcAcceptGui
from loginGUI.addDstAccept import addDstAcceptGui
#my designed file


qtCreatorFile = "nat.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class natGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = FirewallNAT(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listNat()

    def listNat(self):
        devices = self.addr.listRules()
        self.actionField.clear()
        self.chainField.clear()
        self.srcaddrField.clear()
        self.dstaddrField.clear()
        self.protField.clear()
        self.srcportField.clear()
        self.dstportField.clear()
        self.toaddressField.clear()
        self.toportField.clear()
        self.dynamicField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            statesrc = ""
            statedst = ""
            stateprotocol = ""
            statesrcport = ""
            statedstport = ""
            statetoadd = ""
            statetoport = ""
            self.actionField.addItem( devices[i]['action'] )
            self.chainField.addItem(devices[i]['chain'])
            try:
                statesrc = devices[i]['src-address']
            except:
                statesrc = "any"
            self.srcaddrField.addItem(statesrc)
            try:
                statedst = devices[i]['dst-address']
            except:
                statedst = "any"
            self.dstaddrField.addItem(statedst)
            try:
                stateprotocol = devices[i]['protocol']
            except:
                stateprotocol = "any"
            self.protField.addItem(stateprotocol)
            try:
                statesrcport = devices[i]['src-port']
            except:
                statesrcport = "any"
            self.srcportField.addItem(statesrcport)
            try:
                statedstport = devices[i]['dst-port']
            except:
                statedstport = "any"
            self.dstportField.addItem(statedstport)
            try:
                statetoadd = devices[i]['to-addresses']
            except:
                statetoadd = "any"
            self.toaddressField.addItem(statetoadd)
            try:
                statetoport = devices[i]['to-ports']
            except:
                statetoport = "any"
            self.toportField.addItem(statetoport)
            self.dynamicField.addItem(devices[i]['dynamic'])
            statedis = ""
            try:
                statedis = devices[i]['disabled']
            except:
                statedis = "unknown"
            self.disableField.addItem( statedis )
            self.address_to_id[devices[i]['action']] = devices[i]['.id']

    def removeRule(self):
        try:
            current = self.actionField.currentRow()
            itemName = self.actionField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeRule( str( idName ) )
            self.listNat()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "NAT error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def enableRule(self):
        try:
            current = self.actionField.currentRow()
            itemName = self.actionField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableRule( str( idName ) )
            self.listNat()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "NAT error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableRule(self):
        try:
            current = self.actionField.currentRow()
            itemName = self.actionField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableRule( str( idName ) )
            self.listNat()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "NAT error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def addMasquarade(self):
        self.nd = addMasquaradeGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def addSrcNat(self):
        self.nd = addSrcNatGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def addDstNat(self):
        self.nd = addDstNatGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def addSrcAccept(self):
        self.nd = addSrcAcceptGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def addDstAccept(self):
        self.nd = addDstAcceptGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listNat)
        self.enableButton.clicked.connect(self.enableRule)
        self.disableButton.clicked.connect(self.disableRule)
        self.masqButton.clicked.connect(self.addMasquarade)
        self.removeButton.clicked.connect(self.removeRule)
        self.srcButton.clicked.connect(self.addSrcNat)
        self.dstButton.clicked.connect(self.addDstNat)
        self.srcacceptButton.clicked.connect(self.addSrcAccept)
        self.dstacceptButton.clicked.connect(self.addDstAccept)