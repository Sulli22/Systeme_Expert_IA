from baseFaits import BaseFaits
from regle import Regle
from lecture_regle import charger_regles
from strategies import chainage_avant,chainage_arriere

"""regle = Regle()
regle.ajout_si("a", 1)

regle.ajout_alors("c", 3)

baseFaits = BaseFaits([("a",1), ("b",2)])
print(baseFaits.faits)
baseFaits.ajout_fait(regle)

print(baseFaits.faits)

print(baseFaits.faits)"""

tab=charger_regles('regle_diag_ordi.txt')
base=BaseFaits([])
base.charger_fait('fait.txt')
#for i in tab:
   # i.lecture()
"""

for i in base.faits:
    print(i)

if base.but_atteint():
    print("test accomplie")

chainage_avant(base,tab)


for i in base.faits:
    print(i)

if base.but_atteint():
    print("test accomplie")
"""
but_final = ("cause_racine", "=", "panne_alimentation_a_confirmer")

succes = chainage_arriere(base, tab, but_final)

if succes:
  print("Diagnostic réussi : La cause racine a été prouvée !")
else:
  print("Impossible de prouver cette cause avec les faits fournis.")