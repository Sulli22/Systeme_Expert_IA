from baseFaits import BaseFaits
from regle import Regle


def chainage_avant(BaseFaits, Regles):
  i = 0
  while not (BaseFaits.but_atteint()) and i < len(Regles):  # Boucle qui continue tant que notre base de faits n'a pas atteint une conclusion, ou tant qu'il reste des règles à tester
    if Regles[i].verif(BaseFaits.faits):  # On vérifie si la règle est utilisable avec notre base de faits
      BaseFaits.ajout_fait(Regles[i])  # Si la règle est vérifiée, on ajoute alors les faits déduits de cette règle
      i = 0 # On remet i à 0 afin de pouvoir revérifier les règles avec les nouveaux faits
    else:
      i += 1


def chainage_arriere(BaseFaits, Regles, but, en_cours=None):  # Ici, on définit une variable qui sert de mémoire temporaire pour la fonction
  if (en_cours is None):  # Si la variable n'est pas définie, on la définit (vide)
    en_cours = set()

  if (but in BaseFaits):  # Si le but qu'on cherche à prouver est déjà dans la base de faits, pas besoin d'aller plus loin
    return True

  if (but in en_cours):  # Si le but est dans notre mémoire temporaire, alors on coupe direct cette branche de recherche pour eviter une boucle infinie
    return False

  en_cours.add(but)  # On ajoute le but à notre mémoire temporaire

  for k in Regles:  # On parcourt les règles
    if (k.verif_alors(but)):  # On cherche les règles telles que notre but est une conclusion de celle-ci
      aux = True
      for i in k.si:  # On parcourt les conditions de la règle
        aux = aux and chainage_arriere(BaseFaits, Regles, i, en_cours)  # Pour chaque condition, on vérifie si elle mène bien à des faits de notre base de faits
      if aux:  # Si tous les faits trouvés sont bien présents dans la base de faits, on nettoie notre mémoire temporaire et on renvoie True
        en_cours.remove(but)
        return True

  en_cours.remove(but)
  return (False )  # Si on arrive jusque-là, cela signifie que le but initial ne peut pas être vérifié avec nos règles et notre base de faits actuelle