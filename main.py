from settings import REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET, BOT_ID, PLAYLIST_ID, GROUPME_ACCESS
import requests
import json
from random import randint


def get_access_token():                                                 # Grab the access token
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    }
    response = requests.post(
        'https://accounts.spotify.com/api/token', data=data, auth=(
            CLIENT_ID, CLIENT_SECRET))

    return json.loads(response.content)['access_token']


def get_info():                                                         # Get the song, artist, album
    toke = get_access_token()
    response = requests.get(
        f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}", headers={
            "Authorization": "Bearer " + toke})
    response = json.loads(response.content)
    number_of_songs = response['tracks']['total']
    num = randint(0, number_of_songs - 1)
    song = response['tracks']['items'][num]
    artist = song['track']['artists'][0]['name']
    album = song['track']['album']['name']
    name = song['track']['name']
    return [name, artist, album]


def process_img():
    url = "https://dog.ceo/api/breed/shiba/images/random"               # Register and return shib link
    img = json.loads(requests.get(url).content)["message"]
    image_binary = requests.get(img).content
    url = "https://image.groupme.com/pictures"
    headers = {"X-Access-Token": GROUPME_ACCESS, "Content-Type": "image/jpeg"}

    response = requests.post(url, headers=headers, data=image_binary)
    return json.loads(response.content)['payload']['url']


def send_message():                                                     # Send song of month and shib
    info = get_info()
    msg = f"This month's song is {info[0]}, from {info[1]}'s {info[2]}."

    url = "https://api.groupme.com/v3/bots/post"
    data = {
        "bot_id": BOT_ID,
        "attachments": [
            {
                "type": "image",
                "url": process_img()
            }
        ]
    }

    print(requests.post(url, json=data).content)


if __name__ == "__main__":
    send_message()
