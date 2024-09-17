import requests
import os
from dotenv import load_dotenv
load_dotenv()



OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("API_KEY")
LAT = 6.268720 # Example latitude
LON = 100.439522 # Example longitude
CNT = 4 # Number of forecast periods to check (all today)

def bring_umbrella():

    bot_token = os.getenv("bot_token")
    bot_chatID = os.getenv("bot_chatID")
    bot_message = "Bring umbrella, It's raining today ☂️⚡"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID +'&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": CNT
}

respond = requests.get(OWM_ENDPOINT, params=parameters)
respond.raise_for_status()
weather_data = respond.json()

for i in range(CNT):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        bring_umbrella()
        break

