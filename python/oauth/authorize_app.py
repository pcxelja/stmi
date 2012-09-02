#!/usr/bin/python

import time
import random

# URLs form twitter API

# REST API Documentation for request_token
# Example Request
# Request URL:
# POST https://api.twitter.com/oauth/request_token

# Request POST Body:
# N/A

# Authorization Header:
# OAuth 
# oauth_nonce="K7ny27JTpKVsTgdyLdDfmQQWVLERj2zAK5BslRsqyw", 
# oauth_callback="http%3A%2F%2Fmyapp.com%3A3005%2Ftwitter%2Fprocess_callback", 
# oauth_signature_method="HMAC-SHA1", 
# oauth_timestamp="1300228849", 
# oauth_consumer_key="OqEqJeafRSF11jBMStrZz", 
# oauth_signature="Pc%2BMLdv028fxCErFyi8KXFM%2BddU%3D", 
# oauth_version="1.0"

# Response:
# oauth_token=Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik&oauth_token_secret=Kd75W4OQfb2oJTV0vzGzeXftVAwgMnEK9MumzYcM&oauth

# Definitions for API methods
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token=%s"
REQUEST_TOKEN_RESOURCE = "api.twitter.com/oauth/request_token"
ACCESS_TOKEN_RESOURCE = "api.twitter.com/oauth/access_token"

# GLOBAL DEFINITIONS for consumer key and consumer secret
Consumer_key = ""
Consumer_secret = ""

def call_request_token():
    # This constitutes a request
    httpMethod = "POST"
    urlEndpoint = "https://api.twitter.com/oauth/request_token"
    callback = "oob" # This is indication for out of band authentication

    # OAuth parameters for request, i.e. authorization
    # We will use dictionary, because this is most appropriate python data type for this
    req_params = {}
    # Params that need to be filled in are:

    req_params["oauth_nonce"] = noonce_param()
    req_params["oauth_callback"] = "oop" 
    req_params["oauth_signature_method"] = "HMAC-SHA1"
    req_params["oauth_timestamp"] = timestamp_param()
    req_params["oauth_consumer_key"] = Consumer_key
    req_params["oauth_signature"] = generate_signature()
    req_params["oauth_version"] = "1.0"
    return req_params
    
# Functions for time and noonce
def timestamp_param():
    return str(currentMilis())

def noonce_param():
    return str(currentMilis() + getRandomInt32())

def currentMilis():
    value = int(round(time.time() * 1000))
    return value

def getRandomInt32():
    return random.randint(0, 2**32 - 1)

def generate_signature():
    return ""

def get_signature(baseString, apiSecret, tokenSecret):
    pass

def do_sign(


if __name__ == "__main__":
    print("Python authorization of oauth app")
    print(call_request_token())
    pass
