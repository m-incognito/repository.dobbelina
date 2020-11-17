# requests for fetching html of website
import requests
import re

# Make the GET request to a url
r = requests.get('https://freevideo.cz/vase-videa/nejnovejsi/')
# r = requests.get('https://freevideo.cz/vase-videa/nejnovejsi/stranka-1547.html')
# Extract the content
listhtml = r.text

match = re.compile('<a href="([^"]+)" class="pagination__next">', re.DOTALL | re.IGNORECASE).search(listhtml)
if(match):
    nextPageLink = match.group(1)

print(nextPageLink)
#   Changed regex current 19.01.22
# videopage, img, hd, duration, name
match = re.compile('class="video video-preview".*?'
'<a href="([^"]+)".*?'
'image_ultra_2x="([^"]+)".*?'
'duration">.*?([\w:]+).*?'
'(?:quality">.*?(\w+).*?)?'
'<h5 class="video__description">([^<]+)', 
re.DOTALL | re.IGNORECASE).findall(listhtml)

#   Changed var order 19.01.22
for videopage, img, duration, quality, name in match:
    if(quality):
        print(quality)

    print(videopage)
    print(img)
    print("Duration "+ duration)
    print("Quality "+ quality)
    print(name)

listhtml = r.text

r = requests.get('https://freevideo.cz/vase-videa/prsata-panicka-a-jeji-sukaci-hracka-1122437.html')
listhtml = r.text

match = re.compile('<source src="([^"]+)".*?label="(\w+)"', re.DOTALL | re.IGNORECASE).findall(listhtml)
for link, quality in match:
    print(link)
    print(quality)
