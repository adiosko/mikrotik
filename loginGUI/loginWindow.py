import sys
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
qtCreatorFile = "loginWIndow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class loginMikrotik(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_buttons()
        #self.ui.calc_tax_button.clicked.connect(self.calculateTax())

    def init_buttons(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= loginMikrotik()
    window.show()
    sys.exit(app.exec_())