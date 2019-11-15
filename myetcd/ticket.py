#!/usr/bin/python3

import requests

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"

# Function to read all available tickets
# - use a GET on a directory to return all results
def gettickets():
    resp = requests.get(ETCD)
    resp = resp.json()
    if resp.get("errorCode"):
        return False
    else:
        ticketlist = []
        for ticket in resp.get("node").get("nodes"):
            ticketlist.append(ticket.get("key").lstrip("/tickets/"))
        return ticketlist
     
# Function to get a specific ticket
# - pass in the ticket to GET
def getoneticket(ticketid):
    # issue an HTTP GET to our keys/requests
    resp = requests.get(ETCD)
    resp = resp.json()
    for ticket in resp.get("node").get("nodes"):
        existingticket = ticket.get("key").lstrip("/tickets/")
        if ticketid == existingticket:
            ticketinfo = ticket.get("value")
            return ticketinfo
        
# Function to create a ticket
# - use a POST to create a new ticket
def createticket(descofissue):
    resp = requests.post(ETCD, data={'value': descofissue})
    resp = resp.json()
    resp = resp.get("node").get("key").lstrip("/tickets/")
    return resp

# Function to update a ticket
# - pass in the ticket to PUT
def updateticket(ticketnum, descofissue):
    resp = requests.get(ETCD)
    ## print(dir(resp))
    ## print(resp.status_code)
    resp = resp.json()
    for ticket in resp.get("node").get("nodes"):
        existingticket = ticket.get("key").lstrip("/tickets/")
        if existingticket == ticketnum:
            oldinfo = ticket.get("value")
            ## BUSTED --> newinfo = requests.put(ETCD, data={'value': descofissue})

            ## newinfo is a response code generated from our HTTP PUT
            newinfo = requests.put(f"{ETCD}/{ticketnum}", data={'value': descofissue})

            ## strip off the JSON from the response code (assuming it is there)
            ## AND transform into a dict
            newinfo = newinfo.json()

            ## I have NO idea what this new dict looks like. So display it.
            # print(newinfo.get('node').get('value'))
            # The above line is the "safer" version of the line below
            ## print(newinfo["node"]["value"])
            newinfo = newinfo.get('node').get('value') 
            ticketinfo = [ticketnum, oldinfo, newinfo]
            return ticketinfo

# Function to delete a ticket
# - pass in the ticket to DELETE
def deleteticket(ticketid):
    resp = requests.get(ETCD)
    resp = resp.json()
    for ticket in resp.get("node").get("nodes"):
        existingticket = ticket.get("key").lstrip("/tickets/")
        if existingticket == ticketid:
            deletedticket = requests.delete()
    


# Function to delete all tickets
# - use the API parameter ?dir=true&recursive=true to remove a dictionary

def main():
    # Enter a while true loop (run until a break condition)
    while True:

        # Pop up a menu to do the following:
        print('''
        # 1.) Read all available tickets
        # 2.) Get a specific ticket
        # 3.) Create a ticket
        # 4.) Update a ticket
        # 5.) Delete a ticket
        # 6.) Exit
        # 7.) DANGER! Delete all tickets
        ''')
       
        # Collect input from client
        userinput = ""
        while userinput == "":
            userinput = input("> ")

        # If user wants all available tickets, call the gettickets function
        if userinput == "1":
            ticketlist = gettickets()
            if ticketlist:
                for ticket in ticketlist:
                    print(f"Ticket ID - {ticket}")
            else:
                print("There are no tickets in the sytem.")

        # If user wants a single ticket, call the getoneticket function         
        elif userinput == "2":
            ticketid = input("What is the ticket ID? ")
            ticketinfo = getoneticket(ticketid)
            print(f"{ticketid} ticket information: {ticketinfo}")

        # If user wants to create a ticket, call the createticket function
        elif userinput == "3":
            descofissue = input("Give a short 140 char description of the issue: ")
            createdticket = createticket(descofissue)
            print(f"Ticket {createdticket} has been created.")

        # If user wants to update a ticket, call the updateticket function
        elif userinput == "4":
            ticketnum = input("What is the ticket number you want to update? ") 
            descofissue = input("What is the updated 140 char description of the issue? ")
            updatedticket = updateticket(ticketnum, descofissue)
            print("Ticket number " + str(updatedticket[0]))
            print("Old ticket information was: " + str(updatedticket[1]))
            print("New ticket information is: " + str(updatedticket[-1]))

        # If user wants to delete a ticket, call the deleteticket function
        elif userinput == "5":
            ticketid = input("What is the ticket number of the ticket you want to delete? ")
            deleteticket(ticketid)
            print(f"Ticket {ticketid} deleted.")

        #
        elif userinput == "6":
            break

        else:
            print("That is not a valid option.")

    print("Thanks for using the Alta3 RESTful ticketing service!")

if __name__ == "__main__":
    main()
