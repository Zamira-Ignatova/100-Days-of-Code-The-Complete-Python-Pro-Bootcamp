import os
import dotenv
import requests
from datetime import datetime
dotenv.load_dotenv(dotenv_path="/Users/zamiraignatova/PycharmProjects/day_39_/.venv/.env")

#constants
ADULTS = 1
CHILDREN = 0
INFANTS = 0
NONSTOP = "true"
CURRENCY = "USD"
MAX = 10

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._host_domain_amadeus = "https://test.api.amadeus.com/v1"
        self._iata_end_point = "reference-data/locations/cities"
        self._token_end_point = "security/oauth2/token"
        self._flight_offers_search_end_point = "test.api.amadeus.com/v2/shopping/flight-offers"
        self.airport_code = ""
        self._api_key = os.environ["API_KEY_AMADEUS"]
        self._api_secret = os.environ["API_SECRET_AMADEUS"]
        self._token = self.get_new_token()

    def get_code_of_an_airport(self, city):
        """Retrieves the IATA code for a specified city using the Amadeus Location API."""
        _end_point = f"{self._host_domain_amadeus}/{self._iata_end_point}"
        header = {"Authorization": f"Bearer {self._token}"}
        parameters = {
                "keyword": city,
                "max": 3,
                "include": "AIRPORTS"}
        response = requests.get(url=_end_point, params=parameters, headers=header)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            airport_code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        return airport_code

    def get_new_token(self):
        """request a new token using your API keys for accessing Amadeus API"""
        _end_point = f"{self._host_domain_amadeus}/{self._token_end_point}"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {"grant_type": "client_credentials",
                     "client_id": self._api_key,
                     "client_secret": self._api_secret, }
        response = requests.post(url=_end_point, data=body, headers=header)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_flights(self, departure_iata_code: str, arrival_iata_code: str, departure_date, return_date):
        _end_point = f"{self._host_domain_amadeus}/{self._flight_offers_search_end_point}"
        header = {"Authorization": f"Bearer {self._token}"}
        parameters = {"originLocationCode": departure_iata_code,
                "destinationLocationCode": arrival_iata_code,
                "departureDate": departure_date.strftime("%Y-%m-%d"),
                "returnDate": return_date.strftime("%Y-%m-%d"),
                "adults": ADULTS,
                "children": CHILDREN,
                "infants": INFANTS,
                "nonStop": NONSTOP,
                "currencyCode": CURRENCY,
                "max": MAX,
                }
        response = requests.get(url=_end_point, params=parameters, headers=header)
        all_flights_data = response.json()
        print(f"Status code: {response.status_code}.")
        if response.status_code != 200:
            print(f"{response.text}\n Please re-check the parameters of your flight")
            return None
        return all_flights_data



