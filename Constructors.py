import LoginManager
import tikapy
from System import Interfaces, Users, Services, Files, PackageManager, SystemMaintenance
from System import SystemClock, Certificates, Identity, AutoUpdate, Console, Health, History, LCD, LED
from System import Licence,Logging, NTPclient,NTPserver,ResetConfig, Resources, RouterBoard, Scheduller, Scripts, SpecialLogin
from System import UPS, WatchDog
from makeSupportFile import makeSupport
from Dude import Devices,Notifications, Probes, RosInfo, Services, Settings
from Tools import BwServer, BwTest, Email, FloodPing, Graphing, IpScan, MacServer, Netwatch, PacketSniffer, Ping, PingSpeed
from Tools import Profile, RoMon, SMS, Telnet, Torch, TrafficGenerator, TrafficMonitorList
from log import Log
from Radius import Radius
from Queues import SimpleQueues, QueueInterfaces, QueueTree, QueueTypes
from Routing import BFD, bgpInstance, bgpVRF, bgpPeer, bgpNetworks,bgpAfregates,VPNRoutes,bgpAdverisment, RoutingFilters
from  Routing import FIlterChains, FilterBGP, FilterActions, FilterBgpActions, IgmpProxy, MME, OspfInterface,OspfInstances
from Routing import OspfNetworks, OspfArea, OspfAreaRanges,OspfVirtualLink, OspfNeighbors, OspfNbmaNeighbor,OspfShamLinks
from Routing import OspfLsa, OspfRoutes,OspfAsBorderRouters,OspfAreaBorderRouters, RoutingFilters, RoutingFilterMatchers
from Routing import RoutingFilterBgp, RoutingFilterActions,PimSettings,PimInterfaces,PimRp,PimBsrCandidates,RpCandidate
from Routing import PimNeighbors, PimBsr,PimMRib,PimMfc, PimJoins,PimIgmpGroups,PrefixList, RipSettings, RipInterfaces
from Routing import RipNetworks, RipKeys, RipNeighbors, RipRoutes,RipNgSettings,RipNgInterface, RipNgRoutes
from MPLS import MplsSettings, MplsLdpSettings,MplsLdpInterface, MplsLdpNeighbor, MplsAcceptFilter, MplsAdvertiseFilter
from  MPLS import MplsForwardingTable,MplsInterface, MplsLocalBinding, MplsRemoteBindings
from MPLS import TrafficEngInterface,TrafficEngTunnelPath,TrafficEngPathState, TrafficEngResvState, TrafficEngTraffInterface
from MPLS import MplsVpls,MplsBgpVpls,MplsCiscoBgpVpls
from IPv6 import Ipv6Addresses, DHCPv6Client,DHCPrelay, DhcpServer, Pool, Ipv6NeighborDiscovery, Neighbors, IPv6Settings
from IPv6 import IPv6Route, FirewallFilter, FirewallGeneralSetup, FirewallAdvancedSetup, FirewallExtraSetup
from IPv6 import FirewallActions, FirewallConenctions,Ipv6AddressList, FirewallMangle, FirewallRaw
from IPv4 import Arp,Accounting, Addresses, DhcpCLient, DhcpRelay, DhcpServer, DNSglobal, DNScache, DNSstatic
from  IPv4 import FirewallFilter, FirewallNAT, FirewallMangle, FireallGeneralSetup, FirewallAdvancedSetup, FirewallExtraSetup
from IPv4 import  FirewallAction, FirewallServicePOrts, FirewallCOnnections, FirewallAddressist, FirewallL7Protocols
from IPv4 import HotspotServer, HotspotServerProfile,HotspotUsers,HotspotUserProfile, HotspotActive, HotspotIpBindings
from  IPv4 import HotspotServicePorts, HotspotWalledGarden, HotspotWalledGardenList, HotspotCookies, IPsecPolicies
from IPv4 import IPsecGroups, IpsecPeers, IpsecRemotePeers, IPsecModeCOnfig, IPsecProposal, IpsecInstalledSa
from IPv4 import IPsecKeys, IPsecUsers, NeighborLIst, NeighborDIscovery, Packing, Pool, PoolUsedAddresses
from IPv4 import RouteGeneral, RouteNexthops, RouteRules, RoouteVrf, Smb, SmbShare, SmbUsers, Snmp, SnmpCommnity
from IPv4 import Services, Settings, Socks, SocksAccess, SocksConnections, Tftp, TrafficFlow, TrafficFlowIpfix
from IPv4 import UpnpSetting, UpnpInterface, WebProxySettings, WebProxyLookup, WebProxyInserts, WebProxyRefreshes
from IPv4 import WebProxyAccess, WebProxyCache, WebProxyDirect, WebProxyConnections, WebProxyCacheContetnt
from  mesh import MeshInterfaces, MeshPorts, MeshFdb
from switch import SwitchGeeral, SwitchPorts, SwitchHost, SwitchVlan, SwitchRule
from bridge import BridgeGeneral, BridgeSettings, BridgePorts, BridgeHosts, BridgeMdb, bridgeNat, bridgeArp
from bridge import bridgeNatAdvanced,bridgeNatGeneral, bridgeNatStp,bridgeFilter,bridgeFilterAction,bridgeFilterAdvanced
from bridge import bridgeFIlterArp,bridgeFIlterArp,bridgeFilterStp,bridgeMSTI,bridgePortMstOverride,bridgeVlan,bridgeNatAction
from ppp import activeConnections,interfaceL2tpCLient,interfaceL2tpClientSetGeneral,interfaceL2tpServer,interfaceL2tpServerBinding
from ppp import interfaceL2tpSet,interfaceOvpnClient,interfaceOvpnClientSetDialOut,interfacePppClientSetGeneral,interfaceOvpnServer
from ppp import interfacePppClient,interfacePppClientSetPpp,interfacePppClientSetGeneral,interfacePppoe,interfacePppoeClientSetDialOut
from ppp import interfacePppoeSet,interfacePppoeSetGeneral,interfacePppServer,interfacePppServerSetDialIn,interfacePppServerSetGeneral
from ppp import interfacePppServerSetGeneral,interfacePptpClient,interfacePptpCLientSetDialOut,interfacePptpClientSetGeneral
from ppp import interfacePptpServer,interfacePptpServerBinding,interfacePptpServerSetGeneral,interfaceSstpClient,interfaceSstpClientSetDialOut
from ppp import interfaceSstpClientSetDialOut,interfaceSstpServer,interfaceSstpServerSet,interfaceSstpServerBinding
from ppp import l2tpSecrets,pppAuthenticationAndAcounting,pppoe,pppoeSettings,profileGeneral,profileLimits,profileProtocols
from ppp import profileQueue,profiles,profileScripts,secrets,secretSettings,interfaceOvpnClientSetGeneral,interfaceOvpnServerBinding,interfaceOvpnClientSetDialOut
from ppp import interfaceOvpnServerSet, interfacePppClientSetPpp,interfacePppoeClient,interfacePppoeClientSetDialOut,interfaceSstpCLientGeneralSet
from wireless import channels,channelSet,securityProfile,securityProfileSetGeneral,securityProfileRadius,securityProfileEap,securityProfileStaticKeys
from  wireless import  connectList, connectListSet,accessList,accessListSet,NstremeDual,nstremeSetGeneral,nstreameSetDual
from wireless import nstremeDataRates,interfaceCap, interfaceWpsCLient, interfaceRepeater,interfaceWirelessAllignement
from wireless import interfaceSnifferSetting,wirelessSnooper,interfaceVirtual,interfaceVirtualWirelessSet,interfaceVirtualGeneralSet
from wireless import interfaceVirtualApbridgeSet,interfaceVirtualBridgeSet,interfaceVirtualNstreamDualSlave
from wireless import interfaceVirtualNstreamDualSlave,interfaceVirtualStation,interfaceVirtualStationBridge
from wireless import interfaceVirtualStationPseudobridge, interfaceVirtualStationPseudoBridgeClone, interfaceVirtualWds
from wireless import interfaceVirtualWds, interfaceVirtualWdsSlave
from interfaces import  interfaces

