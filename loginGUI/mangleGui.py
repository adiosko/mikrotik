import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.FirewallMangle import FirewallMangle
from loginGUI.addMangleInputAccept import addMangleInput
from loginGUI.addMangleInputReject import addMangleInputReject
from loginGUI.addMangleInputDrop import addMangleInputDrop
from loginGUI.addMangleForwardAccept import addMangleForwardAccept
from loginGUI.addMangleForwardReject import addMangleForwardReject
from loginGUI.addMangleForwardDrop import addMangleForwardDrop
from loginGUI.addMangleOuputAccept import addMangleOutputAccept
from loginGUI.addMangleOutputDrop import addMangleOutputDrop
from loginGUI.addMangleOutputReject import addMangleOutputReject
from loginGUI.addManglePostRouteAccept import addManglePostrouteAccept
from loginGUI.addPostRoutingDrop import addManglePostrouteDrop
from loginGUI.addPostReject import addManglePostrouteReject
from loginGUI.addPrerouteAccept import addManglePrerouteAccept
from loginGUI.addPrerouteDrop import addManglePrerouteDrop
from loginGUI.addPrerouteReject import addManglePrerouteReject
#my designed file


qtCreatorFile = "./loginGUI/mangle.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class mangleGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = FirewallMangle(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listRules()

    def listRules(self):
        devices = self.addr.listRules()
        self.actionField.clear()
        self.chainField.clear()
        self.srcaddrField.clear()
        self.dstaddrField.clear()
        self.protField.clear()
        self.srcportField.clear()
        self.dstportField.clear()
        self.ininterfaceField.clear()
        self.outinterfaceField.clear()
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
                statetoadd = devices[i]['in-interface']
            except:
                statetoadd = "any"
            self.ininterfaceField.addItem(statetoadd)
            try:
                statetoport = devices[i]['out-interface']
            except:
                statetoport = "any"
            self.outinterfaceField.addItem(statetoport)
            self.dynamicField.addItem(devices[i]['dynamic'])
            statedis = ""
            try:
                statedis = devices[i]['disabled']
            except:
                statedis = "unknown"
            self.disableField.addItem(statedis)
            self.address_to_id[devices[i]['action']] = devices[i]['.id']

    def removeRule(self):
        try:
            current = self.actionField.currentRow()
            itemName = self.actionField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeRule( str( idName ) )
            self.listRules()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Mangle error" )
            self.msg.setInformativeText(str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def enableRule(self):
        try:
            current = self.actionField.currentRow()
            itemName = self.actionField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableRule( str( idName ) )
            self.listRules()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "FW error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableRule(self):
        try:
            current = self.actionField.currentRow()
            itemName = self.actionField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableRule( str( idName ) )
            self.listRules()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "FW error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def addInputAccept(self):
        #self.nd = addMangleInput( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addMangleInput( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addInputReject(self):
        #self.nd = addMangleInputReject( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addMangleInputReject( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addInputDrop(self):
        #self.nd = addMangleInputDrop( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addMangleInputDrop( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addForwardAccept(self):
        #self.nd = addMangleForwardAccept(self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addMangleForwardAccept( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addForwardDrop(self):
        #self.nd = addMangleForwardDrop( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addMangleForwardDrop( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addForwardReject(self):
        #self.nd = addMangleForwardReject( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addMangleForwardReject( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addOutpuAccept(self):
        #self.nd = addMangleOutputAccept(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addMangleOutputAccept( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addOutpuDrop(self):
        #self.nd = addMangleOutputDrop(self.user,self.pwd,self.server,self)
        #elf.nd.show()
        action = addMangleOutputDrop( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addOutpuReject(self):
        #self.nd = addMangleOutputReject(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addMangleOutputReject( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()


    def addPostAccept(self):
        #self.nd = addManglePostrouteAccept(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addManglePostrouteAccept( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addPostDrop(self):
        #self.nd = addManglePostrouteDrop(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addManglePostrouteDrop( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addPostReject(self):
        #self.nd = addManglePostrouteReject(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addManglePostrouteReject( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addPreAccept(self):
        #self.nd = addManglePrerouteAccept(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addManglePrerouteAccept( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addPreDrop(self):
        #self.nd = addManglePrerouteDrop(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addManglePrerouteDrop( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def addPreReject(self):
        #self.nd = addManglePrerouteReject(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addManglePrerouteReject( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listRules)
        self.enableButton.clicked.connect(self.enableRule)
        self.disableButton.clicked.connect(self.disableRule)
        self.inputacceptButton.clicked.connect(self.addInputAccept)
        self.removeButton.clicked.connect(self.removeRule)
        self.inputrejectButton.clicked.connect(self.addInputReject)
        self.inputdropButton.clicked.connect(self.addInputDrop)
        self.fwacceptButton.clicked.connect( self.addForwardAccept )
        self.fwrejectButton.clicked.connect( self.addForwardReject)
        self.fwdropButton.clicked.connect( self.addForwardDrop)
        self.outputacceptButton.clicked.connect(self.addOutpuAccept)
        self.outputtrejectButton.clicked.connect(self.addOutpuReject)
        self.outputdropButton.clicked.connect(self.addOutpuDrop)
        self.postroutetacceptButton.clicked.connect(self.addPostAccept)
        self.postroutettrejectButton.clicked.connect(self.addPostReject)
        self.postroutetdropButton.clicked.connect(self.addPostDrop)
        self.preroutetacceptButton.clicked.connect(self.addPreAccept)
        self.prerouterejectButton.clicked.connect(self.addPreReject)
        self.preroutedropButton.clicked.connect(self.addPreDrop)