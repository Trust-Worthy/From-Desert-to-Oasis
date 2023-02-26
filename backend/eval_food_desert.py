from serpapi import GoogleSearch
import gMapsApi
import geopy.distance as gd

def mapscall(query, longitute, latitude):

    params = {
    "engine": "google_maps",
    "q": query,
    "ll": "@{},{},15.1z".format(longitute,latitude), # this parameter has to be in the form of longitude and latitude
    "type": "search",
    "api_key": "c52a3473dc247da70f68ad0adea3b618890bce432d6f30714c438ab9e1e139dd"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    local_results = results["local_results"]
    # in local_results there will be different positions.
    # there will be about 20 different positions
    #each position has a title which is the name of the grocery store (I need to snag this)
    #i also want the address field of the specific grocery store
    # I also want the unique location id
    # I also need the gps_coordinates field it has the lat and long. 
    # I will do my distance calculation on this
    return local_results

def create_search_result_dict(local_results):
    '''Creates a dictionary of the important information from the search results 
    like title of grocery store, unique id (google api), gps_coordinates'''
    grocery_store_dict = {}
    #grocery_store_dict[key] = value
    # grocery_store_dict[title of grocery store] = [address, unique id, {lat:num, long:num}] 
    for position in local_results:
        count = 0
        if position["title"] in grocery_store_dict:
            grocery_store_dict[position["title"] + str(count)] = [position["address"],position["data_cid"],position["gps_coordinates"]]
            count += 1 # if there are multiple of the same grocery chain, they should show up
        grocery_store_dict[position["title"]] = [position["address"],position["data_cid"],position["gps_coordinates"]]

    return grocery_store_dict

        
def is_zip_in_a_desert_URBAN(dict,zip_lat, zip_long):
    distances = []
    for key in dict:
        gps_coordinates = dict[key][2]
        lat = gps_coordinates["latitude"]
        long = gps_coordinates["longitude"]
        coords_1 = (zip_lat,zip_long)
        coords_2 = (lat,long)
        '''Calculate distance of lat and long from lat and long of zip code'''
        distance = gd.geodesic(coords_1, coords_2).miles 
        distances.append(distance)
        food_desert = False
        if distance > 1: # consensus of what how what constitutes a food desert in a non urban area (1 miles)
            food_desert = True
    return distances, food_desert

def is_zip_in_a_desert_NON_URBAN(dict,zip_lat, zip_long):
    distances = []
    for key in dict:
        gps_coordinates = dict[key][2]
        lat = gps_coordinates["latitude"]
        long = gps_coordinates["longitude"]
        coords_1 = (zip_lat,zip_long)
        coords_2 = (lat,long)
        '''Calculate distance of lat and long from lat and long of zip code'''
        distance = gd.geodesic(coords_1, coords_2).miles 
        distances.append(distance)
        food_desert = False
        if distance > 10: # consensus of what how what constitutes a food desert in a non urban area (10 miles)
            food_desert = True

    return distances,food_desert


def main():
    '''@param for google_geocoding has to be a string'''
    json_lat_long = gMapsApi.google_geocoding("80239") # this is where you enter your zip code or place
    lat_long = gMapsApi.getLongLat(json_lat_long)
    zip_lat = lat_long[0]
    zip_long = lat_long[1]

    local_results = mapscall("grocery store",zip_lat,zip_long)
    grocery_store_dict = create_search_result_dict(local_results)
    answer = is_zip_in_a_desert_NON_URBAN(grocery_store_dict,zip_lat,zip_long)
    print(answer)
    

if __name__ == "__main__":
    main()