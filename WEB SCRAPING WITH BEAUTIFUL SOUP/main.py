import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")
list_of_elements = soup.find_all(name="h3", class_="title")
list_of_movies = [element.getText() for element in list_of_elements]
list_of_movies.reverse()
for movie in list_of_movies:
    with open ("movies.txt", mode="a") as file:
        file.write(f"{movie}\n")
