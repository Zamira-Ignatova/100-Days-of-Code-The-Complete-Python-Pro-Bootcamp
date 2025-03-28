from pprint import pprint
import dotenv
import requests
import os

dotenv.load_dotenv(dotenv_path="/Users/zamiraignatova/PycharmProjects/day_39_/.venv/.env") # Load environment variables from .env file

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}
        self.HOST_DOMAIN = os.environ["HOST_DOMAIN"]
        self.USERNAME = os.environ["USERNAME"]
        self.AUTH_TOKEN = os.environ["AUTH_TOKEN"]
        self.PROJECT_NAME = os.environ["PROJECT_NAME"]
        self.SHEET_NAME_PRICES = os.environ["SHEET_NAME_PRICES"]
        self.SHEET_NAME_USERS = os.environ["SHEET_NAME_USERS"]
        self.headers = {"Authorization": os.environ["AUTH_TOKEN"]}

    def get_destination_data_from_google_sheet(self):
        """Uses the Sheety API to GET all the data in that sheet and print it out."""
        response = requests.get(
            url=f"{self.HOST_DOMAIN}/{self.USERNAME}/{self.PROJECT_NAME}/{self.SHEET_NAME_PRICES}", headers=self.headers)
        response.raise_for_status()
        self.destination_data = response.json()['prices']
        pprint(self.destination_data)
        return self.destination_data

    def update_iata_code_in_google_sheet(self):
        """updates the Google Sheet with the IATA codes"""
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{self.HOST_DOMAIN}/{self.USERNAME}/{self.PROJECT_NAME}/{self.SHEET_NAME_PRICES}/{city['id']}",
                json=new_data, headers=self.headers)
            response.raise_for_status()
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            url=f"{self.HOST_DOMAIN}/{self.USERNAME}/{self.PROJECT_NAME}/{self.SHEET_NAME_USERS}",
            headers=self.headers)
        response.raise_for_status()
        self.customer_data = response.json()['users']
        pprint(self.customer_data)
        return self.customer_data

