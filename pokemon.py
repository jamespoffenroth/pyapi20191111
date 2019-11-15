#!/usr/bin/python3

# We are passing an argument from the command line when we run the script.
# You have to run the script like this (where 'heal' is the word we search for):
# python3 pokemon.py heal

# For making HTTP requests
# python -m pip install requests
import requests
# For accepting arguments from the cmd line
import argparse
# For working with data in lots of formats
# python3 -m pip install pandas 
import pandas as pandas

# We are limited by default to 20 items returned at the PokeAPI site, so you need to add ?limit=1000 to increase the limit
POKEURL = "http://pokeapi.co/api/v2/pokemon/?limit=1000"
ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    # Make HTTP GET request using requests, and decode JSON attachment as pythonic data structure 
    pokemon = requests.get(POKEURL)
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        print(poke["name"])
    
    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")


    # Make HTTP GET request using requests, and decode JSON attachment as pythonic data structure
    # Uses a different method to increase the number of items returned by our query
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    # Create a list to store items that contain the word we searched on
    matchedwords = []

    # Loop through data, and add all items to a list
    for item in items.get("results"):
        # Check to see if the current item's VALUE mapped to item["name"] contains the word "heal"
        if args.searchword in item.get("name"):
            # If true, add that item to the list
            matchedwords.append(item.get("name"))
    
    print(f"There are {len(matchedwords)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    # Make a dataframe from our list
    itemsdf = pandas.DataFrame(matchedwords)
    # Export to MS Excel format
    # IMPORTANT: you need to install openpyxl in order for this to work
    # python3 -m pip install openpyxl
    # index=False prevents printing out the index numbers`
    itemsdf.to_excel("pokemonitems.xlsx", index=False)
    # Export to CSV format
    itemsdf.to_csv("pokemonitems.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search the Pokemon Item API: ")
    parser.add_argument('searchword', type=str, default='ball', help="Pass in any word. Default is 'ball'.")
    args = parser.parse_args()
    main()
