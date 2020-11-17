# requests for fetching html of website
import requests
import re

# Make the GET request to a url
r = requests.get('https://www.katedrala.cz/')
# Extract the content
listhtml = r.text

match = re.compile('<form name="URLform" action="(.*?)"', re.DOTALL | re.IGNORECASE).search(listhtml)
if(match):
    post_action = match.group(1)
    print(post_action)

    data = {
        "URL": "https://freevideo.cz"
    }
    r = requests.post(post_action, data)

    text = r.text

    print(type(text))
    print(r.encoding)
    text = text.replace('&amp;','&')
    text = text.replace('&#8211;','-')
    text = text.replace('&ndash;','-')
    text = text.replace('&#038;','&')
    text = text.replace('&#8217;','\'')
    text = text.replace('&#8216;','\'')
    text = text.replace('&#8220;','"')
    text = text.replace('&#8221;','"')
    text = text.replace('&#8230;','...')
    text = text.replace('&quot;','"')
    text = text.replace('&#039;','`')
    text = text.replace('&ntilde;','ñ')
    text = text.replace('&rsquo;','\'')
    text = text.replace('&#133;','...')
    text = text.replace('&#40;', '(')
    text = text.replace('&#41;', ')')
    text = text.replace('&nbsp;', ' ')

    print(r.text)