from data_manager import  DataManager
from  flight_search import FlightSearch
from flight_data import get_cheapest_flights
from notification_manager import NotificationManager
import  time
import datetime
import  dotenv
import os
dotenv.load_dotenv(dotenv_path="your own path to the .env file")

# constants
DEPARTURE_AIRPORT_IATA = "YOUR OWN IATA CODE"
TO_EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]

#variables
ongoing_day = datetime.datetime.now()
tomorrow = ongoing_day + datetime.timedelta(days=1)
one_week_after_tomorrow= ongoing_day + datetime.timedelta(days=7)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#Update the Airport Codes in Google Sheet
for destination in sheet_data:
    for key, value in destination.items():
        if destination['iataCode'] == "":
            destination['iataCode'] = flight_search.get_code_of_an_airport(city=destination['city'])
            time.sleep(2)
#print(f"The data from the Google Sheet: {sheet_data}")
sheet_data = data_manager.destination_data
data_manager.update_airport_code()

#searching flights
for destination in sheet_data:
    for key, value in destination.items():
        print(f"Finding the cheapest flight ✈️ to the {destination["city"]} ⏳")
        flights = flight_search.get_flights(departure_iata_code=DEPARTURE_AIRPORT_IATA, arrival_iata_code=destination["iataCode"],
                                  departure_date=tomorrow, return_date=one_week_after_tomorrow)
        cheapest_flight = get_cheapest_flights(flights)
        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            notification_manager.send_email(to_email_address=TO_EMAIL_ADDRESS,
                                            message=f"PRICE ALERT!\n"
                                                    f"There is a cheapest flight from the {cheapest_flight.departure_iata_code}"
                                                    f" to the {cheapest_flight.arrival_iata_code} for ${cheapest_flight.price}\n"
                                                    f" the departure is on {cheapest_flight.departure_date}, "
                                                    f" the return day is on {cheapest_flight.return_date}.")

