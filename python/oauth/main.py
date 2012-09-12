#!/usr/bin/python

import twitter
import service
import request

def main():
    ta = twitter.TwitterApi()
    serv = service.Service(ta, "api-consumer-key", "api-consumer-secret")
    token = serv.getRequestToken()

if __name__ == "__main__":
    main()
