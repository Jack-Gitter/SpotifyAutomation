import requests
import json
import base64

from requests.api import head

class R():
    
    def __init__(self):
        
        self.refresh_token = "AQCAkLUVRJ912s7ErEAtBL8WHnYH2QXECtLMbkwIkbIyALC5RXLA5Ae-ZqjKpYDWM7aA74KnrCT6yR93oFlTbBPg5zMlAzNKL8elJy89hFeTflOcnP7UWmqhiKPRpxZV7Mk"
        self.base_64 = base64.urlsafe_b64encode("c455cc070ac34d9791ca1c06d6170210:1c0d43f2f4c44ce2b8b6dfc836214016".encode()).decode()
    
    def refresh(self):
        result = requests.post(
            "https://accounts.spotify.com/api/token", 
        headers={
            "Authorization": "Basic " + self.base_64
        },
        data={
            "grant_type":"refresh_token",
            "refresh_token":self.refresh_token,
        })

        result_json = result.json()
        return result_json['access_token']
