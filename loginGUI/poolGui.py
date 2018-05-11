import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.Pool import Pool
from loginGUI.addPoolGui import addPool
#my designed file


qtCreatorFile = "./loginGUI/pool.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class poolGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = Pool(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listPools()

    def listPools(self):
        devices = self.addr.listPool()
        self.nameField.clear()
        self.rangeField.clear()
        self.address_to_id = {}
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.rangeField.addItem(devices[i]['ranges'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']


    def addPool(self):
        self.nd = addPool( self.user, self.pwd, self.server, self )
        self.nd.show()

    def removePool(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removePool( str( idName) )
            self.listPools()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Pool error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listPools)
        #self.enableButton.clicked.connect(self.enableInterface)
        #self.disableButton.clicked.connect(self.disableInterface)
        self.addButton.clicked.connect(self.addPool)
        self.removeButton.clicked.connect(self.removePool)