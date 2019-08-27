#!/usr/bin/python3
'Fetches URL content through URLlib'

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    htmlcont = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(htmlcont)))
    print('\t- content:', htmlcont)
    print('\t- utf8 content:', htmlcont.decode('utf-8'))
