import requests

URL = "https://www.universal-tutorial.com/api/getaccesstoken"
API = "rQUNO7J5_CEmlPxQx1WgSS5NCsM6Q2pP-eFfpC881Fp1HbIC49R1VZKwWZxe5O2Aaxw"
MAIL = "benesby.quentin@gmail.com"



resultat = requests.get(URL, headers={"Accept": "application/json",
"api-token": API,
"user-email": MAIL})

print(resultat)


"Impossible d'obtenir l'API"