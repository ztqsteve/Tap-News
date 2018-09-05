from newsapi import NewsApiClient

NEWS_API_KEY = 'd161fdcfcaed4789989a8e3ead3a5077'

CNN = 'cnn'
DEFAULT_SOURCES = CNN

def getNewsFromSource(source=DEFAULT_SOURCES):
    articles = []
    # Init
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources=source)

    # Extract info from response
    if top_headlines is not None and top_headlines['status'] == 'ok':
       articles.extend(top_headlines['articles'])

    return articles
