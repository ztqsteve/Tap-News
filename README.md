# Tap News
## Overview
This is a real-time news scraping and recommendation system. I built a news pipeline to scraping real-time latest news from a bunch of news source such as CNN, BBC, ESPN and TechCrunch. Created a single-page web application to show the news to users, and recommend news to users based on users' click behavior on different news topic. 
## Architecture
<img src="tap-news-architecture.png" />

### News Pipeline
News pipeline is composed by news monitor, web scraper and news deduper, news is sent and received between them by RabbitMQ which decouples these components. The news monitor use [News API](https://newsapi.org) to derive latest news and store news title MD5 digest into Redis to avoid sending same news to the message queue. The web scraper use a third party package [Newspaper](https://newspaper.readthedocs.io/en/latest/) to fetch news articles from offical news website. News depuper implements TF-IDF to calculate similarity of news to avoid storing same news from different news source into MongoDB. For similar news, only store the one published firstly.
### Machine Learning
The news topic classification is implemented by Convolutional Neutral Nework(CNN) in TensorFlow and deployed online.
