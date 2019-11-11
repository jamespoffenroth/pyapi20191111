#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    # I want to grab by creds
    with open("/home/student/creds", "r") as mycreds:
        nasacreds = mycreds.read()

    # remove any new line characters from the API key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off JSON
    apod = apodresp.json()
    
    print(apod["title"])
    print(apod["date"])
    print(apod["explanation"]) 
    print(apod["url"])

if __name__ == "__main__":
    main()

