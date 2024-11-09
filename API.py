import requests

URL = 'http://www.ulaval.ca/'

# récupérer le contenu de la ressource
rep = requests.get(URL)

if rep.status_code == 200:
    # la réponse est bonne, afficher son contenu
    print(rep.text)

else:
    # une erreur s'est produite, afficher le message d'erreur
    print(f"Le GET sur {URL} a produit le code d'erreur {rep.status_code}.")