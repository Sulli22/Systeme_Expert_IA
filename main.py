from baseFaits import BaseFaits
from regle import Regle
from lecture_regle import charger_regles
from strategies import chainage_avant,chainage_arriere
from optimisation import plus_de_premisses

"""regle = Regle()
regle.ajout_si("a", 1)

regle.ajout_alors("c", 3)

baseFaits = BaseFaits([("a",1), ("b",2)])
print(baseFaits.faits)
baseFaits.ajout_fait(regle)

print(baseFaits.faits)

print(baseFaits.faits)"""

tab=charger_regles('data/regle_diag_ordi.txt')
tabSansPaquets = tab["regles_sans_paquets"]
tabPaquets = tab["regles_paquets"]
tabSansPaquets = plus_de_premisses(tabSansPaquets)
base=BaseFaits([])
base.charger_fait('data/fait.txt')
for i in tabPaquets:
    print(i)
for i in tabSansPaquets:
   print(i)






chainage_avant(base,tabSansPaquets)


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
"""