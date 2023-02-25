import requests
import googlemaps
from datetime import datetime

def google_geocoding():
    gmaps = googlemaps.Client(key='AIzaSyDZG6AM2xR2VBSemt9FBJqYHzM8DVKpM-U')

    # Geocoding an address
    geocode_result = gmaps.geocode('80239')
    return geocode_result


# def ninja_api(city,state):
#     '''Takes in a city and returns longitude and latitude of that city'''
    
#     api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&state={}country=UnitedStates&'.format(city,state)
#     response = requests.get(api_url + city, headers={'X-Api-Key': ''})
#     if response.status_code == requests.codes.ok:
#        print(response.text)
#        return response.text
#     else:
#        return "Error:", response.status_code, response.text


def getLongLat(json_file):
    for keys in json_file:
        for key in keys:
            print(key)
    answer = json_file[0]["geometry"]["bounds"]["northeast"]
    latitude = answer["lat"]
    longitude = answer["lng"]
    return latitude,longitude

def ziptolonglat(zipcode):
    '''Converts a zipcode to Longitude and Latitude'''


def main():
    city = "Denver"
    state = "Colorado"

    result = google_geocoding()
    lat_long = getLongLat(result)
    print(lat_long)
    # json_response = ninja_api(city,state)
    # print(json_response)

    # long_lat = getLongLat(json_response,state)
    # print(long_lat)


   


if __name__ == "__main__":
    main()