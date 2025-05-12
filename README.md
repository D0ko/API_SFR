# API SFR - TEST Dev

Ce projet a été réalisé lors d’un test technique pour intégrer une équipe au sein de SFR dans le cadre de mon alternance. 
L’objectif était d’évaluer mes compétences en développement Python, en intégration d’API tierces, et en gestion de serveur web minimaliste. 

## Files

-   [country.py](https://github.com/D0ko/API_SFR/blob/main/country.py): Fetches and displays country, region, and city data using the `universal-tutorial.com` API.
-   [index.py](https://github.com/D0ko/API_SFR/blob/main/index.py): A CGI script that handles user input for city, country, states, and cities to display weather information.
-   [meteo.py](https://github.com/D0ko/API_SFR/blob/main/meteo.py): Retrieves and displays weather information for a given city or ZIP code using the OpenWeatherMap API.
-   [server.py](https://github.com/D0ko/API_SFR/blob/main/server.py): Sets up a basic HTTP server to run the CGI script (`index.py`).

## Usage

1.  Run the `server.py` script to start the web server:

    ```bash
    python server.py
    ```

2.  Access the application in your web browser using the provided link (typically `http://localhost:8888/index.py`).
3.  Enter a city name or ZIP code in the input field and submit the form to view weather information.

## Note

-   The API keys in `country.py` and `meteo.py` might need to be updated for the application to function correctly.
