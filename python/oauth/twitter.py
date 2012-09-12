# Module for twitter API urls packed into a class
# As in java scribe library

class TwitterApi:

    def __init__(self):
        pass

    # Request Token methods

    def getRequestTokenEndpoint(self):
        return "http://api.twitter.com/oauth/request_token"

    def getRequestTokenVerb(self):
        return "POST"

    # Access Token methods

    def getAccessTokenEndpoint(self):
        return "http://api.twitter.com/oauth/access_token"

    def getAccessTokenVerb(self):
        return "POST"

    def getAuthorizationUrl(self, token):
        return "https://api.twitter.com/oauth/authorize?oauth_token=" + token.getToken()

    
