
class HttpMethods:
    HEAD, GET, POST, PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH = range(9)

class Request:

    OAUTH_PREFIX = "oauth_"

    def __init__(self, httpMethod = None, urlString = None):
        self.method = httpMedhod
        self.url = ulrString

