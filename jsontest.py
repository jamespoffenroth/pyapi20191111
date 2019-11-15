#!/usr/bin/python3

import requests
import json

DATEURL = 'http://date.jsontest.com/'
IPURL = 'http://ip.jsontest.com/'
GETURL = 'http://validate.jsontest.com/'
POSTURL = 'http://validate.jsontest.com/'

def main():
    # Make the request to pull a time object from date.jsontest.com
    resp = requests.get(DATEURL)
    # Strip off JSON response, and convert to Pythonic list/dict
    respjson = resp.json()
    # Pull out the value associated with the KEY "date"
    mytime = respjson["date"]
    print("The current date is: " + mytime)

    # Make the request to pull the IP from ip.jsontest.com
    resp = requests.get(IPURL)
    # Strip off JSON response, and convert to Pythonic list/dict
    respjson = resp.json()
    # Pull out the value associated with the KEY "ip"
    myip = respjson["ip"]
    print("The IP of my VM is: " + myip)

    # Read a list of hosts out of a flat file
    with open("myservers.txt") as myfile:
        mysvrs = myfile.readlines()
    # Second method to read a list of hosts out of a flat file
    myfile = open('myservers.txt')
    mysrvs = myfile.read()
    print(mysrvs)
    
    # Test data to validate as legal JSON. When a POST json= is replaced by the KEY 'json',
    # the key 'json' is mapped to a VALUE of the json to test. Because the test item is a
    # string, we can include whitespaces.
    # Format for requests to validate.jsontest.com is:
    # data={"json": "json_you want to validate_as_a_string"}
    jsonToTest = {}
    jsonToTest['time'] = mytime
    jsonToTest['ip'] = myip
    jsonToTest['mysrvs'] = mysrvs
    mydata = {}
    mydata["json"] = str(jsonToTest)

    #print(f"Is your JSON valid? {respjson["validate"]}")
    
    # Use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=mydata)
    # Strip off JSON response, and convert to Pythonic list/dict
    respjson = resp.json

    # Display our Pythonic list/dict
    print(respjson)

    # Just display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
