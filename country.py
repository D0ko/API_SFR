from itertools import count
import requests
import json


class webservice2:
    """
        class pour l'affichage et le stockage de donnees des pays, de leur regions, et de leurs villes
    """
    def __init__(self):
        URL1 = "https://www.universal-tutorial.com/api/getaccesstoken"
        URL2 = "https://www.universal-tutorial.com/api/countries/"
        API = "a4Ui3bJ3rhrd4vkYVTJ-kjvFiNnI2Q5GG1VK4NO3TjJ-fZH-G8zQV2sglUUoeUGkLl8"
        MAIL = "quentin.benesby@gmail.com"

        params = {"Accept": "application/json", "api-token": API, "user-email": MAIL}
        reponse = requests.get(URL1, headers = params)
        token = json.loads(reponse.text)['auth_token']

        self.params2 = {"Authorization": "Bearer " + str(token), "Accept": "application/json"}
        reponse2 = requests.get(URL2, headers = self.params2)
        self.data = json.loads(reponse2.text)
    
    def affiche_country(self):
        # affiche tous les pays
        for i in self.data:
            print(i["country_name"])
    
    def affiche_states(self, country):
        # affiche toutes les regions d'un pays
        for i in self.data:
            if country == i["country_name"]:
                URL = "https://www.universal-tutorial.com/api/states/%s" % (country)
                reponse = requests.get(URL, headers = self.params2)
                states = json.loads(reponse.text)
                for k in states:
                    print(k["state_name"])
                break
    
    def affiche_cities(self, states):
        # affiche toutes les villes d'une region
        URL = "https://www.universal-tutorial.com/api/cities/%s" % (states)
        reponse = requests.get(URL, headers = self.params2)
        cities = json.loads(reponse.text)
        for k in cities:
            print(k["city_name"])

data = webservice2()

#data.affiche_country()
#data.affiche_states('France')
data.affiche_cities('Seine-et-Marne')
    
