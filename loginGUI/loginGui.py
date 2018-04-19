import sys
from PyQt4 import QtCore, QtGui, uic
from loginGUI.loginWindow import loginMikrotik
#import  LoginManager
#my designed file
qtCreatorFile = "login.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class loginGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_buttons()
        #self.ui.calc_tax_button.clicked.connect(self.calculateTax())

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.loginButton.clicked.connect(self.loginLogin)

    def helloWorld(self,strword):
        print("Hello "+strword)

    def cancelLogin(self):
        sys.exit()


    def loginLogin(self):
        self.nd = loginMikrotik()
        self.nd.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= loginGui()
    window.show()
    sys.exit(app.exec_())