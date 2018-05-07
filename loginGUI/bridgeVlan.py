import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from bridge.bridgeVlan import  bridgeVlan
from loginGUI.addVLAN import addVLANGui

qtCreatorFile = "vlan.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class bridgeVLAN(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = bridgeVlan(self.server,self.user,self.pwd)
        self.listVlan()

    def listVlan(self):
        devices = self.addr.listVlan()
        self.bridgeField.clear()
        self.vlanField.clear()
        self.address_to_id = {}
        for i in devices:
            self.bridgeField.addItem( devices[i]['bridge'])
            self.vlanField.addItem(devices[i]['vlan-ids'])
            self.address_to_id[devices[i]['bridge']] = devices[i]['.id']

    def enableVlan(self):
        try:
            current = self.bridgeField.currentRow()
            self.addr.enableVlan( str( current ) )
            self.listVlan()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()
        """
        currentBridge = self.bridgeField.currentRow()
        currentVlan = self.vlanField.currentRow()
        itemBridge = self.bridgeField.item( currentBridge )
        #idBridge = self.address_to_id[itemBridge]
        itemVlan = self.vlanField.item( currentVlan )
        #idVlan = self.address_to_id[itemVlan]
        self.addr.enableVlan( str( itemBridge ) )
        self.addr.enableVlan( str( itemVlan ) )
        itemBridge.setFlags( Qt.ItemIsSelectable )
        itemVlan.setFlags( Qt.ItemIsSelectable )
        """

    def disableVlan(self):
        current = self.bridgeField.currentRow()
        self.addr.disableVlan( str( current ) )
        self.listVlan()
        """
        currentBridge = self.bridgeField.currentRow()
        currentVlan = self.vlanField.currentRow()
        itemBridge = self.bridgeField.item( currentBridge )
        #idBridge = self.address_to_id[itemBridge]
        itemVlan = self.vlanField.item( currentVlan )
        #idVlan = self.address_to_id[itemVlan]
        self.addr.disableVlan( str( itemBridge) )
        self.addr.disableVlan( str( itemVlan ) )
        itemBridge.setFlags( Qt.ItemIsSelectable )
        itemVlan.setFlags( Qt.ItemIsSelectable )
        """

    def removeVlan(self):
        current = self.bridgeField.currentRow()
        self.addr.removeVlan( str( current ) )
        self.listVlan()
        """
        currentBridge = self.bridgeField.currentRow()
        currentVlan = self.vlanField.currentRow()
        itemBridge = self.bridgeField.item( currentBridge )
        #idBridge = self.address_to_id[itemBridge]
        itemVlan = self.vlanField.item( currentVlan )
        #idVlan = self.address_to_id[itemVlan]
        self.addr.removeVlan( str( itemBridge ) )
        self.addr.removeVlan( str( itemVlan ) )
        itemBridge.setFlags( Qt.ItemIsSelectable )
        itemVlan.setFlags( Qt.ItemIsSelectable )
        """

    def addVlan(self):
        self.nd = addVLANGui(self.user, self.pwd, self.server,self)
        self.nd.show()


    def init_buttons(self):
        self.addButton.clicked.connect( self.addVlan )
        self.enableButton.clicked.connect( self.enableVlan )
        self.disableButton.clicked.connect( self.disableVlan )
        self.removeButton.clicked.connect( self.removeVlan )
        self.refreshButton.clicked.connect( self.listVlan )


