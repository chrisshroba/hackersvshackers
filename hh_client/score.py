__author__ = 'chrisshroba'


__author__ = 'chrisshroba'

import urllib2

url = 'http://localhost:1337/score'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page