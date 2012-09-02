#!/usr/bin/python
import urllib2

def build_base_string(params):
    base = ""
    base += params['method']
    base += "&"
    base += encode_url(params['url'])
    base += "&"
    return base

def encode_url(url):
    print(url)
    value = urllib2.quote(url, "")
    return value

def params1():
    params = {}
    params['method'] = "POST"
    params['url'] = "https://api.twitter.com/oauth/request_token ~*"
    return params

def main():
    print(build_base_string(params1()))
    pass

if __name__ == "__main__":
    main()
