from Fait import fait
class but(fait):
    def __int__(self,a,op,v):
        if(op=="="):
            super().__init__(a,op,v)
        else:
            print("But non valide(pas le bon opérateur)")
        
