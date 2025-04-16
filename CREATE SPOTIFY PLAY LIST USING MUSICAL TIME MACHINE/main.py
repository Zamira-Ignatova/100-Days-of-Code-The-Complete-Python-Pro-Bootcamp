import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

#set environment virables
os.environ["SPOTIPY_CLIENT_ID"] = "your-client-id"
os.environ["SPOTIPY_CLIENT_SECRET"] = "your-client-secret"
os.environ["SPOTIPY_REDIRECT_URI"] = "your-redirection-uri"
# get environment virables
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
desired_date = input("Which year would you like to travel to? Type the date in YYYY-MM-DD format:\n")
URL = f"https://www.billboard.com/charts/hot-100/{desired_date}/"
year = desired_date[:4]

#get the top 100 songs from billboard for a particular date
response = requests.get(url=URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "html.parser")
list_of_elements = soup.select(selector=" ul li ul li h3", class_="c-title", id="title-of-a-story")
top_100_songs = [element.getText().strip() for element in list_of_elements]

#Create a SpotifyOAuth object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    scope="playlist-modify-private",
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri= SPOTIPY_REDIRECT_URI,
    cache_path="token.txt",
    show_dialog=True,
))

user_id = sp.current_user()["id"]

uri_of_songs = []
for song in top_100_songs:
    query = f"track:{song} year:{year}"
    result = sp.search(q=query, type="track", limit=1, market="US")
    try:
        uri = result['tracks']['items'][0]['uri']
        uri_of_songs.append(uri)
    except IndexError:
        print(f"The song: '{song}' doesn't exist in Spotify currently.")
# create a playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{desired_date} Billboard 100", public=False, collaborative=False, description='Songs from the past')
# add tracks to a particular playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_of_songs)
