from flask import Flask

CrimeServer = Flask(__name__)

@CrimeServer.route('/')
def apiRequest():
    return 'hello world'