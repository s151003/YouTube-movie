import rstr
import urllib.request
from time import sleep

while True:
    vidid = rstr.xeger(r'[a-zA-Z0-9-_]{10,12}')
    url = "https://i.ytimg.com/vi/"+vidid+"/1.jpg"

    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
        print("found!!! "+url)
        break
    except:
        print(vidid+"not found")
        sleep(0.4)