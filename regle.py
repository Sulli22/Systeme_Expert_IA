class Regle:
   
    def __init__(self):

        self.nom=''
        self.si = []
        self.alors = []

    def verif(self, liste_fait):
        i = 0
        while(i<len(self.si) and (self.si[i] in liste_fait)):
            i += 1

        return i>=len(self.si)
    

    def ajout_si(self, attribut, etat):
        if ((attribut is not None) and (etat is not None)):
            self.si.append((attribut, etat))

    def ajout_si(self, attribut,operateur, etat):
        if ((attribut is not None) and (etat is not None) and (operateur is not None)):
            self.si.append((attribut,operateur, etat))

        else:
            print("Problème sur l'attribut ou l'état")


    def ajout_alors(self, attribut, etat):
            if ((attribut is not None) and (etat is not None)):
                self.alors.append((attribut, etat))
    
            else:
                print("Problème sur l'attribut ou l'état")

    def ajout_alors(self, attribut,operateur, etat):
            if ((attribut is not None) and (etat is not None) and (operateur is not None)):
                self.alors.append((attribut,operateur, etat))
    
            else:
                print("Problème sur l'attribut ou l'état")

    def lecture(self):
        print(self.nom)
        print('SI')
        for i in self.si:
            print(i)
        print('ALORS')
        for j in self.alors:
            print(j)
