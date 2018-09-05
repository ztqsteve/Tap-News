# -*- coding: utf-8 -*-

import datetime
import os
import sys

from dateutil import parser
from sklearn.feature_extraction.text import TfidfVectorizer

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://xzbggvzn:jFOMw3MZ6hzq0htegQTkG2S7fQsrNby1@chimpanzee.rmq.cloudamqp.com/xzbggvzn"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"


SLEEP_TIME_IN_SECONDS = 1

NEWS_TABLE_NAME = 'news'

SAME_NEWS_SIMILARITY_THRESHOLD = 0.8

cloudAMQP_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)


def handle_message(msg):
    if msg is None or not isinstance(msg, dict) :
        return
    task = msg
    text = task['text']
    if text is None:
        return

    # Get all recent news
    published_at = parser.parse(task['publishedAt'])
    published_at_day_begin = datetime.datetime(published_at.year, published_at.month, published_at.day, 0, 0, 0, 0)
    published_at_day_end = published_at_day_begin + datetime.timedelta(days=1)

    db = mongodb_client.get_db()
    recent_news_list = list(db[NEWS_TABLE_NAME].find({'publishedAt' : {'$gte': published_at_day_begin,
                                                                  '%lt' : published_at_day_end}}))

    if recent_news_list is not None and len(recent_news_list) > 0:
        documents = [str(news['text']) for news in recent_news_list]
        documents.insert(0, text)

        # Calculate similarity matrix
        tfidf = TfidfVectorizer().fit_transform(documents)
        pairwise_sim = tfidf * tfidf.T

        print(pairwise_sim)

        rows, _ = pairwise_sim.shape

        for row in range(1, rows):
            if pairwise_sim[row, 0] > SAME_NEWS_SIMILARITY_THRESHOLD:
                # Duplicated news, ignore.
                print 'Duplicated news, ignore.'
                return

        task['publishedAt'] = parser.parse(task['publishedAt'])
        db[NEWS_TABLE_NAME].replace_one({'digest': task['digest']}, task, upsert=True)

while True:
    if cloudAMQP_client is not None:
        msg = cloudAMQP_client.getMessage()
        if msg is not None:
            # Parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                print(e)
                pass

        cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)
