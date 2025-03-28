from data_manager import  DataManager
from  flight_search import FlightSearch
from flight_data import get_cheapest_flights
from notification_manager import NotificationManager
import  time
import datetime
import  dotenv
import os
from pprint import pprint

dotenv.load_dotenv(dotenv_path="/Users/zamiraignatova/PycharmProjects/day_39_/.venv/.env")

# constants
DEPARTURE_AIRPORT_IATA = "LON"
TO_EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
DAYS_OF_TRIP = 7
#variables
ongoing_day = datetime.datetime.now()
tomorrow = ongoing_day + datetime.timedelta(days=1)
days_of_trip = ongoing_day + datetime.timedelta(days=DAYS_OF_TRIP)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data_from_google_sheet()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#Update the Airport Codes in Google Sheet
for destination in sheet_data:
    for key, value in destination.items():
        if destination['iataCode'] == "":
            destination['iataCode'] = flight_search.get_iata_code_of_destination_airport(city=destination['city'])
            time.sleep(2)

sheet_data = data_manager.destination_data
data_manager.update_iata_code_in_google_sheet()

#Retrieve your customer emails
customer_data = data_manager.get_customer_emails()
pprint(customer_data)
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]
pprint(customer_email_list)

#searching for direct flights
for destination in sheet_data:
    for key, value in destination.items():
        print(f"Finding the cheapest flight ✈️ to the {destination["city"]} ⏳")
        direct_flights = flight_search.get_all_flights(departure_iata_code=DEPARTURE_AIRPORT_IATA, arrival_iata_code=destination["iataCode"],
                                                       departure_date=tomorrow, return_date=days_of_trip)
        cheapest_flight = get_cheapest_flights(direct_flights)
        print(f"Cheapest direct flight price to get to {destination['city']} is £{cheapest_flight.price}")
        time.sleep(2)
# searching for indirect flights
        if cheapest_flight.price != "N/A":
            print(f"No direct flights to {destination['city']} are available right now. We are looking for indirect flights ⏳")
            indirect_flights = flight_search.get_all_flights(departure_iata_code=DEPARTURE_AIRPORT_IATA,
                                                           arrival_iata_code=destination["iataCode"],
                                                           departure_date=tomorrow, return_date=days_of_trip, is_direct_flight=False)
            cheapest_flight = get_cheapest_flights(indirect_flights)
            print(f"Cheapest indirect flight price to get to {destination['city']} is £{cheapest_flight.price}")
        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            if cheapest_flight.layovers == 0:
                message = (f"There is a cheapest flight from the {cheapest_flight.departure_iata_code}"
                           f" to the {cheapest_flight.arrival_iata_code} for ${cheapest_flight.price}.\n"
                           f" The departure is on {cheapest_flight.departure_date},"
                           f" the return day is on {cheapest_flight.return_date}.")
            else:
                message = (
                    f"There is a cheapest flight from the {cheapest_flight.departure_iata_code}"
                    f" to the {cheapest_flight.arrival_iata_code} with {cheapest_flight.layovers} layover(s)"
                    f" for ${cheapest_flight.price}.\n The departure is on {cheapest_flight.departure_date},"
                    f" the return day is on {cheapest_flight.return_date}.")
            notification_manager.send_email(email_list=customer_email_list, message_body=message)

