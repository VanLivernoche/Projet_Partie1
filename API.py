import requests

# récupérer le contenu du serveur
URL = 'https://pax.ulaval.ca/'

#initialiser_partie 
#Authentification du joueur


def authentification(idul, secret):
    # Nous passons les informations d'authentification au serveur
    # en utilisant le paramètre nommé «auth».
    rep = requests.post(URL, auth=(idul, secret))
  # return l'identifiant de la partie (une chaîne)
    print(rep.text)
    print(rep.status_code)
  # return la liste des joueurs (une liste de chaînes)

  # return l'état du plateau (une liste; voir plus loin dans cet énoncé)
authentification("valiv", "b009f928-90fb-42c8-877f-1bb2e450ae1d")


#vérification du serveur





#jouer_un_coup