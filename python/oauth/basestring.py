# Class for building base strings

# For building baseString
import urllib
import collections

import hashlib
import hmac
import binascii

class BaseStringBuilder:

    def __init__(self):
        pass

    def getBaseString(self, request):
        result = ""
        result += request.httpVerb
        result += "&"
        result += self.encode(request.url)
        result += "&"
        result += self.getSortedAndEncodedParams(request)
        return result

    def getSortedAndEncodedParams(self, request):
        result = ""
        od = collections.OrderedDict(sorted(request.params.items()))
        for k, v in od.iteritems():
            result += k + "=" + v + "&"
        result = result[:-1]
        return self.encode(result)

    def encode(self, part):
        result = urllib.quote(part, "")
        return result

    def getSignature(self, baseString, apiSecret, tokenSecret):
        keyString = self.encode(apiSecret) + "&" + self.encode(tokenSecret)
        return self.doSign(baseString, keyString)

    def doSign(self, baseString, key):
        hashed = hmac.new(key, baseString, hashlib.sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]
