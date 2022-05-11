# coding: utf-8

import cgi
from meteo import webservice  # on import la class webservice

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

# on recupere la zone de saisie
city = form.getvalue("city")
country = form.getvalue("country")
states = form.getvalue("states")
cities = form.getvalue("cities")
mail = form.getvalue("mail")
nom = form.getvalue("nom")
commentaire = form.getvalue("commentaire")

print(mail, nom)
print(commentaire)


# code html simple pour afficher la page
html = """<!DOCTYPE html>
<head>
    <title>Service Meteo</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="city" value="ZIP code / nom" />
        <input type="submit" name="send" value="Valider">
        <input type="text" name="country" value="country" />
        <input type="text" name="states" value="states" />
        <input type="text" name="cities" value="cities" />
        <input type="submit" name="send" value="Valider">
        <input type="text" name="mail", value="mail" />
        <input type="text" name="nom", value="nom" />
        <input type="text" name="commentaire", value="commentaire" />
        <input type="submit" name="send" value="Send">
    </form> 
</body>
</html>
"""

# On cree le service
weather = webservice()


if cities != None and states != None and country != None:
    weather.getweather2(cities, states, country)
    weather.affichageWebWeather()

# Lorsqu'une ville a ete entree
if city == None:
    # Tant que la ville n'est pas entree
    pass

else:
    if city.isnumeric():
        # On test si nous avons un ZIP code (grace a isnumeric())
        weather.getweather(city, None)
    else:
        # Si nous n'avons pas de ZIP code
        weather.getweather(None, city)
    # On affiche WebWeather (pour serveur WEB)
    weather.affichageWebWeather()

print(html)


"""
Pour tester l'application, j'ai d'abord cree une zone de texte puis un bouton pour recuperer la saisie
j'ai ensuite lié l'étape 1 (recuperer les donnees meteo d'une ville) a celle-ci
j'ai cree une nouvelle fonction dans la class pour l'affichage sur serveur WEB (utilisation des <br> notamment)
Je re-test avec plusieurs ville (Paris, London, Berlin, Meaux, ...) et plusieurs ZIP-code (75001, 77100, ...)
"""



"""
On test avec par exemple :
(France / Seine-et-Marne / Meaux)
ou encore 
(France / Val-de-Marne / Créteil)
"""
