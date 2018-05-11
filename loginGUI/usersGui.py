import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from System.Users import  Users
from loginGUI.addUserGui import addUserGui
qtCreatorFile = "./loginGUI/user.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class usersGui(QtGui.QMainWindow,Ui_MainWindow):
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
        #self.address_to_id = {}
        self.addr = Users(self.server,self.user,self.pwd)
        self.listUsers()

    def listUsers(self):
        devices = self.addr.listUsers()
        self.userField.clear()
        self.groupField.clear()
        self.addressField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.userField.addItem( devices[i]['name'])
            self.groupField.addItem(devices[i]['group'])
            self.addressField.addItem(devices[i]['address'])
            state = ""
            try:
                state = devices[i]['disabled']
            except:
                state = "Unknown"
            self.disableField.addItem(state)
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def removeUser(self):
        try:
            current = self.userField.currentRow()
            itemName = self.userField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.deleteUser( str( current ) )
            self.listUsers()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "User error" )
            self.msg.setInformativeText( str( e ) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def enableUser(self):
        '''
        currentUser = self.userField.currentRow()
        itemUser = self.userField.item( currentUser)
        idUser = self.address_to_id[itemUser.text()]
        self.addr.enableSystemUser( idUser)
        itemAddress.setFlags( Qt.ItemIsSelectable )
        '''
        try:
            current = self.userField.currentRow()
            itemName = self.userField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableSystemUser( str( current ) )
            self.listUsers()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "User error" )
            self.msg.setInformativeText( str( e ) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def disableUser(self):
        try:
            current = self.userField.currentRow()
            itemName = self.userField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableUser( str( current ) )
            self.listUsers()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "User error" )
            self.msg.setInformativeText( str( e ) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def addUser(self):
        self.nd = addUserGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def init_buttons(self):
        self.addButton.clicked.connect( self.addUser )
        self.enableButton.clicked.connect(self.enableUser)
        self.disableButton.clicked.connect(self.disableUser)
        self.removeButton.clicked.connect(self.removeUser)
        self.refreshButton.clicked.connect( self.listUsers )