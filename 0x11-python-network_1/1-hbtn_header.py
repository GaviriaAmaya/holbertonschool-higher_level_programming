#!/usr/bin/python3
'Takes a URL, send a request and displays X-Request-id'

import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        htmlreq = response.info()
        print(dict(htmlreq).get('X-Request-Id'))
