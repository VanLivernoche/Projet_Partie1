#import API

joueurs = ["valiv", "robot"]
état_jeu = " "
état_plateau = [[" ", " ", "X", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "O"],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],]

#Fonction formater_entête (3 de 7)
def formater_entête(joueur1, joueur2):
    format_joueurs = "Légende:\n" + "   X="+ joueur1 + "\n"+"   O="+joueur2
    return format_joueurs 

#print(formater_entête(joueurs[0], joueurs[1]))

#Fonction formater_le_damier (4 de 7)
def formater_le_damier(état_plateau):
    nb = 1
    newligne = ""
    plateau_ascii = "   -------------------\n"

    for ligne in état_plateau:
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
#print(formater_le_damier(état_plateau))

#Fonction formater_le_jeu (5 de 7)
def formater_le_jeu(joueurs, état_plateau):
    joueur1 = joueurs[0]
    joueur2 = joueurs[1]
    print(formater_entête(joueur1, joueur2))
    print(formater_le_damier(état_plateau))


formater_le_jeu(joueurs, état_plateau)








#Fonction choisir_un_coup (6 de 7)



#Fonction interpréter_la_commande (7 de 7)