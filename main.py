import Constructors

mikrotik = Constructors.Mikrotik(address="172.16.53.2",username="admin",password="admin")
mikrotik.bgpact.setAppenfBgpCommunities("0","no-export")