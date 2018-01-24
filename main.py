import Constructors

mikrotik = Constructors.Mikrotik(address="172.16.53.3",username="admin",password="admin")
mikrotik.system.shutdownRouter()