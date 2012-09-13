#
# Class for OAuth Service
# Based on Scribe OAuth service implementation

import request
import token
import time
import random
import oauth

class Service:

    def __init__(self, api, apiKey, apiSecret):
        self.api = api
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.signature = "header"

    def getRequestToken(self):
        req = request.Request(self.api.getRequestTokenVerb(), self.api.getRequestTokenEndpoint())
        tok = token.Token("","")

        req.addOAuthParam(oauth.CALLBACK, oauth.OUT_OF_BAND)
        self.addOAuthParams(req, tok)
        self.appendSignatur(req)

    def getAccessToken(self, requestToken, verifier):
        pass

    def signRequest(self, accessToken, request):
        pass

    def addOAuthParams(self, request, token):
        req.addOAuthParam(oauth.NONCE, self.getNonce())
        req.addOAuthParam(oauth.TIMESTAMP, self.getTimestamp())
        req.addOAuthParam(oauth.CONSUMER_KEY, self.apiKey)
        req.addOAuthParam(oauth.SIGN_METHOD, "HMAC-SHA1")
        req.addOAuthParam(oauth.VERSION, "1.0")
        req.addOAuthParam(oauth.SIGNATURE, self.getSignature(req, tok))

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
