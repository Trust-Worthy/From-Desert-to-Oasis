from serpapi import GoogleSearch
import convert



def mapscall(query, longitute, latitude):

    params = {
    "engine": "google_maps",
    "q": query,
    "ll": "@40.7455096,-74.0083012,15.1z", # this parameter has to be in the form of longitude and latitude
    "type": "search",
    "api_key": "c52a3473dc247da70f68ad0adea3b618890bce432d6f30714c438ab9e1e139dd"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    local_results = results["local_results"]
    return local_results


def main():
    results = mapscall("liquor stores")
    print(results)



if __name__ == "__main__":
    main()