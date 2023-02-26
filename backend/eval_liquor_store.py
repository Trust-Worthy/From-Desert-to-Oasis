from serpapi import GoogleSearch
import geopy.distance as gd
import gMapsApi

def mapscall(query, longitute, latitude):
    """
    Calls Google Search Api with a query: "liquor store"
    longitude: longitude of zip code entered by user
    latitude: latitude of zip code entered by user
    """
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
    return local_results

    # in local_results there will be different positions.
    # there will be about 20 different positions
    #each position has a title which is the name of the grocery store (I need to snag this)
    #i also want the address field of the specific grocery store
    # I also want the unique location id
    # I also need the gps_coordinates field it has the lat and long. 
    # I will do my distance calculation on this

def create_search_result_dict(local_results):
    '''Creates a sub dictionary of the important information from the search results 
    like title of liquor store, unique id (google api), gps_coordinates'''
    liq_dict = {}
    #grocery_store_dict[key] = value
    # grocery_store_dict[title of liq store] = [address, unique id, {lat:num, long:num}] 
    for position in local_results:
        count = 0
        if position["title"] in liq_dict:
            liq_dict[position["title"] + str(count)] = [position["address"],position["data_cid"],position["gps_coordinates"]]
            count += 1 # if there are multiple of the same liq chain, they should show up
        liq_dict[position["title"]] = [position["address"],position["data_cid"],position["gps_coordinates"]]

    return liq_dict

def is_zip_near_liquor(dict,zip_lat, zip_long):
    # distances = [] I don't really need this 
    sum = 0
    count = 0
    # food_desert = False # don't need this
    for key in dict:
        gps_coordinates = dict[key][2]
        lat = gps_coordinates["latitude"]
        long = gps_coordinates["longitude"]
        coords_1 = (zip_lat,zip_long)
        coords_2 = (lat,long)
        '''Calculate distance of lat and long from lat and long of zip code'''
        distance = gd.geodesic(coords_1, coords_2).miles
        sum += distance
        count += 1
        # distances.append(distance) don't really need this
        
        
    average_distance = sum / count
    # if average_distance < 1.5:
    #      food_desert == True
    # elif average_distance >= 10: # consensus of what how what constitutes a food desert in a non urban area (10 miles)
    #         food_desert = True
    # else:
    #     food_desert = False

    return average_distance

def main():
    zipcode = "80022"
    query = "liquor store"
    liq_json_lat_long = gMapsApi.google_geocoding(zipcode)
    lat_long = gMapsApi.getLongLat(liq_json_lat_long)
    zip_lat = lat_long[0]
    zip_long = lat_long[1]

    local_results = mapscall(query,zip_lat,zip_long)
    liq_store_dict = create_search_result_dict(local_results)
    liq_answer = is_zip_near_liquor(liq_store_dict,zip_lat, zip_long)

    print(liq_answer)

if __name__ == "__main__":
    main()