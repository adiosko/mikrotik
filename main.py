import Constructors

mikrotik = Constructors.Mikrotik(address="172.16.53.2",username="admin",password="admin")
mikrotik.chain.setOspfType("0","external-type-1")