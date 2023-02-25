from serpapi import GoogleSearch

def mapscall():

    params = {
    "engine": "google_maps",
    "q": "pizza",
    "ll": "@40.7455096,-74.0083012,15.1z",
    "type": "search",
    "api_key": ""
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    local_results = results["local_results"]
    return local_results


def main():
    results = mapscall()



if __name__ == "__main__":
    main()