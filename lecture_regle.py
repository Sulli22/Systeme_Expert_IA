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
                    lg_split = ligne.strip().split(" : ")
                    r = lg_split[1].split(" ALORS ")
                    si = r[0].split("SI ")[1]
                    si_split = si.split(" ET ")
                    for s in si_split:
                        s_aux = s.split()
                        regle.ajout_si(s_aux[0], s_aux[1], s_aux[2])
                    
                    alors = r[1]
                    alors_split = alors.split(" ET ")
                    for a in alors_split:
                        a_aux = a.split()
                        regle.ajout_alors(a_aux[0], a_aux[1], a_aux[2])

                    #print(lg)
                   
                    tab.append(regle)
        
    return tab             # print(lg)