import twint
import schedule
import time


# you can change the name of each "job" after "def" if you'd like.


def job_1():
    print("Fetching Tweets")
    c = twint.Config()
    c.Search = "#COVID19"
    c.Since = "2019-12-01"
    c.Until = "2020-04-01"
    c.Lang = "en"
    c.Near = "US"
    c.Database = 'tweets.db'
    twint.run.Search(c)

def job_2():
    print("Fetching Tweets")
    c = twint.Config()
    c.Search = "#C19"
    c.Since = "2019-12-01"
    c.Until = "2020-04-01"
    c.Lang = "en"
    c.Near = "US"
    c.Database = 'tweets.db'
    twint.run.Search(c)

def job_3():
    print("Fetching Tweets")
    c = twint.Config()
    c.Search = "#CoronaVirus"
    c.Since = "2019-12-01"
    c.Until = "2020-04-01"
    c.Lang = "en"
    c.Near = "US"
    c.Database = 'tweets.db'
    twint.run.Search(c)

def job_4():
    print("Fetching Tweets")
    c = twint.Config()
    c.Search = "#StayHome"
    c.Since = "2019-12-01"
    c.Until = "2020-04-01"
    c.Lang = "en"
    c.Near = "US"
    c.Database = 'tweets.db'
    twint.run.Search(c)


# run once when you start the program
job_1()
job_2()
job_3()
job_4()

schedule.every().second.do(job_1)
schedule.every().second.do(job_2)
schedule.every().second.do(job_3)
schedule.every().second.do(job_4)

while True:
    schedule.run_pending()
    time.sleep(1)
