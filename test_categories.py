# requests for fetching html of website
import requests
import re

# Make the GET request to a url
r = requests.get('https://freevideo.cz/vase-videa/kategorie/')
# Extract the content
listhtml = r.text

#   Changed regex current 19.01.22
# videopage, img, hd, duration, name
match = re.compile('<a href="([^"]+)" class="category">.*?'
'data-original="([^"]+)".*?'
'category__description">.*?(\w+).*?</h5>', 
re.DOTALL | re.IGNORECASE).findall(listhtml)


r = requests.get('https://www.adultempire.com/hottest-pornstars.html?pageSize=300&fq=ag_cast_gender%3aF')
# Extract the content
listhtml = r.text

#   Changed regex current 19.01.22
# videopage, img, hd, duration, name
match = re.compile('Label="([^"]+)"><picture>.*?min-width: 1600px.*?srcset="([^"]+)"', 
re.DOTALL | re.IGNORECASE).findall(listhtml)

print(match)