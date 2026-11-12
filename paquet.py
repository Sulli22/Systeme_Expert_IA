from regle import Regle

class Paquet:
    def __init__(self):
        self.premisses = []
        self.consequences = []
        self.regles = []

    def ajouterRegle(self, regle):
        for premisse in regle.si:
            if premisse not in self.premisses:
                self.premisses.append(premisse)

        for consequence in regle.alors:
            if consequence not in self.consequences:
                self.consequences.append(consequence)

        self.regles.append(regle)

    def __str__(self):
        resultat = "PAQUET \nPREMISSE\n" 
        for premisse in self.premisses:
            for i in premisse:
                resultat += i+" "

        resultat += "\nCONSEQUENCES\n"
        for consequence in self.consequences:
            for i in consequence:
                resultat += i+" "

        resultat += "\nREGLES\n"
        for r in self.regles:
            resultat += str(r) +"\n"
        resultat += "\n"
        return resultat