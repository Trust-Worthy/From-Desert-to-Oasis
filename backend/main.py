from serpapi import GoogleSearch
import gMapsApi



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
    print(results)
    for key in results:
        print(key)
    local_results = results["local_results"]
    # in local_results there will be different positions.
    # there will be about 20 different positions
    #each position has a title which is the name of the grocery store (I need to snag this)
    #i also want the address field of the specific grocery store
    # I also want the unique location id
    # I also need the gps_coordinates field it has the lat and long. 
    # I will do my distance calculation on this
    for position in local_results:
        print(position)
    return local_results

def calc_long_lat_of_results(local_results):
    grocery_store_list = []
    grocery_store_dict = {}
    #grocery_store_dict[key] = value
        # grocery_store_dict[title of grocery store] = [address, unique id, (lat, long)] 
    for position in local_results:
        grocery_store_list.append(position["title"])
    
    #     grocery_store_list.append(position["title"])
    # for position in local_results:

        



def main():
    '''@param for google_geocoding has to be a string'''
    json_lat_long = gMapsApi.google_geocoding("80239") # this is where you enter your zip code or place
    lat_long = gMapsApi.getLongLat(json_lat_long)


    local_results = mapscall("grocery store",lat_long[0],lat_long[1])
    calc_long_lat_of_results(local_results)
    # for key in results:
    #     print(key)



if __name__ == "__main__":
    main()