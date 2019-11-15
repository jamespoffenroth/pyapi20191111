#!/user/bin/python3

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = requests.get(MAJORTOM)

    helmet = groundctrl.json()

    print(type(helmet))

    for astro in helmet["people"]:
        print(astro["name"])





if __name__ == "__main__":
    main()

