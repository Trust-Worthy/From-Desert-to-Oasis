import gMapsApi
import eval_food_desert as efd
'''I just realized I can't complete my project this way because I don't have
enough free searched available on my serpapi api. I only get 100'''

def iterate_zip_codes():
    zip_codes = []
    file = open("../txtfiles/zipcode.txt") # all zip codes in district of columbia

    for line in file:
        data = line.split()
        zip_codes.append(data[0])

    return zip_codes

def dc_zip_food_desert(zipcode):
    zips_tested = {}
    for zip in zipcode:
        result = gMapsApi.google_geocoding(zip)
        lat_long = gMapsApi.getLongLat(result)
        zip_lat = lat_long[0]
        zip_long = lat_long[1]
        local_results = efd.mapscall("Grocery Store",zip_lat,zip_long)
        grocery_store_dict = efd.create_search_result_dict(local_results)
        answer = efd.is_zip_in_a_desert_URBAN(grocery_store_dict,zip_lat,zip_long)

        zips_tested[zip] = answer[-1]
    print(zips_tested)


def main():
    dc_zip_codes = iterate_zip_codes()
    dc_zip_food_desert(dc_zip_codes)


if __name__ == "__main__":
    main()