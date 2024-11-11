#import API

joueurs = ["valiv", "robot"]
état_jeu = " "
plateau = [[" ", " ", "X", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "O"],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],]
état_plateau = {"joueurs": joueurs, "plateau": plateau}

#Fonction formater_entête (3 de 7)
def formater_entête(joueur1, joueur2):
    print("Légende:\n","X="+joueur1,"\n","O="+joueur2)

formater_entête(joueurs[0], joueurs[1])

#Fonction formater_le_damier (4 de 7)
def formater_le_damier(état_plateau):
    plateau = état_plateau.get("plateau")
    nb = 1
    newligne = ""
    plateau_ascii = "   -------------------\n"

    for ligne in plateau:
          newligne = " | ".join(str(case) for case in ligne)
        
          if nb <= 4:
            plateau_ascii += str(nb) + " | " + newligne + " |\n"
            plateau_ascii += "  |---|---|---|---|---|\n"
            nb += 1
          else: 
             plateau_ascii += str(nb) + " | " + newligne + " |\n"
             plateau_ascii += "--|---|---|---|---|---|\n" + "  | 1   2   3   4   5 |"
              
    return plateau_ascii
formater_le_damier(état_plateau)
print(formater_le_damier(état_plateau))

#Fonction formater_le_jeu (5 de 7)
#def formater_le_jeu








#Fonction choisir_un_coup (6 de 7)



#Fonction interpréter_la_commande (7 de 7)