#!usr/bin/python3

import requests
import argparse
import time
import hashlib

# Define the API we want to lookup
XAVIER = 'https://gateway.marvel.com/v1/public/characters'

def hashbuilder(timestamp, privkey, pubkey):
    return hashlib.md5((timestamp+privkey+pubkey).encode('utf-8')).hexdigest()

def marvelcharcall(timestamp, marvel_hash, privkey, pubkey, lookmeup):
    resp = requests.get(f"{XAVIER}?name={lookmeup}&ts={timestamp}&apikey={pubkey}&hash={marvel_hash}")
    return resp.json()

def main():
    
    # Capture the private key
    with open(args.dev) as mccoy:
        privkey = mccoy.read().strip('\n')

    # Capture the public key
    with open(args.pub) as munroe:
        pubkey = munroe.read().strip('\n')

    # Generate timestamp - create an integer from a float timestamp (for our RAND)
    timestamp = str(time.time()).rstrip('.')

    # Build hash with hashbuilder(timestamp, privatekey, publickey)
    marvel_hash = hashbuilder(timestamp, privkey, pubkey)

    # Call the API with marvelcharcall(timestamp, hash, publickey, character)
    uncannyxmen = marvelcharcall(timestamp, marvel_hash, privkey, pubkey, args.name)

    # Display results
    print(uncannyxmen)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the path to the private Marvel developer key')
    parser.add_argument('--pub',  help='Provide the path to the public Marvel developer key')
    parser.add_argument("--name", help="Provide the character name to lookup")
    args = parser.parse_args()
    main()
