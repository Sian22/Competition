import requests
#import urllib.requests
import re
import time
import json
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = 'https://events.st-andrews.ac.uk/calendar/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll("div", {"id": re.compile("^event_")})

#print(a)

for tag in a:
    # x = tag.find('script').text
    # print(x)
    # x.strip("\n")
    # y = json.loads(x)
    # print(y["name"])
    name = tag.find("span", itemprop="name")
    info = tag.findAll("em")
    for em in info:
        print(em.text)

with open("myExcitingNewFile.json", "w+") as f:
    f.write("TEST")

# stuff
response = requests.post(
    url='https://www.googleapis.com/calendar/v3/calendars/56k9m5dm433q41r7u3vf3i4fgv21fcfi@import.calendar.google.com/events/quickAdd',
    data={
        'text': 'EVENT_TEXT',
    },
    headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ACCESS_TOKEN',
    },
)
response.raise_for_status()
print(response.json())