class Mikrotik:
    def __init__(self,username,password,address):
        self.username = "admin"
        self.password = 'admin'
        self.login = LoginManager.LoginManager( username, password )
        self.address = "192.168.1.1"
        #self.interface = Interfaces.InterfaceManager( address, username, password )
        self.users = Users.Users( address, username, password )
        self.services = Services.Services( address, username, password )
        self.filesmanager = Files.Files( address, username, password )
        self.packages = PackageManager.PackageManager( address, username, password )
        self.system = SystemMaintenance.SystemMaintenance( address, username, password )
        self.clock = SystemClock.SystemClock( address, username, password )
        self.certs = Certificates.Certificates( address, username, password )
        self.host = Identity.Identity( address, username, password )
        self.update = AutoUpdate.AutoUpdate( address, username, password )
        self.console = Console.Console( address, username, password )
        self.helth = Health.Health( address, username, password )
        self.history = History.History( address, username, password )
        self.LCD = LCD.LCD( address, username, password )
        self.led = LED.LED( address, username, password )
        self.licence = Licence.Licence( address, username, password )
        self.log = Logging.Logging( address, username, password )
        self.ntpc = NTPclient.NTPclient( address, username, password )
        self.ntps = NTPserver.NTPserver( address, username, password )
        self.reset = ResetConfig.ResetConfig( address, username, password )
        self.resc = Resources.Resources( address, username, password )
        self.rbr = RouterBoard.RouterBoard( address, username, password )
        self.schd = Scheduller.Scheduller( address, username, password )
        self.scr = Scripts.Scripts( address, username, password )
        self.spl = SpecialLogin.SpecialLogin( address, username, password )
        self.ups = UPS.UPS( address, username, password )
        self.wdg = WatchDog.WatchDog( address, username, password )
        self.sup = makeSupport.makeSupport( address, username, password )
        self.dev = Devices.Devices( address, username, password )
        self.notif = Notifications.Notifications( address, username, password )
        self.probe = Probes.Probes( address, username, password )
        self.ros = RosInfo.RosInfo( address, username, password )
        self.serv = Services.Services( address, username, password )
        self.sett = Settings.Settings( address, username, password )
        self.bws = BwServer.BwServer( address, username, password )
        self.bwt = BwTest.BwTest( address, username, password )
        self.mail = Email.Email( address, username, password )
        self.fping = FloodPing.FloodPing( address, username, password )
        self.graf = Graphing.Graphing( address, username, password )
        self.ips = IpScan.IpScan( address, username, password )
        self.mac = MacServer.MacServer( address, username, password )
        self.nwc = Netwatch.Netwatch( address, username, password )
        self.sniff = PacketSniffer.PacketSniffer( address, username, password )
        self.ping = Ping.Ping( address, username, password )
        self.speed = PingSpeed.PingSpeed( address, username, password )
        self.prof = Profile.Profile( address, username, password )
        self.romon = RoMon.RoMon( address, username, password )
        self.SMS = SMS.SMS( address, username, password )
        self.torch = Torch.Torch( address, username, password )
        self.traff = TrafficGenerator.TrafficGenerator( address, username, password )
        self.mon = TrafficMonitorList.TrafficMonitorList( address, username, password )
        self.log = Log.Log( address, username, password )
        self.radius = Radius.Radius( address, username, password )
        self.queue = SimpleQueues.SimpleQueues( address, username, password )
        self.qiface = QueueInterfaces.QueueInterfaces( address, username, password )
        self.tree = QueueTree.QueueTree( address, username, password )
        self.qtypes = QueueTypes.QueueTypes( address, username, password )
        self.bfd = BFD.BFD(address,username,password)
        self.inst = bgpInstance.BGPInstance(address,username,password)
        self.vrf = bgpVRF.bgpVRF(address,username,password)
        self.peer=bgpPeer.bgpPeer(address,username,password)
        self.bnet=bgpNetworks.bgpNetworks(address,username,password)
        self.bagr = bgpAfregates.bgpAgregates(address,username,password)
        self.bvpn = VPNRoutes.VPNRoutes(address,username,password)
        self.badv = bgpAdverisment.bgpAdvertisment(address,username,password)
        self.filt = RoutingFilters.RoutingFilters(address,username,password)
        self.chain = FIlterChains.FilterChains(address,username,password)
        self.bgpfilter = FilterBGP.FilterBGP(address,username,password)
        self.bgpaction = FilterActions.FilterActions(address,username,password)
        self.bgpact = FilterBgpActions.FilterBgpActions(address,username,password)
        self.proxy = IgmpProxy.IgmpProxy(address,username,password)
        self.mme = MME.MME(address,username,password)
        self.oiface = OspfInterface.OspfInterface(address,username,password)
        self.oinstance = OspfInstances.OspfInstances(address,username,password)
        self.onet = OspfNetworks.OspfNetworks(address,username,password)
        self.oarea = OspfArea.OspfArea(address,username,password)
        self.orange = OspfAreaRanges.OspfAreaRanges(address,username,password)
        self.ovirt = OspfVirtualLink.OspfVirtualLinks(address,username,password)
        self.oneig = OspfNeighbors.OspfNeighbors(address,username,password)
        self.onbma = OspfNbmaNeighbor.OspfNbmaNeighbor(address,username,password)
        self.osham = OspfShamLinks.OspfShamLinks(address,username,password)
        self.olsa = OspfLsa.OspfLsa(address,username,password)
        self.oroute = OspfRoutes.OspfRoutes(address,username,password)
        self.oasrtr = OspfAsBorderRouters.OspfAsBorderRouters(address,username,password)
        self.oareartr = OspfAreaBorderRouters.OspfAreaBorderRouters(address,username,password)
        self.rflt = RoutingFilters.RoutingFilters(address,username,password)
        self.rfltmatch = RoutingFilterMatchers.RoutingFiltersMatchers(address,username,password)
        self.rfltbgp = RoutingFilterBgp.RoutingFilterBgp(address,username,password)
        self.rflact = RoutingFilterActions.RoutingFilterActions(address,username,password)
        self.pim = PimSettings.PimSettings(address,username,password)
        self.piface = PimInterfaces.PimInterfaces(address,username,password)
        self.prp = PimRp.PimRp(address,username,password)
        self.pbsrc = PimBsrCandidates.PimBsrCandidates(address,username,password)
        self.prpc = RpCandidate.RpCandidate(address,username,password)
        self.pbsr = PimBsr.BsrStats(address,username,password)
        self.pmrib = PimMRib.PimMRib(address,username,password)
        self.pmfc = PimMfc.PimMfc(address,username,password)
        self.pjoin = PimJoins.PimJoins(address,username,password)
        self.pigmp = PimIgmpGroups.PimIgmpGroups(address,username,password)
        self.pflist = PrefixList.PrefixList(address,username,password)
        self.rset = RipSettings.RipSettings(address,username,password)
        self.riface = RipInterfaces.RipInterfaces(address,username,password)
        self.rntw = RipNetworks.RipNetworks(address,username,password)
        self.rkey = RipKeys.RipKeys(address,username,password)
        self.rneig = RipNeighbors.RipNeighbors(address,username,password)
        self.rroute = RipRoutes.RipRoutes(address,username,password)
        self.rngset = RipNgSettings.RipNgSettings(address,username,password)
        self.rngiface = RipNgInterface.RipNgInterfaces(address,username,password)
        self.rngroute = RipNgRoutes.RipNgRoutes(address,username,password)
        self.mset = MplsSettings.MplsSettings(address,username,password)
        self.mldpset = MplsLdpSettings.MplsLdpSettings(address,username,password)
        self.mldpiface = MplsLdpInterface.MplsLdpInterface(address,username,password)
        self.mldpneig = MplsLdpNeighbor.MplsLdpNeighbors(address,username,password)
        self.mldpacceptfilter = MplsAcceptFilter.MplsLdpAcceptFilter(address,username,password)
        self.mldpadvertfilter = MplsAdvertiseFilter.MplsAdvertiseFilter(address,username,password)
        self.mfwtable = MplsForwardingTable.MplsForwardingTable(address,username,password)
        self.miface = MplsInterface.MplsInterface(address,username,password)
        self.mlbind = MplsLocalBinding.MplsLocalBinding(address,username,password)
        self.mrbind = MplsRemoteBindings.MplsRemoteBinding(address,username,password)
        self.teiface = TrafficEngInterface.TrafficEngInterface(address,username,password)
        self.tetunp = TrafficEngTunnelPath.TrafficEngTunnelPath(address,username,password)
        self.tepstate =TrafficEngPathState.TrafficEngPathState(address,username,password)
        self.terstate = TrafficEngResvState.TrafficEngResvState(address,username,password)
        self.tetriface = TrafficEngTraffInterface.TrafficEngTraffInterface(address,username,password)
        self.mvpls = MplsVpls.MplsVpls(address,username,password)
        self.mbgp = MplsBgpVpls.MplsBgpVpls(address,username,password)
        self.mcisco = MplsCiscoBgpVpls.MplsCiscoBgpVpls(address,username,password)
        self.ipv6add = Ipv6Addresses.Ipv6Addresses(address,username,password)
        self.dhcpv6c = DHCPv6Client.Dhcpv6Client(address,username,password)
        self.dhcpr = DHCPrelay.Dhcpv6Relay(address,username,password)
        self.dhcps = DhcpServer.DhcpServer(address,username,password)
        self.pool = Pool.Pool(address,username,password)
        self.ipv6nd = Ipv6NeighborDiscovery.IPv6NeighborDiscovery(address,username,password)
        self.ipv6neig = Neighbors.Neighbors(address,username,password)
        self.ipv6set = IPv6Settings.Settings(address,username,password)
        self.ipv6rt = IPv6Route.IPv6Route(address,username,password)
        self.ipv6fw1 = FirewallFilter.FirewallFilter(address,username,password)
        self.ipv6fw2 = FirewallGeneralSetup.FirewallGeneralSetup(address,username,password)
        self.ipv6fw3 = FirewallAdvancedSetup.FirewallAdvancedSetup(address,username,password)
        self.ipv6fw4 = FirewallExtraSetup.FirewallExtraSetup(address,username,password)
        self.ipv6fw5 = FirewallActions.FirewallActions(address,username,password)
        self.ipv6fw6 = FirewallConenctions.FirewallConnections(address,username,password)
        self.ipv6fw7 = Ipv6AddressList.FirewallAddressList(address,username,password)
        self.ipv6mangle = FirewallMangle.FirewallMangle(address,username,password)
        self.ipv6raw = FirewallRaw.FirewallRaw(address,username,password)
        self.arp = Arp.Arp(address,username,password)
        self.accouting = Accounting.Accounting(address,username,password)
        self.addresses = Addresses.Addresses(address,username,password)
        self.dhclient = DhcpCLient.DhcpClient(address,username,password)
        self.dhrelay = DhcpRelay.DhcpRelay(address,username,password)
        self.dhcpserver1 = DhcpServer.DhcpServer(address,username,password)
        self.dnsglob = DNSglobal.DNSglobal(address,username,password)
        self.dnscache = DNScache.DNScache(address,username,password)
        self.dnsstatic = DNSstatic.DNSstatic(address,username,password)
        self.fw1 = FirewallFilter.FirewallFilter(address,username,password)
        self.fw2 = FirewallNAT.FirewallNAT(address,username,password)
        self.fw3 = FirewallMangle.FirewallMangle(address,username,password)
        self.fw4 = FireallGeneralSetup.FirewallGeneralSetup(address,username,password)
        self.fw5 = FirewallAdvancedSetup.FirewallAdvancedSetup(address,username,password)
        self.fw6 = FirewallExtraSetup.FirewallExtraSetup(address,username,password)
        self.fw7 = FirewallAction.FirewallActions(address,username,password)
        self.fwservice = FirewallServicePOrts.FirewallServicePOrts(address,username,password)
        self.fwconn = FirewallCOnnections.FirewallConnections(address,username,password)
        self.fwaddr = FirewallAddressist.FirewallAddressList(address,username,password)
        self.fwl7 = FirewallL7Protocols.FirewallL7Protocols(address,username,password)
        self.hpotserver = HotspotServer.HotspotServer(address,username,password)
        self.hpotserverprofile = HotspotServerProfile.HotspotServerProfile(address,username,password)
        self.hpotusers = HotspotUsers.HotspotUsers(address,username,password)
        self.hpotuprofiles = HotspotUserProfile.HotspotUserProfile(address,username,password)
        self.hactive = HotspotActive.HotspotActive(address,username,password)
        self.hsbind = HotspotIpBindings.HotspotIpBinding(address,username,password)
        self.hsport = HotspotServicePorts.HotspotServicePorts(address,username,password)
        self.hswg = HotspotWalledGarden.HotspotWalledGarden(address,username,password)
        self.hswgl = HotspotWalledGardenList.HotspotWalledGardenList(address,username,password)
        self.hscookie = HotspotCookies.HotspotCookies(address,username,password)
        self.ipsec1 = IPsecPolicies.IPsecPolicy(address,username,password)
        self.ipsec2 = IPsecGroups.IPsecGroups(address,username,password)
        self.ipsec3 = IpsecPeers.IPsecPeers(address,username,password)
        self.ipsec4 = IpsecRemotePeers.IPsecRemotePeers(address,username,password)
        self.ipsec5 = IPsecModeCOnfig.IPsecModeConfig(address,username,password)
        self.ipsec6 = IPsecProposal.IPsecProposal(address,username,password)
        self.ipsec7 = IpsecInstalledSa.IPsecInstalledSa(address,username,password)
        self.ipsec8 = IPsecKeys.IPsecKeys(address,username,password)
        self.ipsec9 = IPsecUsers.IPsecUsers(address,username,password)
        self.neig1 = NeighborLIst.NeighborList(address,username,password)
        self.neig2 = NeighborDIscovery.NeighborDiscovery(address,username,password)
        self.pack = Packing.Packing(address,username,password)
        self.pool1 = Pool.Pool(address,username,password)
        self.pool2 = PoolUsedAddresses.PoolUsedAddresses(address,username,password)
        self.route1 = RouteGeneral.RouteGeneral(address,username,password)
        self.route2 = RouteNexthops.RouteNexthops(address,username,password)
        self.route3 = RouteRules.RouteRules(address,username,password)
        self.route4 = RoouteVrf.RouteVrf(address,username,password)
        self.smb = Smb.Smb(address,username,password)
        self.smbshare = SmbShare.SmbShare(address,username,password)
        self.smbuser = SmbUsers.SmbUsers(address,username,password)
        self.snmp = Snmp.Snmp(address,username,password)
        self.snmpcomm = SnmpCommnity.SnmpCommunity(address,username,password)
        self.service = Services.Services(address,username,password)
        self.setting = Settings.Settings(address,username,password)
        self.socks = Socks.Socks(address,username,password)
        self.socksaccess = SocksAccess.SocksAccess(address,username,password)
        self.sockconn = SocksConnections.SocksConnections(address,username,password)
        self.tftp = Tftp.Tftp(address,username,password)
        self.trafficflow = TrafficFlow.TrafficFlow(address,username,password)
        self.trafficflow = TrafficFlowIpfix.TrafficFlowIpfix(address,username,password)
        self.upnpset = UpnpSetting.UpnpSetting(address,username,password)
        self.upnpiface = UpnpInterface.UpnpInterface(address,username,password)
        self.webproxyset = WebProxySettings.WebProxySettings(address,username,password)
        self.webproxylookup = WebProxyLookup.WebProxyLookup(address,username,password)
        self.webproxyinserts = WebProxyInserts.WebProxyInserts(address,username,password)
        self.webproxyrefreshes = WebProxyRefreshes.WebProxyRefreshes(address,username,password)
        self.webproxyaccess = WebProxyAccess.WebProxyAccess(address,username,password)
        self.webproxycache = WebProxyCache.WebProxycache(address,username,password)
        self.webproxydirect = WebProxyDirect.WebProxyDirect(address,username,password)
        self.webproxyconnections = WebProxyConnections.WebProxyConnections(address,username,password)
        self.webproxycachecontent = WebProxyCacheContetnt.WebProxyCacheContent(address,username,password)
        self.meshiface = MeshInterfaces.MeshInterfaces(address,username,password)
        self.meshport = MeshPorts.MeshPorts(address,username,password)
        self.meshfdb = MeshFdb.MeshFdb(address,username,password)
        self.switch = SwitchGeeral.SwitchGeneral(address,username,password)
        self.switchport = SwitchPorts.SwitchPorts(address,username,password)
        self.switchhost = SwitchHost.SwitchHost(address,username,password)
        self.switchvlan = SwitchVlan.SwitchVlan(address,username,password)
        self.switchrule = SwitchRule.SwitchRule(address,username,password)
        self.bridgegeneral = BridgeGeneral.BridgeGeneral(address,username,password)
        self.bridgeset = BridgeSettings.BridgeSettings(address,username,password)
        self.bridgeport = BridgePorts.BridgePorts(address,username,password)
        self.bridgehost = BridgeHosts.BridgeHosts(address,username,password)
        self.bridgemdb = BridgeMdb.BridgeMdb(address,username,password)
        self.bnat = bridgeNat.bridgeNat(address,username,password)
        self.bnatgen = bridgeNatGeneral.bridgeNatGeneral(address,username,password)
        self.bnatgenadv = bridgeNatAdvanced.bridgeNatAdvanced(address,username,password)
        self.bridgenatarp = bridgeArp.bridgeNatArp(address,username,password)
        self.bridgestp = bridgeNatStp.bridgeNatStp(address,username,password)
        self.bridgefilter = bridgeFilter.bridgefilter(address,username,password)
        self.bridgefiltact = bridgeFilterAction.bridgeFilterAction(address,username,password)
        self.bridgefiltadv = bridgeFilterAdvanced.bridgeFilterAdvanced(address,username,password)
        self.bridgefiltarp = bridgeFIlterArp.bridgeFilterArp(address,username,password)
        self.bridgegen = bridgeFilter.bridgefilter(address,username,password)
        self.bridgestp = bridgeNatStp.bridgeNatStp(address,username,password)
        self.bridgemsti = bridgeMSTI.bridgeMSTI(address,username,password)
        self.bridgemstoverride = bridgePortMstOverride.bridgeMstOverride(address,username,password)
        self.bridgenatact = bridgeNatAction.bridgeNatAction(address,username,password)
        self.bridgvlan = bridgeVlan.bridgeVlan(address,username,password)
        self.activeppp = activeConnections.activeCOnnections(address,username,password)
        self.l2tpclient = interfaceL2tpCLient.interfaceL2tpClientServer( address, username, password )
        self.l2tpclientgeneral = interfaceL2tpClientSetGeneral.interfaceL2tpClientSetGeneral( address, username, password )
        self.l2tpserver = interfaceL2tpServer.interfaceL2tpServer( address, username, password )
        self.l2tpserverbind = interfaceL2tpServerBinding.interfaceL2tpServerBinding( address, username, password )
        self.l2tpset = interfaceL2tpSet.interfaceL2tpServerSet( address, username, password )
        self.l2tpclient = interfaceL2tpCLient.interfaceL2tpClientServer( address, username, password )
        self.l2tpserverbind = interfaceL2tpServerBinding.interfaceL2tpServerBinding( address, username, password )
        self.l2tpset1 = interfaceL2tpSet.interfaceL2tpServerSet( address, username, password )
        self.ovpnclient = interfaceOvpnClient.interfaceOvpnClient( address, username, password )
        self.ovpnclientdial = interfaceOvpnClientSetDialOut.interfaceOvpnClientSetDialOut( address, username, password )
        self.ovpncclientgen = interfaceOvpnClientSetGeneral.interfaceOvpnClientSetGeneral( address, username, password )
        self.ovpnserver = interfaceOvpnServer.interfaceOvpnServer( address, username, password )
        self.ovpnserverbin = interfaceOvpnServerBinding.interfaceOvpnServerBinding( address, username, password )
        self.ovpnserverset = interfaceOvpnServerSet.interfaceOvpnServerBinding( address, username, password )
        self.pppclient = interfacePppClient.interfacePppclient(address,username,password)
        self.pppclientgen = interfacePppClientSetGeneral.interfacePppClientSetSetGeneral(address,username,password)
        self.pppclientppp = interfacePppClientSetPpp.interfacePppClientSetPpp(address,username,password)
        self.pppoeserver = interfacePppoe.interfacePppoeServerBinding(address,username,password)
        self.pppoeClient = interfacePppoeClient.interfacePppoeClient(address,username,password)
        self.pppoeClientdial = interfacePppoeClientSetDialOut.interfacePppoeClientSetDialOut(address,username,password)
        self.pppoeset = interfacePppoeSet.interfacePppoeServerSet(address,username,password)
        self.pppoegenset = interfacePppoeSetGeneral.interfacePppoeClientSetGeneral(address,username,password)
        self.pppserver = interfacePppServer.interfacePppServer(address,username,password)
        self.pppserverdial = interfacePppServerSetDialIn.interfacePppServerSetDialIn(address,username,password)
        self.pppservergen = interfacePppServerSetGeneral.interfacePppServerSetGeneral(address,username,password)
        self.pptpclient = interfacePptpClient.interfacePptpClient(address,username,password)
        self.pptpclientdial = interfacePptpCLientSetDialOut.interfacePptpClientSetDialOut(address,username,password)
        self.pptpclientgen = interfacePptpClientSetGeneral.interfacePppoeClientSetGeneral(address,username,password)
        self.pptpserver = interfacePptpServer.interfacePptpServer(address,username,password)
        self.pptpserbin = interfacePptpServerBinding.interfacePptpServer(address,username,password)
        self.pptpsergen = interfacePptpServerSetGeneral.interfacePptpServerSetGeneral(address,username,password)
        self.sstpserver = interfaceSstpServer.interfaceSstpServer(address,username,password)
        self.sstpserversetbin = interfaceSstpServerBinding.interfaceSstpServerBinding(address,username,password)
        self.sstpserverglob = interfaceSstpServerSet.interfaceSstpServerSetGeneral(address,username,password)
        self.sstpclient = interfaceSstpClient.interfaceSstpClient(address,username,password)
        self.sstpclientgen = interfaceSstpCLientGeneralSet.interfaceSstpClientSetGeneral(address,username,password)
        self.sstpclientdial = interfaceSstpClientSetDialOut.interfaceSstpClientSetDialOut(address,username,password)
        self.l2tpsecret = l2tpSecrets.l2tpSecrets(address,username,password)
        self.pppauth = pppAuthenticationAndAcounting.pppAuthenticationAndAcounting(address,username,password)
        self.pppoe = pppoe.pppoe(address,username,password)
        self.pppoeset = pppoeSettings.pppoeSettings(address,username,password)
        self.profgen = profileGeneral.profileGeneral(address,username,password)
        self.profLimit = profileLimits.profileLimits(address,username,password)
        self.profprot = profileProtocols.profileProtocols(address,username,password)
        self.profqueue = profileQueue.profileQueue(address,username,password)
        self.profiles = profiles.profiles(address,username,password)
        self.profilescript = profileScripts.profileScripts(address,username,password)
        self.secret = secrets.secrets(address,username,password)
        self.secretset = secretSettings.secretSettings(address,username,password)
        self.wchannel = channels.Channels(address,username,password)
        self.wchannelset = channelSet.ChannelsSet(address,username,password)
        self.security1 = securityProfile.securityProfile(address,username,password)
        self.security2 = securityProfileSetGeneral.securityProfileSetGeneral(address,username,password)
        self.security3 = securityProfileRadius.securityProfileRadius(address,username,password)
        self.security4 = securityProfileEap.securityProfileSetEap(address,username,password)
        self.security5 = securityProfileStaticKeys.securityProfileSetStaticKeys(address,username,password)
        self.conlist = connectList.connectList(address,username,password)
        self.connlistset = connectListSet.connectListSet(address,username,password)
        self.acl = accessList.accessList(address,username,password)
        self.aclset = accessListSet.accessListSet(address,username,password)
        self.nstream1 = NstremeDual.NstreamDual(address,username,password)
        self.nstreamsetgen = nstremeSetGeneral.NstreamSetGeneral(address,username,password)
        self.nstreamsetdual = nstreameSetDual.NstreamSetDual(address,username,password)
        self.nstreamrates = nstremeDataRates.NstreamSetDataRates(address,username,password)
        self.cap = interfaceCap.interfaceCap(address,username,password)
        self.wps = interfaceWpsCLient.interfaceWpsCLient(address,username,password)
        self.repeater = interfaceRepeater.interfaceRepeater(address,username,password)
        self.align = interfaceWirelessAllignement.interfaceWirelessAlignement(address,username,password)
        self.sniffer = interfaceSnifferSetting.interfaceWirelessSmiffer(address,username,password)
        self.snooper = wirelessSnooper.interfaceWirelessSnooper(address,username,password)
        self.virt = interfaceVirtual.interfaceVirtual(address,username,password)
        self.virtwireless = interfaceVirtualWirelessSet.interfaceVirtualWirelessAllignmentOnlySet(address,username,password)
        self.virtaligngen = interfaceVirtualGeneralSet.interfaceVirtualGeneralSet(address,username,password)
        self.virtapbridge = interfaceVirtualApbridgeSet.interfaceVirtualApbridgeSet(address,username,password)
        self.virtbridge = interfaceVirtualBridgeSet.interfaceVirtualBridgeSet(address,username,password)
        self.virtnstremeslave = interfaceVirtualNstreamDualSlave.interfaceVirtualNstreamDualSlave(address,username,password)
        self.virtnsslave = interfaceVirtualNstreamDualSlave.interfaceVirtualNstreamDualSlave(address,username,password)
        self.virtstation =interfaceVirtualStation.interfaceVirtualStation(address,username,password)
        self.virtstationbr = interfaceVirtualStationBridge.interfaceVirtualStationBridge(address,username,password)
        self.virtpsbr = interfaceVirtualStationPseudobridge.interfaceVirtualStationPseudobridge(address,username,password)
        self.virtclone = interfaceVirtualStationPseudoBridgeClone.interfaceVirtualStationPseudobridge(address,username,password)
        self.virtwds = interfaceVirtualWds.interfaceVirtualWds(address,username,password)
        self.wds = interfaceVirtualWds.interfaceVirtualWds(address,username,password)
        self.wdsslave = interfaceVirtualWdsSlave.interfaceVirtualWdsSLave(address,username,password)
        self.ifacelist = interfaces.interfaces(address,username,password)