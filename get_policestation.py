import googlemaps
import pandas as pd
import time

# API_KEY = "AIzaSyADQ3ItHf0lKjPndIM7pbkaDBr0u002N4E"
map_client = googlemaps.Client(API_KEY)

def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0

lat = float(input("Enter the latitude: "))
lon = float(input("Enter the longitude: "))
location = (lat, lon)

search_string = 'polica station'
distance = miles_to_meters(20)
list = []

response = map_client.places_nearby(
    Location = location,
    keywork = search_string,
    radius = distance
)

list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        Location = location,
        keywork = search_string,
        radius = distance
    )
    list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

df = pd.DataFrame(list)
df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
df.to_excel('Police_station.xlsx', inddex = False)




    
 