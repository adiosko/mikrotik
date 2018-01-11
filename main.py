import Constructors

mikrotik = Constructors.Mikrotik(address="172.16.53.2",username="admin",password="admin")
mikrotik.prp.addRp("172.16.53.2")