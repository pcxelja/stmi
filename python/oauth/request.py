
class Request:

    OAUTH_PREFIX = "oauth_"

    def __init__(self, httpVerb, url):
        self.httpVerb = httpVerb
        self.url = url
        self.params = {}

    def addOAuthParam(self, key, value):
        self.params[key] = value
