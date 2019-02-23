from flask import Flask
import requests

CrimeServer = Flask(__name__)

@CrimeServer.route('/')
def apiRequest():
    return 'hello world'