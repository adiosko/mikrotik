import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from interfaces.interfaceList import interfaceList

qtCreatorFile = "./loginGUI/addListMember.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addListMemberGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server,address_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.address_window = address_window
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = interfaceList(self.server,self.user,self.pwd)

    def okButon(self):
        try:
            name = self.listField.toPlainText()
            interface = self.interfaceField.toPlainText()
            self.addr.addInterface(name,interface)
            self.address_window.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Interface error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelButon(self):
        self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect( self.cancelButon )
        self.okButton.clicked.connect( self.okButon )