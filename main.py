import requests
from twilio.rest import Client
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "1142c18856f1666d6a10b03fe2740c86"
account_sid = "AC53ec109fd4521b121d3b8a25052aca93"
auth_token = "06696ced934f4b1c3a91ee40f9c4c21c"
parameters = {
    "lat": 25.204849,
    "lon": 55.270782,
    "appid": api_key,
    "exclude" : "current,minutely,daily"
}

#+14706348198
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
condition_code = [hour_data["weather"][0][id] for hour_data in weather_slice]

will_rain = False 
for code in condition_code:
    if int(code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Bring an umbrella.It's going to rain today",
                        from_='+14706348198',
                        to='+15558675310'
                    )
    print(message.sid)

