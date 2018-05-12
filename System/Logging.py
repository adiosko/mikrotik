from tikapy import TikapyClient
from tikapy import TikapySslClient

class Logging:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listLogging(self):
        """
        Method will list all logging config
        :return:  list
        """
        log = self.client.talk(['/system/logging/print'])
        return log

    def addLoggingRule(self,topic,action,prefix=None):
        """
        Method will add logging rule
        :param topic: one of rules for topic includes account, async, backup, bfd, bgp, calc, caps, certificate,
        critical, ddns, debug, dhcp, dns, dude, e-mail, error, event, firewall, gps, gsm, hotspot, igmp-proxy, info,
        interface, ipsec, iscsi, isdn, kvm, l2tp, ldp, lte, manager, mme, mpls, ntp, ospf, ovpn, packet, pim, poe-out,
        ppp, ppptp, pppoe, radius, radvd, raw, read, rip, route, rsvp, script, sertcp, simulator, smb, snmp, ssh,
        sstp, state, store, system, telephony, tftp, timer, tr069, upnp, ups, vrrp, warning, watchdog, web-proxy,
        wireless, write
        for negation use !name
        :param action: memory, disk, echo, remote
        :param prefix: custome prefix (optional)
        :return: list
        """
        if prefix == None:
            log = self.client.talk(['/system/logging/add','=topics='+topic,'=action='+action])
        else:
            log = self.client.talk( ['/system/logging/add', '=topics=' + topic, '=action=' + action,'=prefix='+prefix] )
        return log

    def addAccount(self):
        log = self.client.talk(['/system/logging/add','=topics=account','=action=disk'])
        return log

    def addBackup(self):
        log = self.client.talk(['/system/logging/add','=topics=backup','=action=disk'])
        return log

    def addCertificate(self):
        log = self.client.talk(['/system/logging/add','=topics=certificate','=action=disk'])
        return log

    def addDebug(self):
        log = self.client.talk(['/system/logging/add','=topics=debug','=action=disk'])
        return log

    def addDns(self):
        log = self.client.talk(['/system/logging/add','=topics=dns','=action=disk'])
        return log

    def addError(self):
        log = self.client.talk(['/system/logging/add','=topics=error','=action=disk'])
        return log

    def addEvent(self):
        log = self.client.talk( ['/system/logging/add', '=topics=event', '=action=disk'] )
        return log

    def addFirewall(self):
        log = self.client.talk( ['/system/logging/add', '=topics=firewall', '=action=disk'] )
        return log

    def addInfo(self):
        log = self.client.talk( ['/system/logging/add', '=topics=info', '=action=disk'] )
        return log

    def addIpsec(self):
        log = self.client.talk( ['/system/logging/add', '=topics=ipsec', '=action=disk'] )
        return log

    def addOspf(self):
        log = self.client.talk( ['/system/logging/add', '=topics=ospf', '=action=disk'] )
        return log

    def addOvpn(self):
        log = self.client.talk( ['/system/logging/add', '=topics=ovpn', '=action=disk'] )
        return log

    def addPacket(self):
        log = self.client.talk( ['/system/logging/add', '=topics=packet', '=action=disk'] )
        return log

    def addRoute(self):
        log = self.client.talk( ['/system/logging/add', '=topics=route', '=action=disk'] )
        return log

    def addSsh(self):
        log = self.client.talk( ['/system/logging/add', '=topics=ssh', '=action=disk'] )
        return log

    def addWireless(self):
        log = self.client.talk( ['/system/logging/add', '=topics=write', '=action=disk'] )
        return log


    def removeLoggingRule(self,numbers):
        """
        Method will remove logging rule by order number
        :param number: order number of dictionary index
        :return: list
        """
        log = self.client.talk(['/system/logging/remove','=remove='+numbers])
        return log

    def enableRule(self,number):
        """
        Enabling disabled rule
        :param number: order no
        :return:  list
        """
        log = self.client.talk(['/system/logging/enable','=numbers='+number])
        return log

    def disableRule(self,number):
        """
        Disable enabled rule
        :param number:  number of rule
        :return:  list
        """
        log = self.client.talk( ['/system/logging/disable', '=numbers=' + number] )
        return log

    def listCustomActions(self):
        """
        Method will list all custom actions
        :return: list
        """
        action = self.client.talk(['/system/logging/action/print'])
        if action == {}:
            print("No customa ction found")
        else:
            print("Name\ttype\tisDefault")
            for i in action:
                print(action[i]['name']+"\t"+action[i]['target']+"\t"+action[i]['default'])

    def addAction(self,name,type,lines):
        """
        Method will add customa ction to mikrotik
        :param name: name of action
        :param type: type of action: mamory, disk, echo, email, remote
        :param stoponfull:action will stop if is full
        :return: list
        """
        action = self.client.talk(['/system/logging/action/add','=name='+name,'=target='+type,'=memory-lines='+lines])
        return action

    def removeAction(self,actionName):
        """
        Method will remove custom action name
        :param actionName: action Name u wanna remove
        :return: list
        """
        if actionName == "disk" or actionName == "echo" or actionName == "memory" or actionName == "remote":
            print("cannot remove default action")
        else:
            action = self.client.talk(['/system/logging/action/remove','=numbers='+actionName])
        return action

    def setAction(self,actionName,newName,type,lines):
        """
        Method will edit action which exists
        :param actionName: name of action u wanna edit
        :return: list
        """
        if actionName == "disk" or actionName == "echo" or actionName == "memory" or actionName == "remote":
            print( "cannot edit default action" )
            self.client.disconnect()
        else:
            action = self.client.talk(['/system/logging/action/set','=numbers='+actionName,'=name='+newName,'=target='
                                       +type,'=memory-lines='+lines])
        return action
