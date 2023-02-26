import gMapsApi
import eval_food_desert as efd



def main():
    zipcode = input("Please enter a five digit zip code ")
    json_lat_long = gMapsApi.google_geocoding(zipcode) # this is where you enter your zip code or place
    lat_long = gMapsApi.getLongLat(json_lat_long)
    zip_lat = lat_long[0]
    zip_long = lat_long[1]

    local_results = efd.mapscall("grocery store",zip_lat,zip_long)
    grocery_store_dict = efd.create_search_result_dict(local_results)
    answer = efd.is_zip_in_a_desert(grocery_store_dict,zip_lat,zip_long)

    if answer[0]:
        t = "a food desert"
    else:
        t = "not a food desert"

    print("This zipcode: " + zipcode + " is " + t)
    print()
    print("A grocery store is an average distance of " + str(answer[2]) + " miles away from \nthis location")
    

if __name__ == "__main__":
    main()