import gMapsApi
import eval_food_desert as efd
import eval_liquor_store as els


def main():
    zipcode = input("Please enter a five digit zip code: ")
    json_lat_long = gMapsApi.google_geocoding(zipcode) # this is where you enter your zip code or place
    lat_long = gMapsApi.getLongLat(json_lat_long)
    zip_lat = lat_long[0]
    zip_long = lat_long[1]

    """
    Distance from zip code to grocery store
    """
    local_results = efd.mapscall("grocery store",zip_lat,zip_long)
    grocery_store_dict = efd.create_search_result_dict(local_results)
    answer = efd.is_zip_in_a_desert(grocery_store_dict,zip_lat,zip_long)

    """
    Distance from zip code to liquor store
    """
    local_liquor_results = els.mapscall("liquor store",zip_lat,zip_long)
    liquor_store_dict = els.create_search_result_dict(local_liquor_results)
    lq_answer = els.is_zip_near_liquor(liquor_store_dict,zip_lat,zip_long)

    desert = ""
    final = round(answer[-1],2)
    final_lq = round(lq_answer,2)

    if answer[-2] == True:
        desert += "a food desert"
    else:
        desert += "not a food desert"

    print(f"The zipcode: {zipcode} is {desert} \n{zipcode} is an average distance of {final} miles away from a grocery store \n{zipcode} is also an average distance of {final_lq} miles away from a liquor store")
    # print(grocery_store_dict)

if __name__ == "__main__":
    main()