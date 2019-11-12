#!usr/bin/python3

import requests

GOTAPI_CHAR = 'https://anapioficeandfire.com/api/characters'

def main():
    # Send HTTPS GET to API of Fire and Ice
    gotcharlookup = input("What is the name of the character we should lookup? ")
    # 
    gotresp = requests.get(GOTAPI_CHAR + "?name" + gotcharlookup)

    # Decode the response (taking response object and stripping off the JSON)
    gotdj = gotresp.json()
                                

if __name__ == "__main__":
    main()


