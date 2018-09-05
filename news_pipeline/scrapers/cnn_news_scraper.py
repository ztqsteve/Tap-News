import requests
import random
import os

from lxml import html

GET_CNN_NEWS_XPATH = '''//div[@class='zn-body__paragraph']//text() |
                        //div[@class='zn-body__paragraph speakable']//text() |
                        //p[@class='zn-body__paragraph speakable']//text() |
                        //p[@class='zn-body__paragraph']//text()'''

# Load user agents
USER_AGENTS_FILE = os.path.dirname(os.path.abspath(__file__)) + '/user_agents.txt'
print USER_AGENTS_FILE
USER_AGENTS = []


with open(USER_AGENTS_FILE, 'r') as uaf:
    for ua in uaf.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1:-1])

random.shuffle(USER_AGENTS)

def getHeaders():
    ua = random.choice(USER_AGENTS)
    headers = {
        'Connection': 'close',
        'User-Agent': ua
    }
    return headers

def extract_news(news_url):
    # Fetch .html
    session_requests = requests.session()
    response = session_requests.get(news_url, headers=getHeaders())

    news = {}

    try:
        # Parse html
        tree = html.fromstring(response.content)
        # Extract information

        news = tree.xpath(GET_CNN_NEWS_XPATH)
        news = ''.join(news)
    except Exception as e:
        print e
        return {}

    return news
