import Constructors

mikrotik = Constructors.Mikrotik(address="172.16.53.2",username="admin",password="admin")
mikrotik.proxy.setQueryInterval("00:05:00")
mikrotik.proxy.setDownstreamInterface("1","ether1")