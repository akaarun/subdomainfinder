#!/usr/bin/env python
import requests

def sending_subdomain_request(url):
    try:
        return requests.get("https://"+url)
    except:
        pass


print("\n")

#Getting user input

print("Enter target domain without wwww or https example == google.com or wwe.com")
target_domain_url = input("Give your target url >> ")

print('Enter the filename with ".txt" extension example == subdomainlist.txt')
what_will_be_the_file_name = input("Give your file name >> ")

if not target_domain_url:
    print("please give target domain")
    exit()

if not what_will_be_the_file_name:
    print("please enter file name")
    exit()
elif what_will_be_the_file_name.find(".txt") == -1:
    what_will_be_the_file_name + ".txt"




#Opening wordlist file
subdomain_wordlist_file = open("subdomain.txt","r")
iterating_subdomain_wordlist_file = iter(subdomain_wordlist_file)


#sending request of each subdomain
while True:
    try:
        iterting_wordlist = iterating_subdomain_wordlist_file.__next__()
        spliting_iterting_wordlist = iterting_wordlist.strip()
        final_url = spliting_iterting_wordlist + "." + target_domain_url
        response = sending_subdomain_request(final_url)
        print("Testing this url >> "+ final_url)
        # print("\n")
        if response:
            print("Discovered Domain => " + final_url)
            create_finding_subdomain_file = open(what_will_be_the_file_name,"a")
            create_finding_subdomain_file.write(final_url + "\n")

    except:
          exit()