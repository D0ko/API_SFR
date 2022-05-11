import requests
import json


API = "fe82fec2fe9b13954c3094329476e236"
CITY = "Paris"



class webservice:
    """
        class python pour obtenir meteo d'une ville (ZIP code / nom), utilisant l'API de Curretn weather data
    """
    def getweather(self, zip_code, nom_ville):
        # On entre soit un ZIP code, soit le nom d'une ville
        if zip_code is not None:
            # Lorsqu'on a un ZIP code (ex: '75001')
            self.zip_code = zip_code
            self.url = "https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=%s" % (zip_code, API)
        else:
            # Lorsqu'on a le nom d'une ville (ex: 'Paris')
            self.nom_ville = nom_ville
            self.url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (nom_ville, API)
        # On demande la recherche
        resultat = requests.get(self.url)
        # On enregistre la data obtenue
        self.data = json.loads(resultat.text)
    
    def printdata(self):
        # Affiche la data obtenue en brut
        print(self.data)

    def printweather(self):
        # Affichage terminal: - Location, - Temps, - Desciption du temps, - Si nuageux ou pas
        print("Location =", self.data['name'])
        print("temps =", self.data['weather'][0]['main'])
        print("description =", self.data['weather'][0]['description'])
        if self.data['clouds']['all'] == 0:
            print("Pas de Nuage")
        else:
            print("Nuageux")
    
    def affichageWebWeather(self):
        # Affichage serveur WEB (idem)
        # On utilise <br> pour les retours a la ligne (HTML)
        # Ici on utilise try pour prendre en compte lorsqu'aucune ville n'a ete saisie, il n'y a alors pas de data
        try:
            if self.data['clouds']['all'] == 0:
                affichage = "Location = %s<br>temps = %s<br>description = %s<br>Pas de nuage" % (self.data['name'], self.data['weather'][0]['main'], self.data['weather'][0]['description'])
            else:
                affichage = "Location = %s<br>temps = %s<br>description = %s<br>Nuageux" % (self.data['name'], self.data['weather'][0]['main'], self.data['weather'][0]['description'])
            print(affichage)
        except:
            pass



weather = webservice()
weather.getweather(None, CITY)
weather.printweather()

"""
Pour tester la class :
j'initisalise une ville dans <CITY>
j'ai cree la fonction printweather pour afficher les informations essentiels recuperee de data
je regarde la coherence des resultats
je test plusieurs ville (Paris, London, Berlin, Meaux, ...) et ZIP-code (75001, 77100, ...)
"""
