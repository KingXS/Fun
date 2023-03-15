import requests
import sys
import json

def main(domain):
    url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
    querystring = {"children_only":"false","include_inactive":"true"}
    headers = {
        "Accept": "application/json",
        "APIKEY": "i1gOG8L4HSVyijsk7dqHDVsDPuAJcN3m"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).text
    list = json.loads(response)["subdomains"]
    f = open(domain+'.txt','w+')
    for i in range(0,len(list)):
        f.write("https://"+str(list[i])+"."+domain+"\r\n")
    f.close()

if __name__ == '__main__':
    domain = sys.argv[1]
    main(domain)