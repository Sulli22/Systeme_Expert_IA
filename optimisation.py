from regle import Regle

def plus_de_premisses(regles):
    return sorted(regles, key=lambda regle: len(regle.si), reverse=True)