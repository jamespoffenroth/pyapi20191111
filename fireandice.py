#!usr/bin/python3

import requests

GOTAPI =' https://anapioficeandfire.com/api'

def main():
    # Send HTTPS GET to API of Fire and Ice
    gotresp = requests.get(GOTAPI)

    # Decode the response (taking response object and stripping off the JSON)
    gotdecodedjson = gotresp.json()
    print(gotdecodedjson)

    


if __name__ == "__main__":
    main()


