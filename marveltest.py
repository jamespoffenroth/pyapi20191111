#!usr/bin/python3

import requests
import time
import hashlib
import pprint

# Define the API we want to lookup
XAVIER = 'https://gateway.marvel.com/v1/public/characters'

def hashbuilder(timestamp, privkey, pubkey):
    return hashlib.md5((timestamp+privkey+pubkey).encode('utf-8')).hexdigest()

def marvelcharcall(timestamp, marvel_hash, privkey, pubkey):
    resp = requests.get(f"{XAVIER}?ts={timestamp}&apikey={pubkey}&hash={marvel_hash}")
    return resp.json()

def main():
    
    # Capture the private key
    with open("/home/student/marvel_priv", "r") as mycreds:
        privkey = mycreds.read()
    privkey = privkey.strip('\n')

    # Capture the public key
    with open("/home/student/marvel_pub", "r") as mycreds1:
        pubkey = mycreds1.read()
    pubkey = pubkey.strip('\n')

    # Generate timestamp - create an integer from a float timestamp (for our RAND)
    timestamp = str(time.time()).rstrip('.')

    # Build hash with hashbuilder(timestamp, privatekey, publickey)
    marvel_hash = hashbuilder(timestamp, privkey, pubkey)

    # Call the API with marvelcharcall(timestamp, hash, privatekey, publickey)
    uncannyxmen = marvelcharcall(timestamp, marvel_hash, privkey, pubkey)

    # Display results
    pprint.pprint(uncannyxmen)

## Define arguments to collect
if __name__ == '__main__':
    main()
