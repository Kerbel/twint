from multiprocessing import Process
from threading import Thread

import twint
import schedule
import time

hashtags = ['#COVID19',
            '#C19',
            'Corona',
            'CORONA',
            'corona',
            '#Corona',
            '#CORONA',
            '#corona',
            'Coronavirus',
            'CoronaVirus',
            'CORONAVIRUS',
            '#Coronavirus',
            '#CoronaVirus',
            '#CORONAVIRUS'
            ]


def job(hashtag):
    c = twint.Config()
    c.Search = hashtag
    c.Since = "2019-12-01"
    c.Until = "2020-05-01"
    c.Lang = "en"
    c.Near = "US"
    c.Database = 'new_tweets.db'
    twint.run.Search(c)


def fetch_hashtags():
    for hashtag in hashtags:
        job(hashtag)


# fetch_hashtags()

# while True:
#     thread = Thread(target=fetch_hashtags)
#     thread.start()
#     time.sleep(1)

def job():
    c = twint.Config()
    c.Search = '#COVID19'
    c.Since = "2019-12-01"
    c.Until = "2020-04-15"
    c.Lang = "en"
    c.Near = "US"
    c.Database = 'tweets'
    twint.run.Search(c)


job()

# schedule.every().second.do(job)

# while True:
#     # schedule.run_pending()
#     thread = Thread(target=job)
#     thread.start()
#     time.sleep(0.05)

