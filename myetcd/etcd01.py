#!/usr/bin/python3

import requests
import pprint

def main():

    # issue an HTTP PUT transaction to store our data within /keys/requests
    # the value http for humans, and the response, as the object r
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans'})
    r.status_code # return the status code associated with object r
    pprint.pprint(r.json()) # pretty print the json associated with object r
    
    print('*******************')
    
    # issue an HTTP PUT to replace the value of keys/requests
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans, version 2'})
    r.status_code
    pprint.pprint(r.json())
    
    print('*******************')
    
    # issue an HTTP GET to our keys/requests
    r = requests.get("http://127.0.0.1:2379/v2/keys/requests")
    r.status_code
    pprint.pprint(r.json())

    r = requests.delete("http://127.0.0.1:2379/v2/keys/requests")
    r.status_code
    pprint.pprint(r.json())
    
if __name__ == "__main__":
    main()
