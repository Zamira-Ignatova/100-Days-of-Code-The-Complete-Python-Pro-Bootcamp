from pprint import pprint
import dotenv
import requests
import os

dotenv.load_dotenv(dotenv_path="/Users/zamiraignatova/PycharmProjects/day_39_/.venv/.env") # Load environment variables from .env file

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.HOST_DOMAIN = os.environ["HOST_DOMAIN"]
        self.USERNAME = os.environ["USERNAME"]
        self.AUTH_TOKEN = os.environ["AUTH_TOKEN"]
        self.PROJECT_NAME = os.environ["PROJECT_NAME"]
        self.SHEET_NAME = os.environ["SHEET_NAME"]
        self.headers = {"Authorization": os.environ["AUTH_TOKEN"]}

    def get_destination_data(self):
        """Uses the Sheety API to GET all the data in that sheet and print it out."""
        response_get = requests.get(
            url=f"{self.HOST_DOMAIN}/{self.USERNAME}/{self.PROJECT_NAME}/{self.SHEET_NAME}", headers=self.headers)
        response_get.raise_for_status()
        self.destination_data = response_get.json()['prices']
        pprint(self.destination_data)
        return self.destination_data

    def update_airport_code(self):
        """updates the Google Sheet with the IATA codes"""
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{self.HOST_DOMAIN}/{self.USERNAME}/{self.PROJECT_NAME}/{self.SHEET_NAME}/{city['id']}",
                json=new_data, headers=self.headers)
            response.raise_for_status()
            print(response.text)
