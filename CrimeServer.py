from flask import Flask
import requests
import recieveJSON
import json

CrimeServer = Flask(__name__)

@CrimeServer.route('/')
def apiRequest():
    y = recieveJSON.getRestaurants("icecream", -74.7771916 , 40.272249099999996, 5)['businesses'][0]['name']
    return y
if __name__ == '__main__':
    CrimeServer.run() 
