#!usr/bin/python3

import requests

GOTAPI_BOOKS =' https://anapioficeandfire.com/api/books'

def main():
    # Send HTTPS GET to API of Fire and Ice
    gotresp = requests.get(GOTAPI_BOOKS)

    # Decode the response (taking response object and stripping off the JSON)
    gotdecodedjson = gotresp.json()

    # Loop across response
    for singlebook in gotdecodedjson:
        # Each of these will print the same thing (title of each book, and number of pages)
        print(singlebook["name"] + ",", "pages -", singlebook["numberOfPages"])
        #print("{}, pages - {}".format(singlebook["name"], singlebook["numberOfPages"]))
        #print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")    
        print("ISBN:" + singlebook["isbn"])
        print("Publisher:" + singlebook["publisher"])

        count = 0
        for number in singlebook["characters"]:
            count += 1

        # print(f"No. of characters {len(singlebook['characters'])}")

        print(count)
    
    # Accepts user input
    gotchar = input("Enter a character number: ")

    # Loops through dictionaries
    for singlebook in gotdecodedjson:
        # Obtains char ID by spliting each character URL on '/', and adds the last index to a new value 
        for character in singlebook["characters"]:
            char_split = character.split('/')
            char_number = char_split[-1]

            if char_number == gotchar:
                # New call to get character specific data, then convert JSON data to list
                charlookup = requests.get(character)
                charlookup = charlookup.json()
                # Print character name
                print(f'The character {charlookup["name"]} appears in {singlebook["name"]}')
                                

if __name__ == "__main__":
    main()


