import requests
import  datetime

TOKEN = "{your_won_token}"
USERNAME = "{your_won_user_name}"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}
current_date = datetime.date.today()
current_date_formated = current_date.strftime("%Y%m%d")

user_creating_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response_user_creating_response = requests.post(url=pixela_endpoint, json=user_creating_param)
print(response_user_creating_response.text)

graph_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_create_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "float",
    "color": "ajisai"
}
response_create_graph = requests.post(url=graph_create_endpoint, json=graph_create_config, headers=headers)
print(response_create_graph.text)

graph_post_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_create_config["id"]}"
graph_post_a_value_config = {
    "date": current_date_formated,
    "quantity": "2"
}
response_post_value_in_graph = requests.post(url=graph_post_a_pixel_endpoint, json=graph_post_a_value_config, headers=headers)
print(response_post_value_in_graph.text)

graph_update_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_create_config["id"]}/{current_date_formated}"
graph_update_a_pixel_config = {
    "quantity": "120"
}
response_update_a_pixel_in_graph = requests.put(url=graph_update_a_pixel_endpoint, json=graph_update_a_pixel_config, headers=headers)
print(response_update_a_pixel_in_graph.text)

graph_delete_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_create_config["id"]}/{current_date_formated}"

response_delete_a_pixel_in_graph = requests.delete(url=graph_delete_a_pixel_endpoint, headers=headers)
print(response_delete_a_pixel_in_graph.text)
