from flask import Flask
import requests
import YelpAPI
import json

CrimeServer = Flask(__name__)

@CrimeServer.route('/')
def apiRequest():
    y = json.load(YelpAPI.getRestaurants("icecream", -74.7771916 , 40.272249099999996, 5))
    return y.text()
if __name__ == '__main__':
    CrimeServer.run() 