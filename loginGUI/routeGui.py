import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from IPv4.RouteGeneral import  RouteGeneral
from loginGUI.addRoute import addRoute
import tikapy

qtCreatorFile = "./loginGUI/route.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class routeGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = RouteGeneral(self.server,self.user,self.pwd)
        self.listRoutes()

    def listRoutes(self):
        devices = self.addr.listRoutes()
        self.destField.clear()
        self.gwField.clear()
        self.distanceField.clear()
        self.dynamicField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.destField.addItem( devices[i]['dst-address'])
            self.gwField.addItem(devices[i]['gateway-status'])
            self.distanceField.addItem(devices[i]['distance'])
            self.disableField.addItem(devices[i]['disabled'])
            state = ""
            try:
                devices[i]['dynamic']
                state = "dynamic"
            except:
                state = "static"
            self.dynamicField.addItem(state)
            self.address_to_id[devices[i]['dst-address']] = devices[i]['.id']

    def addRoute(self):
        #self.nd = addRoute(self.user, self.pwd, self.server,self)
        #self.nd.show()
        action = addRoute( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.setFixedSize(380,105)
        action.show()
        #self.mdi.cascadeSubWindows()


    def enableRoute(self):
        try:
            current = self.destField.currentRow()
            itemName = self.destField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableRoute( str( idName ) )
            self.listRoutes()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Route error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableRoute(self):
        try:
            current = self.destField.currentRow()
            itemName = self.destField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableRoute( str( idName ) )
            self.listRoutes()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Route error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeRoute(self):
        try:
            current = self.destField.currentRow()
            itemName = self.destField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeRoute( str( idName ) )
            self.listRoutes()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Route error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def init_buttons(self):
        print("text")
        self.addButton.clicked.connect( self.addRoute )
        self.enableButton.clicked.connect( self.enableRoute )
        self.disableButton.clicked.connect( self.disableRoute )
        self.removeButton.clicked.connect( self.removeRoute )
        self.refreshButton.clicked.connect( self.listRoutes )


