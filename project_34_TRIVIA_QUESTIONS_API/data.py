import requests

parameters = {
    "amount": 20,
    "difficulty": "medium",
    "type": "boolean",
}
response_data = requests.get(url="https://opentdb.com/api.php", params=parameters)
response_data.raise_for_status()
data = response_data.json()
question_data = data["results"]



