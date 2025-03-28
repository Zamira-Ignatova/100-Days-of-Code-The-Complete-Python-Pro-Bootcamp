class FlightData:

    def __init__(self, price, departure_iata_code: str, arrival_iata_code: str, departure_date: str, return_date: str, layovers):
        """Constructor for creating a new flight data instance with specific travel details.
        Attributes:
        - price: The cost of the flight.
        - departure_iata_code: The IATA code for the flight's origin airport.
        - arrival_iata_code: The IATA code for the flight's destination airport.
        - departure_date: The departure date for the flight.
        - return_date: The return date for the flight.
        - layovers: 0 for direct flights. >= 1 for indirect flights """
        self.price = price
        self.departure_iata_code = departure_iata_code
        self.arrival_iata_code = arrival_iata_code
        self.departure_date = departure_date
        self.return_date = return_date
        self.layovers = layovers

def get_cheapest_flights(all_flights_data):
        """Assumes the first flight in the list is the cheapest one.
         After iterates through all available flights in the all_flights_data,
         updating the cheapest flight details whenever a lower-priced flight is encountered."""

        if all_flights_data is None or not all_flights_data.get('data'):
            print("There is no available flight data")
            cheapest_flight = FlightData(price="N/A", departure_iata_code="N/A",
                                         arrival_iata_code="N/A",
                                         departure_date="N/A", return_date="N/A",
                                         layovers="N/A")
            return cheapest_flight
        else:
            first_flight = all_flights_data['data'][0]
            lowest_price = float(first_flight["price"]["grandTotal"])
            departure_iata_code = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            #number of layovers = number of segments - 1
            number_of_layovers = len(first_flight["itineraries"][0]["segments"]) - 1
            arrival_iata_code = first_flight["itineraries"][0]["segments"][number_of_layovers]["arrival"]["iataCode"]
            departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0] # Return date is the first segment(index=0) of the second itinerary (index= 1)


            cheapest_flight = FlightData(price=lowest_price, departure_iata_code=departure_iata_code, arrival_iata_code=arrival_iata_code,
                                          departure_date=departure_date, return_date=return_date, layovers=number_of_layovers)

            for flight in all_flights_data["data"]:
                price = float(flight["price"]["grandTotal"])
                if price < lowest_price:
                    lowest_price = price
                    departure_iata_code = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    arrival_iata_code = flight["itineraries"][0]["segments"][number_of_layovers]["arrival"]["iataCode"]
                    departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                    return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                    cheapest_flight = FlightData(price=lowest_price, departure_iata_code=departure_iata_code,
                                                  arrival_iata_code=arrival_iata_code, departure_date=departure_date,
                                                  return_date=return_date,layovers=number_of_layovers)
                    print(f"Lowest price to {departure_iata_code} is ${lowest_price}")

            return cheapest_flight




