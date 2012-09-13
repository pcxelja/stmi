#
# Tests for basestring module
#

import basestring
import request
import token
import oauth
import unittest

class BaseStringBuilderTest(unittest.TestCase):

    # Case:
    # POST https://api.twitter.com/oauth/request_token
    # ConsumerKey = El88ZRRULiEz3rjoPb5Sg
    # ConsumerSecret = b2vEQACuZ46fthEBkoVJ5bk4Wky0hAVMQ3cXArHsA
    # Token = 39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt
    # TokenSecret = 8OeytV7fBKcsuRuosjSC1AJNvohvuPbJTSVyZjtr4
    def test_restapi_request_token(self):
        # Given
        req = request.Request("POST", "https://api.twitter.com/oauth/request_token")
        req.addOAuthParam(oauth.NONCE, "ef8dbc91b7597bd3aa10d530200975b7")
        req.addOAuthParam(oauth.SIGN_METHOD, "HMAC-SHA1")
        req.addOAuthParam(oauth.TIMESTAMP, "1347511829")
        req.addOAuthParam(oauth.TOKEN, "39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt")
        req.addOAuthParam(oauth.VERSION, "1.0")
        req.addOAuthParam(oauth.CONSUMER_KEY, "El88ZRRULiEz3rjoPb5Sg") 
        # When
        builder = basestring.BaseStringBuilder()

        bs = builder.getBaseString(req)
        
        # Then
        baseString = "POST&https%3A%2F%2Fapi.twitter.com%2Foauth%2Frequest_token&oauth_consumer_key%3DEl88ZRRULiEz3rjoPb5Sg%26oauth_nonce%3Def8dbc91b7597bd3aa10d530200975b7%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1347511829%26oauth_token%3D39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt%26oauth_version%3D1.0"

        self.assertEqual(bs, baseString)

        auth = {"oauth_consumer_key" : "El88ZRRULiEz3rjoPb5Sg", "oauth_nonce" : "ef8dbc91b7597bd3aa10d530200975b7", "oauth_signature" : "Yym81IJgCDiymck6cxcgvkjZevc%3D", "oauth_signature_method" : "HMAC-SHA1", "oauth_timestamp" : "1347511829", "oauth_token" : "39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt", "oauth_version" : "1.0"}

        sign = builder.getSignature(bs, "b2vEQACuZ46fthEBkoVJ5bk4Wky0hAVMQ3cXArHsA", "8OeytV7fBKcsuRuosjSC1AJNvohvuPbJTSVyZjtr4")
        print(builder.encode(sign))
        print("")
        print(auth[oauth.SIGNATURE])

        authHeader = 'Authorization: OAuth oauth_consumer_key="El88ZRRULiEz3rjoPb5Sg", oauth_nonce="ef8dbc91b7597bd3aa10d530200975b7", oauth_signature="Yym81IJgCDiymck6cxcgvkjZevc%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1347511829", oauth_token="39660721-HXaLQHl9yRe0BuJlk6CRNRhHeJSxUhT2G4Mz2EsQt", oauth_version"="1.0"'
