import urllib.request
import sys

if len(sys.argv)!=3:
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]


url = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, stopid))
data = url.read()

from xml.etree.ElementTree import  XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)