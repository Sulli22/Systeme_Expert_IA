from baseFaits import BaseFaits
from regle import Regle

regle = Regle()
regle.ajout_si("a", 1)

regle.ajout_alors("c", 3)

baseFaits = BaseFaits([("a",1), ("b",2)])
print(baseFaits.faits)
baseFaits.ajout_fait(regle)
print(baseFaits.faits)