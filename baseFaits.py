from regle import Regle

class BaseFaits:
    def __init__(self, liste_faits):
        self.faits = liste_faits

    def __contains__(self, item):     #methode permettant de redéfinir le IN 
        return item in self.faits



    def charger_fait(self,nom_fichier):
       
        with open(nom_fichier, 'r') as f:
            lignes = f.readlines()  # Retourne une liste

            for ligne in lignes:
                lg=ligne.strip().split()
                
               

                if lg!=[]:
                        
                        i=0
                        #print(lg)
                        while i<(len(lg)-1):
                            
                            if(lg[i]!='ET'):
                                a=lg[i]
                                    #print('a '+a)
                                b=lg[i+1]
                                    #print('b '+b)
                                c=lg[i+2]
                                    #print('c ' +c)
                                i=i+3
                              
                                self.faits.append((a,b,c))
                            else:
                                i=i+1
                            #print('test')
                    
                        
                
            

        

    def ajout_fait(self, regle):
        if regle.verif(self.faits):
            for alors in regle.alors:
                self.faits.append(alors)


    def but_atteint(self):
        for i in self.faits:
            if 'cause_racine' == i[0]:
                return True

        return False
