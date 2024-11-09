import requests

# récupérer le contenu du serveur
URL = 'https://pax.ulaval.ca/'

#Authentification du joueur
def authentification(idul, secret):
    # Nous passons les informations d'authentification au serveur
    # en utilisant le paramètre nommé «auth».
    rep = requests.get(URL, auth=(idul, secret))
    print(rep.text)

#vérification du serveur
if rep.status_code == 200:
    # la réponse est bonne, afficher son contenu
   # print(rep.text)
   print("Vous avez bien accédé au serveur de PAX")

else:
    # une erreur s'est produite, afficher le message d'erreur
    print(f"Le GET sur {URL} a produit le code d'erreur {rep.status_code}.")




#initialiser_partie 

#jouer_un_coup