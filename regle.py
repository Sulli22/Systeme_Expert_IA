class Regle:
   
    def __init__(self):

        self.nom=''
        self.si = []
        self.alors = []

    def verif(self, liste_fait):
        i = 0
        j = 0
        while(j<len(self.alors) and (self.alors[j] in liste_fait)):
            j+=1

        if(j<len(self.alors)):
            while(i<len(self.si) and (self.si[i] in liste_fait)):
                i += 1
        else:
            return False

        return i>=len(self.si)

    def verif_alors(self,but):
        return but in self.alors

    

    

    def ajout_si(self, attribut,operateur, etat):
        if ((attribut is not None) and (etat is not None) and (operateur is not None)):
            self.si.append((attribut,operateur, etat))

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
