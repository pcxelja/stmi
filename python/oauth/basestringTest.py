#
# Tests for basestring module
#

import basestring
import request
import token

class BaseStringBuilderTest(unittest.TestCase):

    def __init__(self):
        pass

    # Case:
    # POST https://api.twitter.com/oauth/request_token
    # ConsumerKey = El88ZRRULiEz3rjoPb5Sg
    # ConsumerSecret = b2vEQACuZ46fthEBkoVJ5bk4Wky0hAVMQ3cXArHsA
    # Token = 39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt
    # TokenSecret = 8OeytV7fBKcsuRuosjSC1AJNvohvuPbJTSVyZjtr4
    def restapi_request_token():
        # Given
        nonce = "ef8dbc91b7597bd3aa10d530200975b7"
        sig_method = "HMAC-SHA1"
        timestamp = "1347511829"
        token = "39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt"
        req = request.Request("POST", "https://api.twitter.com/oauth/request_token")
        req.addOAuthParam(
        # When

        # Then
        baseString = "POST&https%3A%2F%2Fapi.twitter.com%2Foauth%2Frequest_token&oauth_consumer_key%3DEl88ZRRULiEz3rjoPb5Sg%26oauth_nonce%3Def8dbc91b7597bd3aa10d530200975b7%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1347511829%26oauth_token%3D39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt%26oauth_version%3D1.0"
        auth = {oauth_consumer_key="El88ZRRULiEz3rjoPb5Sg", oauth_nonce="ef8dbc91b7597bd3aa10d530200975b7", oauth_signature="Yym81IJgCDiymck6cxcgvkjZevc%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1347511829", oauth_token="39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt", oauth_version="1.0"}

        authHeader = 'Authorization: OAuth oauth_consumer_key="El88ZRRULiEz3rjoPb5Sg", oauth_nonce="ef8dbc91b7597bd3aa10d530200975b7", oauth_signature="Yym81IJgCDiymck6cxcgvkjZevc%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1347511829", oauth_token="39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt", oauth_version="1.0"'
