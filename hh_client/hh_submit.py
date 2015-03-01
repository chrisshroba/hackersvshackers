__author__ = 'chrisshroba'

import urllib
import urllib2
import sys

url = 'http://localhost:1337/submit'
values = {'answer': sys.argv[1],
          'team': 'red',
          }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page