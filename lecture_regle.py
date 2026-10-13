from regle import Regle

def charger_regles(nom_fichier):
    tab=[]
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines()  # Retourne une liste

    for ligne in lignes:
        lg=ligne.strip().split()

        if lg!=[]:
            aux=lg[0]
            if aux=='PAQUET':

                print('paquet')

            else:
                if aux[0]=='R':
                    regle=Regle()
                    regle.nom=aux
                    i=3
                    #print(lg)
                    while lg[i]!='ALORS' and i<len(lg):
                      
                        if(lg[i]!='ET'):
                            a=lg[i]
                            #print('a '+a)
                            b=lg[i+1]
                            #print('b '+b)
                            c=lg[i+2]
                            #print('c ' +c)
                            i=i+3
                            regle.ajout_si(a,b,c)
                        else:
                            i=i+1
                    #print('test')
                    i+=1
                    while  i<len(lg):
                        if(lg[i]!='ET'):
                            a=lg[i]
                            #print('a '+a)
                            b=lg[i+1]
                            #print('b '+b)
                            c=lg[i+2]
                            #print('c ' +c)
                            i=i+3
                            regle.ajout_alors(a,b,c)
                        else:
                            i=i+1

                    tab.append(regle)
        

    return tab             # print(lg)