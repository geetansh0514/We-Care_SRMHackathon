import requests
import json
import os

def getIpLoc(ip):
    print('My public IP address is: {}'.format(ip))
    ipresponse = requests.get("http://api.ipstack.com/{}?access_key=06a3cc3488fe04144c6bae754f4d3bcb".format(ip)).json()
    return((ipresponse['latitude'],ipresponse['longitude']))