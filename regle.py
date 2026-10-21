




class Regle:
   
    def __init__(self):

        self.nom=''
        self.si = []
        self.alors = []

    def valid(self, cond, liste_fait):
        var_cond, op_cond, val_cond = cond
        if op_cond in ("=", "!="):
            for fait in liste_fait:
                var_fait, op_fait, val_fait = fait
                
                if var_cond == var_fait and val_cond == val_fait:
                    if op_fait == "=" and op_cond == "!=":
                        return False
                    elif op_fait == "=" and op_cond == "=":
                        return True
                        
        
            return op_cond == "!="
            
        
        elif op_cond in ("<", "<=", ">=", ">"):
            for fait in liste_fait:
                var_fait, op_fait, val_fait = fait
                
                if var_cond == var_fait:
                    try:
                        v_cond = int(val_cond)
                        v_fait = int(val_fait)
                        
                        if op_cond == "<" and v_cond < v_fait: return True
                        if op_cond == "<=" and v_cond <= v_fait: return True
                        if op_cond == ">" and v_cond > v_fait: return True
                        if op_cond == ">=" and v_cond >= v_fait: return True
                    except ValueError:
                        print("Problème de conversion entre int et string")
                        
            return False
            
        return False
            
                   
                    
    def verif(self, liste_fait):
        i = 0
        j = 0
        while(j<len(self.alors) and (self.valid(self.alors[j],liste_fait))):
            j+=1

        if(j<len(self.alors)):
            while(i<len(self.si) and (self.valid(self.si[i],liste_fait))):
                i += 1
        else:
            return False

        return i>=len(self.si)

    def verif_alors(self,but):
        return self.valid(but,self.alors)

    

    

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
