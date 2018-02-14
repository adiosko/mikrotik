import Constructors

mikrotik = Constructors.Mikrotik(address="192.168.1.1",username="admin",password="admin")
mikrotik.switchvlan.listVlans()