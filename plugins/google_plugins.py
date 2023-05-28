import os
import requests
# https://developers.google.com/maps/documentation/geocoding/overview

def geocode_address(address: str) -> tuple[float, float]:
    api_key = os.getenv("GOOGLE_API_KEY")

    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            error_message = data.get('error_message', 'Error in geocoding request.')
            print(f"Geocoding request failed. Error message: {error_message}")
    else:
        print("Error connecting to the Google Maps Geocoding API.")
    # convert google geo code to baidu geo code


    return [latitude, longitude]

