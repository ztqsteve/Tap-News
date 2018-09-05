import cnn_news_scraper as scraper

EXPECTED_NEWS = "The United States is not some banana republic with a two-tiered system of justice"
CNN_NEWS_URL = "https://www.cnn.com/2018/09/04/politics/democrats-senators-donald-trump-jeff-sessions-tweet/index.html"

def test_basic():
    news = scraper.extract_news(CNN_NEWS_URL)

    assert EXPECTED_NEWS in news
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()
