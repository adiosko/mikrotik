from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from PyQt4.QtGui import *
from IPv4.RouteGeneral import  RouteGeneral
import sys
import tikapy

qtCreatorFile = "./loginGUI/addRoute.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addRoute(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, route_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.route_window = route_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = RouteGeneral( self.server, self.user, self.pwd )

    def okLogin(self):
        try:
            dest = self.destField.toPlainText()
            gateway = self.gwField.toPlainText()
            self.addr.addRoute(dest,gateway)
            self.route_window.listRoutes()
            self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Route error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)