#
# Class for OAuth Service
# Based on Scribe OAuth service implementation

import request
import token
import time
import random

TIMESTAMP = "oauth_timestamp";
SIGN_METHOD = "oauth_signature_method";
SIGNATURE = "oauth_signature";
CONSUMER_SECRET = "oauth_consumer_secret";
CONSUMER_KEY = "oauth_consumer_key";
CALLBACK = "oauth_callback";
VERSION = "oauth_version";
NONCE = "oauth_nonce";
PARAM_PREFIX = "oauth_";
TOKEN = "oauth_token";
TOKEN_SECRET = "oauth_token_secret";
OUT_OF_BAND = "oob";
VERIFIER = "oauth_verifier";
HEADER = "Authorization";

class Service:

    def __init__(self, api, apiKey, apiSecret):
        self.api = api
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.signature = "header"

    def getRequestToken(self):
        req = request.Request(self.api.getRequestTokenVerb(), self.api.getRequestTokenEndpoint())
        tok = token.Token("","")

        req.addOAuthParam(CALLBACK, OUT_OF_BAND)      # Done
        req.addOAuthParam(NONCE, self.getNonce())             # Done
        req.addOAuthParam(TIMESTAMP, self.getTimestamp())     # Done
        req.addOAuthParam(CONSUMER_KEY, self.apiKey)  # Done
        req.addOAuthParam(SIGN_METHOD, "HMAC-SHA1")   # Done
        req.addOAuthParam(VERSION, "1.0")             # Done
        req.addOAuthParam(SIGNATURE, self.getSignature(req, tok))     # Done
        print(req.params)

    def getNonce(self):
        return str(self.currMilis())

    def getTimestamp(self):
        return str(self.randInt32())

    def currMilis(self):
        return int(round(time.time() * 1000))

    def randInt32(self):
        return random.randint(0, 2**32 - 1)

    def getSignature(self, request, token): # TODO
        baseString = self.extractBaseString(request)
        print(baseString)
        pass

    def extractBaseString(request):
        print("base string extract")
