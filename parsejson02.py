#!/usr/bin/python3

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    '''reading json from api'''
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)


    # strip off the attachment and read it
    helmet = groundctrl.read()

    print(helmet)


    # converts to utf-8, which gets rid of the little 'b' and quote '
    helmetson = json.loads(helmet.decode('utf-8'))

    #should say string
    print(type(helmet))

    #should say list or dict
    print(type(helmetson))


    print(helmetson["number"])
    
    print(helmetson["people"])

    print(helmetson["people"][0])


    #display every item in a list
    for astro in helmetson["people"]:
        print(astro)

    for astro in helmetson["people"]:
        print(astro["name"])




if __name__ == "__main__":
    main()

