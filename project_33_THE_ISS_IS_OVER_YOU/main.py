import time
import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 25
MY_LONGITUDE = 147
FROM_EMAIL_ADDRESS = "sender_address"
PASSWORD = "password"
TO_ADDRESS = "recepient_address"
PORT = 465
SERVER_ADRESS = "server_adress"

def iss_is_over_you():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    if (MY_LATITUDE - 5) <= iss_latitude <= (MY_LATITUDE + 5) and (MY_LONGITUDE - 5) <= iss_longitude <= (MY_LONGITUDE + 5): #Your position is within +5 or -5 degrees of the ISS position.
        return  True

def it_is_dark():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
        "tzid": "Europe/Moscow",}
    response_sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sunrise_sunset.raise_for_status()
    data_sunrise_sunset = response_sunrise_sunset.json()
    sunrise = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sunrise_sunset["results"]["sunset"].split("T")[1].split(":")[0])
    ongoing_time = datetime.now()
    current_hour = ongoing_time.hour
    if sunset >= current_hour < sunrise:
        return True

while True:
    time.sleep(60)
    if iss_is_over_you() and it_is_dark():
            with smtplib.SMTP_SSL(SERVER_ADRESS, PORT) as connection:
                connection.login(user=FROM_EMAIL_ADDRESS, password=PASSWORD)
                connection.sendmail(
                    from_addr=FROM_EMAIL_ADDRESS,
                    to_addrs=TO_ADDRESS,
                    msg=f"Subject: LOOK UP! \nTHE ISS IS ABOVE YOU!")
