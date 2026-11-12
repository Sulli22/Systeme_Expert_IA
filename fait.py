class Fait:
   def  __init__(self,a,op,v):
    self.attribut=a
    self.operateur=op
    self.valeur=v


   def __eq__(self, other):
   
    if not isinstance(other, fait):
      return False
   
    return self.attribut == other.attribut and self.operateur == other.operateur and self.valeur==other.valeur

   def __str__(self):
     return self.attribut+" "+self.operateur+" "+self.valeur





