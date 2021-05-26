import requests
import json
import refresh

class SpotifyAutomator():

    def __init__(self):
        self.user_id = "22hz5uldr7fru6jhkuou6zgja"
        self.spotify_token = refresh.R().refresh()
        self.song_uris = ""

    def get_songs(self, playlist_id):
        response = requests.get(
            "https://api.spotify.com/v1/playlists/"+str(playlist_id)+"/tracks",
            headers={
                "Authorization": f"Bearer {self.spotify_token}"
            },
            params={
                "market":"PL"
            }
        )
        
        response_json = response.json()

        for i in response_json['items']:
            if i != (len(response_json['items'])-1):
                self.song_uris += str(i['track']['uri']) + ","
            else:
                self.song_uris += str(i['track']['uri'])
    
    def clear_songs(self):
        self.song_uris = ""

    def add_songs(self, playlist_id):
        response = requests.post(
            "https://api.spotify.com/v1/playlists/"+str(playlist_id)+"/tracks",
            headers={
                "Authorization": f"Bearer {self.spotify_token}",
                "Content-Type":"application/json"
            },
            params={
                "uris":self.song_uris
            }
        )
        print(response.text)

