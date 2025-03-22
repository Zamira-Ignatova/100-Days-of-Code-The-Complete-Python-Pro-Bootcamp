import requests
import  datetime
import time
import  os

#set environment variables
os.environ["APPLICATION_ID_NUTRITIONIX"] = "yourOwnId"
os.environ["APPLICATION_KEY_NUTRITIONIX"] = "youtOwnKey"
os.environ["USERNAME"] = "yourOwnUserName"
os.environ["SHEETY_AUTH_TOKEN"] = "your own token"
os.environ["PROJECT_NAME"] = "projectName"
os.environ["SHEET_NAME"] = "sheet_name"

#get environment variables
APPLICATION_ID_NUTRITIONIX = os.environ.get("APPLICATION_ID_NUTRITIONIX")
APPLICATION_KEY_NUTRITIONIX = os.environ.get("APPLICATION_KEY_NUTRITIONIX")
USERNAME = os.environ.get("USERNAME")
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
PROJECT_NAME = os.environ.get("PROJECT_NAME")
SHEET_NAME = os.environ.get("SHEET_NAME")

#constants
HOST_DOMAIN_NUTRITIONIX = "https://trackapi.nutritionix.com"
ENDPOINT_EXERCISE_NUTRITIONIX = "/v2/natural/exercise"
WEIGHT = int
HEIGHT_CM = int
AGE = int
HOST_DOMAIN_SHEETY = "https://api.sheety.co"
ENDPOINT_SHEETY = f"/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

user_query = input("What did you do today?\n")

headers_nutritionix = {
    "x-app-id": APPLICATION_ID_NUTRITIONIX,
    "x-app-key": APPLICATION_KEY_NUTRITIONIX,
}
parameters_nutritionix = {
    "query": user_query,
    "weight_kg": float(WEIGHT),
    "height_cm": float(HEIGHT_CM),
    "age": AGE,
}
response_nutritionix = requests.post(url=f"{HOST_DOMAIN_NUTRITIONIX}{ENDPOINT_EXERCISE_NUTRITIONIX}",
                                     json=parameters_nutritionix, headers=headers_nutritionix)
response_nutritionix.raise_for_status()
results = response_nutritionix.json()

duration = str(results["exercises"][0]["duration_min"])
exercise = str(results["exercises"][0]["name"])
calories = str(results["exercises"][0]["nf_calories"])
current_date = datetime.date.today()
current_date_formated = current_date.strftime("%d/%m/%Y")
current_time = time.time()
current_formatted_time = time.strftime("%X", time.localtime(current_time))

headers_sheety = {
    "Authorization": SHEETY_AUTH_TOKEN
}
parameters_sheety = {
    SHEET_NAME: {
        "date": current_date_formated,
        "time": current_formatted_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
}
}
response_sheety = requests.post(url=f"{HOST_DOMAIN_SHEETY}{ENDPOINT_SHEETY}",
                                     json=parameters_sheety, headers=headers_sheety)
response_sheety.raise_for_status()
results = response_sheety.json()
