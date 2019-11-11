#!/usr/bin/python3

def main():
    mylist = []
    
    # Append works by opening up a single slot a the END of the list and inserting the value
    mylist.append("192.168.102.55")
    mylist.append("10.10.0.1")
    print(mylist)

    ## Extend works by intereating access the value passed, and opening up that may slots at the endo fo the list
    myotherlist = []
    myotherlist.extend("abcdefg")
    # myotherlist == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(myotherlist)

    lastlist = ['The', 'big']
    lastlist.extend(['red', 'dog'])
    print(lastlist)


if __name__ == "__main__":
    main()

    
