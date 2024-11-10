#import API

liste_joueurs = ["valiv", "robot"]

#formater_entête
def formater_entête(joueur1, joueur2):
    print("Légende:\n","X="+joueur1,"\n","O="+joueur2)

formater_entête(liste_joueurs[0], liste_joueurs[1])