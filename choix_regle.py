
class Choix_regle:

   def __init__(self,rgs):
      self.regles=rgs


   def basique(self):
      return self.regles

   def plus_premisse(self):
      rgs=sorted(self.regles,key=lambda x:len(x.si),reverse=True)
      return rgs


   def plus_recent(self,fait):
    rgs=[]
    for i in self.regles:
    
       j=0
       aux=j<len(i.si)
       while(aux and i.si[j]!=fait):
         
         j+=1
         if(j>=len(i.si)):
            aux=False
         

       if(not(aux)):
          rgs.append(i)
       else:
          rgs.insert(0,i)

    return rgs      
       
          

             
          

       
         
      
      
   
      
         
         
      

