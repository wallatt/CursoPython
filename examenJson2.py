import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving',url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print('retrieved', len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    print('Place ID',js["results"][0]["place_id"])