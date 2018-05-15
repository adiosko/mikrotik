from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from IPv4.Pool import  Pool

qtCreatorFile = "./loginGUI/addPool.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addPool(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, pool_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pool_window = pool_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = Pool( self.server, self.user, self.pwd )

    def okLogin(self):
        try:
            name = self.nameField.toPlainText()
            range = self.rangeField.toPlainText()
            self.addr.addPool(name,range)
            self.pool_window.listPools()
        except Exception as e:
            from PyQt4.QtGui import QMessageBox
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Wrong range" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)